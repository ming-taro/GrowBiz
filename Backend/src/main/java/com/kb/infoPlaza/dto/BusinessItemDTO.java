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
    private String stdrTrdarSvc;      // STDR_TRDAR_SVC
    private Long stdrYyquCd;          // STDR_YYQU_CD
    private String trdarSeCdNm;       // TRDAR_SE_CD_NM
    private String svcIndutyCdNm;     // SVC_INDUTY_CD_NM
    private Long thsmonSelngAmt;      // THSMON_SELNG_AMT
    private Long mdwkSelngAmt;        // MDWK_SELNG_AMT
    private Long wkendSelngAmt;       // WKEND_SELNG_AMT
    private Long mlSelngAmt;          // ML_SELNG_AMT
    private Long fmlSelngAmt;         // FML_SELNG_AMT
    private Long agrde10SelngAmt;     // AGRDE_10_SELNG_AMT
    private Long agrde20SelngAmt;     // AGRDE_20_SELNG_AMT
    private Long agrde30SelngAmt;     // AGRDE_30_SELNG_AMT
    private Long agrde40SelngAmt;     // AGRDE_40_SELNG_AMT
    private Long agrde50SelngAmt;     // AGRDE_50_SELNG_AMT
    private Long agrde60AboveSelngAmt; // AGRDE_60_ABOVE_SELNG_AMT
    private String signguCdNm;        // SIGNGU_CD_NM
    private String adstrdCdNm;        // ADSTRD_CD_NM
    private String img;                // img
    private Integer rank;             // RANK
    private String rankChange;        // RANK_CHANGE
    private Long opbizStorCo;         // OPBIZ_STOR_CO
}
