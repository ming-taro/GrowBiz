package com.kb.infoPlaza.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class PersonalCreditLoanDTO {
    private Long id; // ID
    private String finPrdtNm; // FIN_PRDT_NM
    private String korCoNm; // KOR_CO_NM
    private Long dclsStrtDay; // DCLS_STRT_DAY
    private Double dclsEndDay; // DCLS_END_DAY
    private String crdtPrdtTypeNm; // CRDT_PRDT_TYPE_NM
    private String crdtLendRateTypeNm; // CRDT_LEND_RATE_TYPE_NM
    private Double crdtGradAvg; // CRDT_GRAD_AVG
    private Double crdtGrad1; // CRDT_GRAD_1
    private Double crdtGrad4; // CRDT_GRAD_4
    private Double crdtGrad5; // CRDT_GRAD_5
    private Double crdtGrad6; // CRDT_GRAD_6
    private Double crdtGrad10; // CRDT_GRAD_10
    private Double crdtGrad11; // CRDT_GRAD_11
    private Double crdtGrad12; // CRDT_GRAD_12
    private Double crdtGrad13; // CRDT_GRAD_13
    private String img; // IMG
}
