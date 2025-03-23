package com.kb.simulation.dto.test;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.concurrent.Future;

@AllArgsConstructor
@Data
public class ReportTest {
    private String reportId;
    private long startTime;
    private long endTime;
    private long executionTime;

    @Override
    public String toString() {
        return "ReportTest{" +
                "reportId='" + reportId + '\'' +
                ", startTime=" + startTime +
                ", endTime=" + endTime +
                ", executionTime=" + executionTime +
                '}';
    }
}
