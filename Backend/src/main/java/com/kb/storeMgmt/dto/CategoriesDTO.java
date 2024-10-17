package com.kb.storeMgmt.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class CategoriesDTO {
    private int id;
    private String category;
    private String categoryName;
    private java.sql.Date insertDate;
    private long amount;
    private String svcIndutyCdNm;
}
