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
    private Long stdrYyquCd; // STDR_YYQU_CD
    private String trdarCdNm; // TRDAR_CD_NM
    private String svcIndutyCdNm; // SVC_INDUTY_CD_NM
    private Long storCo; // STOR_CO
    private Long similrIndutyStorCo; // SIMILR_INDUTY_STOR_CO
    private Long opbizRt; // OPBIZ_RT
    private Long opbizStorCo; // OPBIZ_STOR_CO
    private Long clsbizRt; // CLSBIZ_RT
    private Long clsbizStorCo; // CLSBIZ_STOR_CO
    private String signGuCdNm; // SIGNGU_CD_NM
    private String adstrdCdNm; // ADSTRD_CD_NM
    private Long ranking; // RANKING
}
