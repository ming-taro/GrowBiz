package com.kb.simulation.service;

import com.kb.simulation.dto.report.RequestReport;
import com.kb.simulation.dto.report.ResponseReport;
import lombok.RequiredArgsConstructor;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;

@RequiredArgsConstructor
@Service
public class ReportService {
    private final MongoTemplate mongoTemplate;

    public RequestReport findBySimulationResponseId(String id) {
        Query query = new Query();
        query.addCriteria(Criteria.where("simulation_response_id").is(id));
        return mongoTemplate.findOne(query, RequestReport.class);
    }

    public ResponseReport save(RequestReport requestReport) {
        ZonedDateTime now = ZonedDateTime.now(ZoneId.of("Asia/Seoul"));
        LocalDateTime createdAt = now.toLocalDateTime();

        ResponseReport responseReport = ResponseReport.builder()
                .userId(requestReport.getUserId())
                .simulationResponseId(requestReport.getSimulationResponseId())
                .createdAt(createdAt)
                .build();

        return mongoTemplate.save(responseReport);
    }
}
