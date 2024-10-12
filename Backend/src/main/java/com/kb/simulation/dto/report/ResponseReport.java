package com.kb.simulation.dto.report;

import lombok.*;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

import javax.swing.*;
import java.time.LocalDateTime;
import java.util.List;

@ToString
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Document(collection = "report")
public class ResponseReport {
    @Id
    private String id;
    @Field("user_id")
    private String userId;
    @Field("simulation_response_id")
    private String simulationResponseId;
    @Field("created_at")
    private LocalDateTime createdAt;
//    @Field("plno_list")
//    private List<Integer> plnoList;
//    @Field("brand_name")
//    private String brandName;
//    @Field("franchise_score")
//    private double franchiseScore;
//    @Field("average_brand_score")
//    private double averageBrandScore;
//    @Field("industry_density_average")
//    private double industryDensityAverage;
//    @Field("recommended_brand_density")
//    private double recommendedBrandDensity;
//    @Field("industry_initial_cost")
//    private long industryInitialCost;
//    @Field("recommended_brand_initial_cost")
//    private long recommendedBrandInitialCost;
//    @Field("industry_total_interior_cost")
//    private long industryTotalInteriorCost;
//    @Field("recommended_brand_total_interior_cost")
//    private long;
//    @Field("industry_opening_rate_average")
//    private double;
//    @Field("industry_closing_rate_average")
//    private double;
//    @Field("recommended_brand_opening_rate_average")
//    private double;
//    @Field("recommended_brand_closing_rate_average")
//    private double;
//    @Field("top_3_nearby_stations")
//    private List<>;
//    industry_closing_rate_average
//1.73
//    recommended_brand_opening_rate_average
//4.23
//    recommended_brand_closing_rate_average
//1.13
//
//    top_3_nearby_stations
//    Array (3)
//    recommended_brand_average_sales_per_area
//1800
//    recommended_brand_average_sales
//120000
//    industry_average_sales_per_area
//1500
//    industry_average_sales
//100000
//
//    contract_period
}
