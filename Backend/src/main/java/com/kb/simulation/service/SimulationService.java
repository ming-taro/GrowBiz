package com.kb.simulation.service;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.kb.simulation.dto.question.Question;
import lombok.RequiredArgsConstructor;
import org.bson.Document;
import org.bson.types.ObjectId;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;

@RequiredArgsConstructor
@Service
@PropertySource({"classpath:/application.properties"})
public class SimulationService {
    @Value("${ai.analysis.path}")
    private String aiAnalysisPath;

    private final MongoTemplate mongoTemplate;
    private final String QUESTION_ID = "ind";
    private final String SIMULATION_RESPONSE_COLLECTION = "simulation_response";

    public Question<?> findQuestionById(int id) {
        Query query = new Query();
        query.addCriteria(Criteria.where(QUESTION_ID).is(id));
        Question<?> question = mongoTemplate.findOne(query, Question.class);

        return question;
    }

    public <T> List<Question<T>> findQuestions() {
        List<LinkedHashMap> rawData = mongoTemplate.findAll(LinkedHashMap.class, "questions");
        ObjectMapper objectMapper = new ObjectMapper();
        List<Question<T>> questions = new ArrayList<>();

        for (LinkedHashMap<String, Object> data : rawData) {
            if (data.get("_id") instanceof ObjectId) {
                data.put("_id", data.get("_id").toString());
            }
            Question<T> question = objectMapper.convertValue(data, new TypeReference<Question<T>>() {});
            questions.add(question);
        }

        return questions;
    }

    public Document createResponse(String answer) {
        Document document = Document.parse(answer);
        return mongoTemplate.save(document, SIMULATION_RESPONSE_COLLECTION);
    }

    public Document findResponseById(String id) {
        Query query = new Query();
        query.addCriteria(Criteria.where("_id").is(id));
        return mongoTemplate.findOne(query, Document.class, SIMULATION_RESPONSE_COLLECTION);
    }

    public String executeSimulation(String id) {
        List<String> result = new ArrayList<>();
        try {
            File workingDirectory = new File(aiAnalysisPath);
            String scriptPath = "report.py";

            ProcessBuilder processBuilder = new ProcessBuilder("python3", scriptPath, id);
            processBuilder.directory(workingDirectory);
            processBuilder.redirectErrorStream(true);

            Process process = processBuilder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
                result.add(line);
            }

            String[] text =  result.get(result.size() - 1).split(" ");
            String reportId = text[text.length - 1];

            return reportId;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}
