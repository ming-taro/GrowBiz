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
    private String stdrTrdarSvc;
    private Long stdrYyquCd;
    private String trdarSeCdNm;
    private String adstrdCdNm;
    private String signguCdNm;
    private String svcIndutyCdNm;
    private Long opbizRt;
    private Long clsbizRt;
    private Long storCo;
    private Long similrIndutyStorCo;
    private String img;
}
