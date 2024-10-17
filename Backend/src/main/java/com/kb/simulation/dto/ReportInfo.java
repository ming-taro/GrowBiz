package com.kb.simulation.dto;

import lombok.*;
import org.springframework.data.mongodb.core.mapping.Field;

@ToString
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class ReportInfo {
    @Field("_id")
    private String reportId;
    @Field("created_at")
    private String createdAt;
    @Field("brand_name")
    private String brandName;
    @Field("simulation_response_id")
    private String simulationResponseId;
}