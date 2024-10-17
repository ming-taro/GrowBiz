package com.kb.infoPlaza.controller;

import com.kb.infoPlaza.dto.DistrictCodeDTO;
import com.kb.infoPlaza.dto.FloatPopularDTO;
import com.kb.infoPlaza.dto.FloatPopularReqDTO;
import com.kb.infoPlaza.dto.PropertyListingDTO;
import com.kb.infoPlaza.service.DistrictCodeService;
import com.kb.infoPlaza.service.FloatPopularService;
import com.kb.infoPlaza.service.PropertyListingService;
import io.swagger.annotations.Api;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/property")
@RequiredArgsConstructor
@Slf4j
@Api(value = "PropertyListingController", tags = "매물 정보")
public class PropertyListingController {

    private final PropertyListingService propertyService;
    private final DistrictCodeService districtService;
    private final FloatPopularService floatPopularService;

    // 모든 매물 조회
    @GetMapping("/list-all")
    public ResponseEntity<List<PropertyListingDTO>> getAllProperties() {
        List<PropertyListingDTO> propertyListings = propertyService.selectAllPropertyListings();
        return ResponseEntity.ok(propertyListings);
    }

    // 중복 제거한 모든 구 이름을 반환하는 API
    @GetMapping("/gu-names")
    public ResponseEntity<List<DistrictCodeDTO>> getDistinctGuNames() {
        List<DistrictCodeDTO> guNames = districtService.getDistinctGuNames();
        return ResponseEntity.ok(guNames);
    }

    // 구 이름에 맞는 동 이름 조회
    @GetMapping("/dong-names")
    public ResponseEntity<List<DistrictCodeDTO>> getDongNamesByGuName(@RequestParam String guName) {
        List<DistrictCodeDTO> dongNames = districtService.getDistinctDongNames(guName);
        return ResponseEntity.ok(dongNames);
    }


    // 동 이름으로 매물 동 코드 조회
    @GetMapping("/dong-code")
    public ResponseEntity<String> getDongCodeByDongName(@RequestParam String dongName) {
        try {
            String dongCode = propertyService.selectDongCodeByDongName(dongName);

            // 동 코드가 있을 경우
            if (dongCode != null) {
                return ResponseEntity.ok(dongCode);
            } else {
                // 동 코드가 없을 경우 빈 문자열로 응답
                return ResponseEntity.ok("");
            }
        } catch (Exception e) {
            // 예외가 발생할 경우 빈 문자열로 응답
            return ResponseEntity.ok(""); // 오류가 발생했을 때도 빈 문자열로 응답
        }
    }

    @GetMapping("/list")
    public ResponseEntity<List<PropertyListingDTO>> selectPropertyListingByDongCode(@RequestParam String dongCode) {
        List<PropertyListingDTO> propertyListings = propertyService.selectPropertyListingByDongCode(dongCode);
        return ResponseEntity.ok(propertyListings);
    }

    @PostMapping("/float-popular")
    public ResponseEntity<List<FloatPopularDTO>> getPopularByDongName(@RequestBody FloatPopularReqDTO request) {
        List<FloatPopularDTO> populationData = floatPopularService.getPopularData(request);
        return ResponseEntity.ok(populationData);
    }

    @GetMapping("/{id}")
    public ResponseEntity<PropertyListingDTO> findPropertyById(@PathVariable String id) {
        PropertyListingDTO property = propertyService.findPropertyById(id);
        if (property == null) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.ok(property);
    }
}
