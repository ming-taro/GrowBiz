package com.kb.storeMgmt.controller;

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

    @GetMapping("/address/{address}")
    public String getDongName(@PathVariable String address) {
        return neighborhoodService.getDongName(address);
    }

    @GetMapping("/{dongName}")
    public Map<String, Object> getNearbyInfo(@PathVariable String dongName) {
        return neighborhoodService.getNearbyInfo(dongName);
    }
}
