package com.kb.storeMgmt.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SalesInfoDTO {
    // 기준 연도-분기 코드 (varchar(10))
    private String stdrYyquCd;

    // 행정동 코드 이름 (varchar(100))
    private String adstrdCdNm;

    // 서비스 산업 코드 이름 (varchar(100))
    private String svcIndutyCdNm;

    // 이번 달 판매 금액 (bigint)
    private Long thsmonSelngAmt;

    // 주중 판매 금액 (bigint)
    private Long mdwkSelngAmt;

    private List<String> dongname;

    // Getter, Setter
    public List<String> getDongname() {
        return dongname;
    }

    public void setDongname(List<String> dongname) {
        this.dongname = dongname;
    }
}
