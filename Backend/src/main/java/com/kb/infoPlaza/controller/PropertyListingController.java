package com.kb.infoPlaza.controller;

import com.kb.infoPlaza.dto.DistrictCodeDTO;
import com.kb.infoPlaza.dto.PropertyListingDTO;
import com.kb.infoPlaza.service.DistrictCodeService;
import com.kb.infoPlaza.service.PropertyListingService;
import io.swagger.annotations.Api;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/property")
@RequiredArgsConstructor
@Slf4j
@Api(value = "PropertyListingController", tags = "매물 정보")
public class PropertyListingController {

    private final PropertyListingService propertyService;
    private final DistrictCodeService districtService;

    // 모든 매물 조회
    @GetMapping("")
    public ResponseEntity<List<PropertyListingDTO>> getAllProperties() {
        List<PropertyListingDTO> propertyListings = propertyService.selectAllPropertyListings();
        return ResponseEntity.ok(propertyListings);
    }

    // 특정 매물 조회
    @GetMapping("/{plno}")
    public ResponseEntity<PropertyListingDTO> getPropertyById(@PathVariable int plno) {
        PropertyListingDTO propertyListing = propertyService.selectPropertyListingById(plno);
        return ResponseEntity.ok(propertyListing);
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

    // 동 이름으로 위도, 경도 조회
    @GetMapping("/location")
    public ResponseEntity<DistrictCodeDTO> getLocation(@RequestParam String dongName) {
        DistrictCodeDTO location = districtService.getLocationByDongName(dongName);
        if (location != null) {
            return ResponseEntity.ok(location);
        } else {
            return ResponseEntity.notFound().build(); // Not found
        }
    }

}
