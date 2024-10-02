package com.kb.infoPlaza.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class BusinessItemDTO {
    private String stdrTrdarSvc;
    private Long stdrYyquCd;
    private String trdarSeCdNm;
    private String svcIndutyCdNm;
    private Long thsmonSelngAmt;
    private Long mdwkSelngAmt;
    private Long wkendSelngAmt;
    private Long mlSelngAmt;
    private Long fmlSelngAmt;
    private Long agrde10SelngAmt;
    private Long agrde20SelngAmt;
    private Long agrde30SelngAmt;
    private Long agrde40SelngAmt;
    private Long agrde50SelngAmt;
    private Long agrde60AboveSelngAmt;
    private String signguCdNm;
    private String adstrdCdNm;
    private String img;
}
