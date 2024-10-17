package com.kb.infoPlaza.service;

import com.kb.infoPlaza.dto.PropertyListingDTO;
import com.kb.infoPlaza.dto.DistrictCodeDTO;
import com.kb.infoPlaza.mapper.PropertyListingMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Log4j
@Service
@RequiredArgsConstructor
public class PropertyListingService {

    private final PropertyListingMapper mapper;

    // 매물 전체 조회
    public List<PropertyListingDTO> selectAllPropertyListings() {
        List<PropertyListingDTO> listings = mapper.selectAllPropertyListings();
        if (listings == null || listings.isEmpty()) {
            listings = new ArrayList<>();
        }
        return listings;
    }


    // 동 이름으로 매물동 코드 조회
    @Transactional
    public String selectDongCodeByDongName(String dongName) {
        String dongCode = mapper.selectDongCodeByDongName(dongName);
        return Optional.ofNullable(dongCode)
                .orElseThrow(NoSuchElementException::new);
    }

    // 동 코드로 매물 조회
    public List<PropertyListingDTO> selectPropertyListingByDongCode(String dongCode) {
        List<PropertyListingDTO> listings = mapper.selectPropertyListingByDongCode(dongCode);
        if (listings == null || listings.isEmpty()) {
            listings = new ArrayList<>();
        }
        return listings;
    }

    public PropertyListingDTO findPropertyById(String id) {
        return mapper.findById(id);
    }
}
