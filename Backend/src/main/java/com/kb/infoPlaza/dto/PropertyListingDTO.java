package com.kb.infoPlaza.dto;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

import java.util.Date;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PropertyListingDTO {
    private int plno;
    private String ldongCd;
    private String atclNo;
    private Date atclRegDttm;
    private String ctgryCd1;
    private String ctgryCd1Nm;
    private String ctgryCd2;
    private String ctgryCd2Nm;
    private String atclSfeCn;
    private String dealKindCdNm;
    private long bscTnthWuntAmt;
    private long addTnthWuntAmt;
    private double area1;
    private double area2;
    private String imageData;
    private double laCrd;
    private double loCrd;
    private String mdiatBzestNm;
    // 새로 추가된 필드
    private String addr;
    private String drcCd; //방향
    private String mmMcost; //관리비
    private String heatingInfo; //난방정보
    private String bldUsageCd; //건물용도
    private String parkCcnt;   //주차가능대수
    private String mdiatBzestRepTelno; //부동산번호
    private String mdiatBzestRepMoblno; //대표자번호
    private String dtlDesc; //매물설명
}