package com.kb.simulation.service;

import com.kb.simulation.dto.question.LocationQuestion;
import com.kb.simulation.dto.question.Question;
import com.kb.simulation.dto.question.StoreQuestion;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import javax.xml.stream.Location;
import java.util.List;

@Service
public class SimulationService {
    private final MongoTemplate mongoTemplate;
    private final int LOCATION_QUESTION_IND = 1;

    @Autowired
    public SimulationService(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    public LocationQuestion findLocationQuestion() {
        Query query = new Query();
        query.addCriteria(Criteria.where("ind").is(LOCATION_QUESTION_IND));
        return mongoTemplate.findOne(query, LocationQuestion.class);
    }

    public List<StoreQuestion> findStoreQuestions() {
        Query query = new Query();
        query.addCriteria(Criteria.where("ind").ne(LOCATION_QUESTION_IND));
        return mongoTemplate.find(query, StoreQuestion.class);
    }
}
