package com.kb.infoPlaza.controller;

import com.kb.infoPlaza.dto.Best3DTO;
import com.kb.infoPlaza.dto.BusinessClosureDTO;
import com.kb.infoPlaza.dto.BusinessItemDTO;
import com.kb.infoPlaza.service.BusinessItemService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/infoPlaza/businessItem")
@RequiredArgsConstructor
@Slf4j
public class BusinessItemController {
    private final BusinessItemService service;

    @GetMapping("/getBest3")
    public ResponseEntity<List<BusinessItemDTO>> getBest3(Best3DTO best3) {
        return ResponseEntity.ok(service.getBest3List(best3));
    }

    @GetMapping("/getTotal5")
    public ResponseEntity<List<BusinessItemDTO>> getTotal5() {
        return ResponseEntity.ok(service.getTotal5());
    }

    @GetMapping("/getTotal")
    public ResponseEntity<List<BusinessItemDTO>> getTotal() {
        return ResponseEntity.ok(service.getTotal());
    }

    @GetMapping("/getPortion5")
    public ResponseEntity<List<BusinessItemDTO>> getPortion5(@RequestParam(required = false) String location) {
        return ResponseEntity.ok(service.getPortion5(location));
    }

    @GetMapping("/getPortion")
    public ResponseEntity<List<BusinessItemDTO>> getPortion(@RequestParam(required = false) String location) {
        return ResponseEntity.ok(service.getPortion(location));
    }

    @GetMapping("/getRate5")
    public ResponseEntity<List<BusinessClosureDTO>> getRate5() {
        return ResponseEntity.ok(service.getRate5());
    }

    @GetMapping("/getRate")
    public ResponseEntity<List<BusinessClosureDTO>> getRate() {
        return ResponseEntity.ok(service.getRate());
    }
}
