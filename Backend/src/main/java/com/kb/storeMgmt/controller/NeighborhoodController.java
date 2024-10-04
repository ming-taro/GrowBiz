package com.kb.storeMgmt.controller;

import com.kb.storeMgmt.dto.NeighborhoodDTO;
import com.kb.storeMgmt.service.NeighborhoodService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/kmap")
@RequiredArgsConstructor
@Slf4j
public class NeighborhoodController {

    @Autowired
    private NeighborhoodService neighborhoodService;


    @GetMapping("/member/{id}")
    public NeighborhoodDTO getAddress(NeighborhoodDTO neighborhoodDTO) {
        return neighborhoodService.getAddressById(neighborhoodDTO);
    }

    @GetMapping("/nearby/{address}")
    public Map<String, Object> getNearbyInfo(@PathVariable String address) {
        return neighborhoodService.getNearbyInfo(address);
    }
}
