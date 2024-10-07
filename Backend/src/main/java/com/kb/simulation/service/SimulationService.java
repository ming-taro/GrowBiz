//package com.kb.simulation.service;
//
//import com.kb.simulation.dto.question.Question;
//import com.kb.simulation.dto.question.Seoul;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.data.mongodb.core.MongoTemplate;
//import org.springframework.data.mongodb.core.query.Criteria;
//import org.springframework.data.mongodb.core.query.Query;
//import org.springframework.stereotype.Service;
//
//import java.util.List;
//
//@Service
//public class SimulationService {
//    private final MongoTemplate mongoTemplate;
//    private final int LOCATION_QUESTION_IND = 1;
//
//    @Autowired
//    public SimulationService(MongoTemplate mongoTemplate) {
//        this.mongoTemplate = mongoTemplate;
//    }
//
//    public Question<?> findQuestionByInd(int ind) {
//        Query query = new Query();
//        query.addCriteria(Criteria.where("ind").is(ind));
//        Question<?> question = mongoTemplate.findOne(query, Question.class);
//
//        return question;
//    }
//
//    public List<Question> findQuestions() {
//        List<Question> question = mongoTemplate.findAll(Question.class); // 일반적인 Question 클래스를 사용
//        return question;
//    }
//}
