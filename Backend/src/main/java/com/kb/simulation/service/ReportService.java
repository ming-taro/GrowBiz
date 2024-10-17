package com.kb.simulation.service;

import com.kb.simulation.dto.ReportInfo;
import com.kb.simulation.dto.report.RequestReport;
import com.kb.simulation.dto.report.ResponseReport;
import lombok.RequiredArgsConstructor;
import org.bson.Document;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.List;

@RequiredArgsConstructor
@Service
public class ReportService {
    private final MongoTemplate mongoTemplate;
    private final String REPORT_COLLECTION = "report";

    public Document findById(String id) {
        Query query = new Query();
        query.addCriteria(Criteria.where("_id").is(id));
        return mongoTemplate.findOne(query, Document.class, REPORT_COLLECTION);
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

    public String findReportByResponseId(String id) {
        Query query = new Query();
        query.addCriteria(Criteria.where("simulation_response_id").is(id));
        Document result =  mongoTemplate.findOne(query, Document.class, REPORT_COLLECTION);
        System.out.println(">>id:" + id);
        System.out.println(result);
        if (result != null) {
            Object reportId = result.get("_id");
            System.out.println("reportId:" + reportId);
            return reportId.toString();
        }

        return "";
    }

    public List<ReportInfo> findAllReports(String userId) {
        Query query = new Query();
        query.addCriteria(Criteria.where("user_id").is(userId));

        return mongoTemplate.find(query, ReportInfo.class, REPORT_COLLECTION);
    }
}