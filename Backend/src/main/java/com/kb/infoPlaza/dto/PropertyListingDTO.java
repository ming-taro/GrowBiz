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
}