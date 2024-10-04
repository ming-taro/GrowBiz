package com.kb.infoPlaza.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class GovernmentFundDTO {
    private String loanProductName;      // loan_product_name
    private String applicationPeriod;     // application_period
    private String category;               // category
    private String baseInterestRate;      // base_interest_rate
    private String additionalInterestRate; // additional_interest_rate
    private String totalInterestRate;      // total_interest_rate
    private String description;            // description
}