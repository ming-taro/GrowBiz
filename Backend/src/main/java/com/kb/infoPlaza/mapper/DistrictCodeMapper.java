package com.kb.infoPlaza.mapper;

import com.kb.infoPlaza.dto.DistrictCodeDTO;
import java.util.List;
import java.util.Map;

public interface DistrictCodeMapper {
    //모든 구 이름 조회
    List<DistrictCodeDTO> selectDistinctGuNames();

    //모든 동 이름 조회
    List<DistrictCodeDTO> selectDistinctDongNames(String guName);

    // 동 이름으로 위도와 경도 가져오기
    DistrictCodeDTO selectLocationByDongName(String dongName);
}