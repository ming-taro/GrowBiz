package com.kb.simulation.controller;

import com.kb.simulation.dto.ReportInfo;
import com.kb.simulation.dto.report.RequestReport;
import com.kb.simulation.dto.report.ResponseReport;
import com.kb.simulation.service.ReportService;
import lombok.RequiredArgsConstructor;
import org.bson.Document;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.List;
import java.util.Locale;

@RequiredArgsConstructor
@RestController
@RequestMapping("/api/report")
public class ReportController {
    private final ReportService reportService;

    @PostMapping("")
    public ResponseEntity<ResponseReport> createReport(@RequestBody RequestReport requestReport) {
        ResponseReport savedReport = reportService.save(requestReport);
        if (savedReport == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(savedReport);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Document> findReportById(@PathVariable("id") String id) {
        Document report = reportService.findById(id);

        if (report == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(report);
    }

    @GetMapping("/response-id/{id}")
    public ResponseEntity<String> findReportByResponseId(@PathVariable("id") String id) {
        String result = reportService.findReportByResponseId(id);

        if (result == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(result);
    }

    @GetMapping("/user/{userId}")
    public ResponseEntity<List<ReportInfo>> findAllReports(@PathVariable String userId) {
        List<ReportInfo> reports = reportService.findAllReports(userId);

        // 정렬된 결과 출력
        System.out.println("크기:" + reports.size());
        reports.forEach(System.out::println);

        return ResponseEntity.ok(reports);
    }
}
