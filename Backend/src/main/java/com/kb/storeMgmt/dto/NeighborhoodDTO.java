package com.kb.storeMgmt.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class NeighborhoodDTO {
    private String address;
    private String id;
    private String addressname;
    private String dongname;
    private String svcIndutyCdNm;

    private int rent; // 월세
    private int utilityExpenses; // 공과금
    private int laborCost; // 인건비
    private int otherExpenses; // 기타 비용
    private String detailAddress; // 상세주소
    private String imageUrl; // 가게 이미지 URL
}
