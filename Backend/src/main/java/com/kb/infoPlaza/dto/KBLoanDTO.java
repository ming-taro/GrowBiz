package com.kb.infoPlaza.dto;

import lombok.Data;

@Data
public class KBLoanDTO {
    private String loanKey;
    private String productName;
    private String lowestInterestRate;
    private String loanEligibility;
    private String loanAmount;
    private String loanDurationAndRepayment;
    private String availableHours;
    private String loanNotice;
}
