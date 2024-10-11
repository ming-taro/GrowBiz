package com.kb.storeMgmt.dto;

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
}
