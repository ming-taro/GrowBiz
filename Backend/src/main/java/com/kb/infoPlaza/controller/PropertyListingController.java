package com.kb.infoPlaza.controller;

import com.kb.infoPlaza.dto.PropertyListingDTO;
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

    private final PropertyListingService service;

    // 모든 매물 조회
    @GetMapping("")
    public ResponseEntity<List<PropertyListingDTO>> getAllProperties() {
        System.out.println("!!!!!!!!!!!!!!!");
        List<PropertyListingDTO> propertyListings = service.selectAllPropertyListings();
        return ResponseEntity.ok(propertyListings);
    }

    // 특정 매물 조회
    @GetMapping("/{plno}")
    public ResponseEntity<PropertyListingDTO> getPropertyById(@PathVariable int plno) {
        PropertyListingDTO propertyListing = service.selectPropertyListingById(plno);
        return ResponseEntity.ok(propertyListing);
    }

}
