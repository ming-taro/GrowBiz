package com.kb.simulation.dto.report;

import lombok.*;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

import java.time.LocalDateTime;

@ToString
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class RequestReport {
    @Field("user_id")
    private String userId;
    @Field("simulation_response_id")
    private String simulationResponseId;
}