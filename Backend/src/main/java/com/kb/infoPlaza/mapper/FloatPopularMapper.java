package com.kb.infoPlaza.mapper;

import com.kb.infoPlaza.dto.FloatPopularDTO;
import org.apache.ibatis.annotations.Param;

import java.util.List;

public interface FloatPopularMapper {
    // 특정 동과 기준 분기 정보를 기반으로 인구 수 조회
    List<FloatPopularDTO> selectPopularByDongName(@Param("dongNames") List<String> dongNames, @Param("yearQuarter") String yearQuarter);

}
