package com.kb.simulation.service;

import com.kb._config.RootConfig;
import com.kb.simulation.dto.question.Question;
import lombok.extern.log4j.Log4j;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.extension.ExtendWith;
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
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

import static org.junit.jupiter.api.Assertions.*;

@WebAppConfiguration
@ExtendWith(SpringExtension.class)
@ContextConfiguration(classes = RootConfig.class)
@Log4j
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

    private ExecutorService pool = Executors.newFixedThreadPool(10);

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
        String responseId = "679f30e9180a3c12d217707c";

        // When
        String reportId = simulationService.executeSimulation(responseId);

        // Then
        assertEquals(reportService.findReportByResponseId(responseId), reportId);
    }

//    @DisplayName("10 개의 응답에 대한 보고서 동시 생성 테스트")
//    @Test
//    void executeSimulationByMultiRequest() throws ExecutionException, InterruptedException {
//        List<String> responseIds = new ArrayList<>();
//        List<Future<String>> result = new ArrayList<>();
//
//        for (String id: responseIds) {
//            result.add(pool.submit(() -> simulationService.executeSimulation(id)));
//        }
//
//        pool.shutdown();
//
//        for (Future<String> future: result) {
//            System.out.println("결과 = " + future.get());
//            assertTrue(future.isDone());
//        }
//    }

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