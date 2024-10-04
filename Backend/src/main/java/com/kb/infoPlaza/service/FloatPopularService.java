package com.kb.infoPlaza.service;

import com.kb.infoPlaza.dto.FloatPopularDTO;
import com.kb.infoPlaza.dto.FloatPopularReqDTO;
import com.kb.infoPlaza.mapper.FloatPopularMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Log4j
@Service
@RequiredArgsConstructor
public class FloatPopularService {

    private final FloatPopularMapper floatPopulationMapper;

    // 특정 동에 대한 인구 수 조회
    public List<FloatPopularDTO> getPopularData(FloatPopularReqDTO request) {
        return floatPopulationMapper.selectPopularByDongName(request.getDongNames(), request.getYearQuarter());
    }
}
