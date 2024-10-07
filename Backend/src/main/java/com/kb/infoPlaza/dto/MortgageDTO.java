package com.kb.infoPlaza.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class MortgageDTO {
    private Long id; // ID
    private String finPrdtNm; // FIN_PRDT_NM
    private String korCoNm; // KOR_CO_NM
    private Long dclsStrtDay; // DCLS_STRT_DAY
    private Double dclsEndDay; // DCLS_END_DAY
    private String loanInciExpn; // LOAN_INCI_EXPN
    private String erlyRpayFee; // ERLY_RPAY_FEE
    private String dlyRate; // DLY_RATE
    private String loanLmt; // LOAN_LMT
    private String rpayTypeNm; // RPAY_TYPE_NM
    private String lendRateTypeNm; // LEND_RATE_TYPE_NM
    private Double lendRateMin; // LEND_RATE_MIN
    private Double lendRateMax; // LEND_RATE_MAX
    private Double lendRateAvg; // LEND_RATE_AVG
    private String img; // IMG
}
