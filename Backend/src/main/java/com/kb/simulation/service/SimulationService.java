package com.kb.simulation.service;

import com.kb.simulation.dto.question.Question;
import lombok.RequiredArgsConstructor;
import org.bson.Document;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

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
}
