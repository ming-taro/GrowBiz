package com.kb.infoPlaza.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class BusinessClosureDTO {
    private Long stdrYyquCd;              // STDR_YYQU_CD
    private String trdarSeCd;             // TRDAR_SE_CD
    private String trdarCdNm;             // TRDAR_CD_NM
    private String trdarCd;                // TRDAR_CD
    private String trdarSeCdNm;           // TRDAR_SE_CD_NM
    private String svcIndutyCd;           // SVC_INDUTY_CD
    private String svcIndutyCdNm;         // SVC_INDUTY_CD_NM
    private Long storCo;                   // STOR_CO
    private Long similrIndutyStorCo;      // SIMILR_INDUTY_STOR_CO
    private Double opbizRt;                // OPBIZ_RT
    private Long opbizStorCo;              // OPBIZ_STOR_CO
    private Double clsbizRt;               // CLSBIZ_RT
    private Long clsbizStorCo;             // CLSBIZ_STOR_CO
    private Long frcStorCo;
}
