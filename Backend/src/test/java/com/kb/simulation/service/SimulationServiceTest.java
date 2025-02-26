package com.kb.simulation.service;

import com.kb._config.RootConfig;
import com.kb.simulation.dto.question.Question;
import com.kb.simulation.dto.test.ReportTest;
import lombok.extern.log4j.Log4j;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.TestPropertySource;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.context.web.WebAppConfiguration;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.*;

import static org.junit.jupiter.api.Assertions.*;

@WebAppConfiguration
@ExtendWith(SpringExtension.class)
@ContextConfiguration(classes = RootConfig.class)
@Slf4j
@TestPropertySource(locations = "classpath:application.properties")
class SimulationServiceTest {
    @Value("${spring.data.mongodb.host}")
    private String host;
    @Value("${spring.data.mongodb.port}")
    private int port;
    @Value("${spring.data.mongodb.database}")
    private String database;
    @Value("${spring.data.mongodb.username}")
    private String username;
    @Value("${spring.data.mongodb.password}")
    private String password;
    @Value("${spring.data.mongodb.authentication-database}")
    private String authenticationDatabase;
    @Value("${spring.data.mongodb.collection.report}")
    private String REPORT_COLLECTION;

    @Autowired
    private MongoTemplate mongoTemplate;

    // env 설정
    private static List<String> originalEnvLines = new ArrayList<>();
    private static Path envPath = Paths.get(System.getProperty("user.dir"), "../AI_Models", ".env");

    @Autowired
    private SimulationService simulationService;
    @Autowired
    private ReportService reportService;

    @BeforeEach
    void setup() throws IOException {
        String mongoUri = String.format("mongodb://%s:%s@%s:%d/%s?authSource=%s", username, password, host, port, database, authenticationDatabase);

        // .env 백업
        originalEnvLines = Files.readAllLines(envPath, StandardCharsets.UTF_8);

        // python .env 업데이트
        List<String> updatedLines = new ArrayList<>();
        for (String line : originalEnvLines) {
            if (line.startsWith("MONGO_URI=")) {
                updatedLines.add("MONGO_URI=" + mongoUri);
            } else if (line.startsWith("MONGO_DB_NAME=")) {
                updatedLines.add("MONGO_DB_NAME=" + database);
            }
            else {
                updatedLines.add(line);
            }
        }
        Files.write(envPath, updatedLines, StandardCharsets.UTF_8);
    }

    @AfterEach
    void tearDown() throws IOException {
        // .env 파일 복구
        Files.write(envPath, originalEnvLines, StandardCharsets.UTF_8);
        mongoTemplate.dropCollection(REPORT_COLLECTION);
    }

    @DisplayName("1개의 응답에 대한 보고서 생성 테스트")
    @Test
    void executeSimulation() {
        // Given
        String responseId = "67bab0d04a6d57312bde038a";

        // When
        String reportId = simulationService.executeSimulation(responseId);

        // Then
        assertEquals(reportService.findReportByResponseId(responseId), reportId);
    }

    @DisplayName("20개 응답에 대한 보고서 동시 생성 테스트")
    @ParameterizedTest
    @ValueSource(ints = {20})
    void executeSimulationByMultiRequest(int reportCount) throws ExecutionException, InterruptedException {
        List<String> responseIds = simulationService.findResponseByMemberId("foreigners");
        List<Future<ReportTest>> result = new ArrayList<>();
        ExecutorService pool = Executors.newFixedThreadPool(reportCount);

        for (int i = 0; i < reportCount; i++) {
            final String id = responseIds.get(i);
            result.add(pool.submit(() -> {
                long taskStartTime = System.currentTimeMillis();
                String reportId = simulationService.executeSimulation(id);
                long taskEndTime = System.currentTimeMillis();
                return new ReportTest(reportId, taskStartTime, taskEndTime, taskEndTime - taskStartTime);
            }));
        }
        pool.shutdown();

        for (int i = 0; i < reportCount; i++) {
            ReportTest report = result.get(i).get();
            assertEquals(reportService.findReportByResponseId(responseIds.get(i)), report.getReportId());
        }
    }

    @DisplayName("2개 응답에 대한 보고서 동시 생성 테스트")
    @Test
    void executeSimulationByTwoRequest() throws ExecutionException, InterruptedException {
        int reportCount = 2;
        List<String> responseIds = simulationService.findResponseByMemberId("foreigners");
        List<Future<ReportTest>> result = new ArrayList<>();

        CountDownLatch latch = new CountDownLatch(reportCount);
        ExecutorService pool = Executors.newFixedThreadPool(reportCount);

        long startTime = System.currentTimeMillis();
        for (int i = 0; i < reportCount; i++) {
            final String id = responseIds.get(i);
            try {
                result.add(pool.submit(() -> {
                    long taskStartTime = System.currentTimeMillis();
                    String reportId = simulationService.executeSimulation(id);
                    long taskEndTime = System.currentTimeMillis();
                    latch.countDown();
                    return new ReportTest(reportId, taskStartTime, taskEndTime, taskEndTime - taskStartTime);
                }));
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }

        latch.await();
        long endTime = System.currentTimeMillis();

        pool.shutdown();

        System.out.println();
        for (int i = 0; i < reportCount; i++) {
            assertFalse(reportService.findById(result.get(i).get().getReportId()).isEmpty());
            log.info((i + 1) + "번 보고서 결과 = " + result.get(i).get());
        }

        log.info("총 보고서 개수 = " + reportCount + ", 생성된 보고서 개수 = " + result.size());
        log.info("시작 시간 = " + startTime + ", 종료 시간 = " + endTime);
        log.info("전체 소요 시간 = " + (endTime - startTime) + "ms");
    }

    @DisplayName("시뮬레이션 질문 조회 테스트")
    @Test
    void findQuestions() {
        List<Question<Object>> questions = simulationService.findQuestions();

        Assertions.assertFalse(questions.isEmpty(), "조회된 질문이 없습니다.");

        for (Question<Object> question : questions) {
            Assertions.assertNotNull(question.getId(), "조회한 질문의 ID가 null입니다.");
        }
    }
}