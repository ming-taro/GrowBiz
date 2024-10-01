package com.kb.infoPlaza.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class DistrictCodeDTO {
    private int dsno;
    private String guName;
    private String guCode;
    private String dongName;
    private String dongCode;
}
