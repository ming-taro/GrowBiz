package com.kb.infoPlaza.service;

import com.kb.infoPlaza.dto.DistrictCodeDTO;
import com.kb.infoPlaza.mapper.DistrictCodeMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.*;

@Log4j
@Service
@RequiredArgsConstructor
public class DistrictCodeService {

    private final DistrictCodeMapper mapper;

    // 중복 제거한 모든 구 이름 가져오기
    public List<DistrictCodeDTO> getDistinctGuNames() {
        return mapper.selectDistinctGuNames();
    }
    // 중복 제거한 모든 동 이름 가져오기
    public List<DistrictCodeDTO> getDistinctDongNames(String guName) {
        return mapper.selectDistinctDongNames(guName);
    }
}
