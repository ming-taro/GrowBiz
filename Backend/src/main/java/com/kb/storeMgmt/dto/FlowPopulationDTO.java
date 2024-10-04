package com.kb.storeMgmt.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class FlowPopulationDTO {
    private String stdrYyquCd;
    private String adstrdCdNm;
    private Integer totFlpopCo;
    private Integer mlFlpopCo;
    private Integer fmlFlpopCo;
}
