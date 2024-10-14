package com.kb.simulation.service;

import com.kb.simulation.dto.question.Question;
import lombok.RequiredArgsConstructor;
import org.bson.Document;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.List;

@RequiredArgsConstructor
@Service
public class SimulationService {
    private final MongoTemplate mongoTemplate;
    private final String QUESTION_ID = "ind";
    private final String SIMULATION_RESPONSE_COLLECTION = "simulation_response";

    public Question<?> findQuestionById(int id) {
        Query query = new Query();
        query.addCriteria(Criteria.where(QUESTION_ID).is(id));
        Question<?> question = mongoTemplate.findOne(query, Question.class);

        return question;
    }

    public List<Question> findQuestions() {
        List<Question> question = mongoTemplate.findAll(Question.class);
        return question;
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



    public int executeSimulation(String id) {
        StringBuilder result = new StringBuilder();
        try {
            File workingDirectory = new File("C:/Users/student/Desktop/final/self-employed/AI_Models/AI/");
            String scriptPath = "ts_report.py";

            ProcessBuilder processBuilder = new ProcessBuilder("python", scriptPath, id);
            processBuilder.directory(workingDirectory);
            processBuilder.redirectErrorStream(true);

            Process process = processBuilder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
                result.append(line);
            }
            return process.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return -1;
    }
}
