package com.kb.simulation.service;

import com.kb.simulation.dto.question.Question;
import org.bson.Document;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SimulationService {
    private final MongoTemplate mongoTemplate;
    private final String QUESTION_ID = "ind";

    @Autowired
    public SimulationService(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

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

    public Document saveAnswer(String answer) {
        Document document = Document.parse(answer);
        return mongoTemplate.save(document, "simulation_response");
    }
}
