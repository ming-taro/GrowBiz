package com.kb.simulation.controller;

import com.kb.simulation.dto.report.RequestReport;
import com.kb.simulation.dto.report.ResponseReport;
import com.kb.simulation.service.ReportService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

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

    @GetMapping("")
    public ResponseEntity<RequestReport> findReport(@RequestParam("simulationResponseId") String id) {
        RequestReport requestReport = reportService.findBySimulationResponseId(id);

        if (requestReport == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(requestReport);
    }
}
