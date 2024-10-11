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
}
