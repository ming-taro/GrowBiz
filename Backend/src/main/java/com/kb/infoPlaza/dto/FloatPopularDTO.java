package com.kb.infoPlaza.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class FloatPopularDTO {
    private String stdrYyquCd; // STDR_YYQU_CD
    private String adstrdCdNm; // ADSTRD_CD_NM
    private Integer totFlpopCo; // TOT_FLPOP_CO
    private Integer mlFlpopCo;   // ML_FLPOP_CO
    private Integer fmlFlpopCo;  // FML_FLPOP_CO

}
