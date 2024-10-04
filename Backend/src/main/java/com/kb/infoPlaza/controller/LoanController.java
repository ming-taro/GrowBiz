package com.kb.infoPlaza.controller;

import com.kb.infoPlaza.dto.*;
import com.kb.infoPlaza.service.BusinessItemService;
import com.kb.infoPlaza.service.LoanService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/infoPlaza/loan")
@RequiredArgsConstructor
@Slf4j
public class LoanController {
    private final LoanService service;

    @GetMapping("/getBest4")
    public ResponseEntity<List<GovernmentFundDTO>> getBest4List() {
        return ResponseEntity.ok(service.getBest4List() );
    }

    @GetMapping("/getFilteredList")
    public ResponseEntity<List<GovernmentFundDTO>> getFilteredList(GovernmentFilterDTO governmentFilter) {
        return ResponseEntity.ok(service.getFilteredList(governmentFilter));
    }

    @GetMapping("/getDetailItem")
    public ResponseEntity<GovernmentFundDTO> getDetailItem(String productName) {
        return ResponseEntity.ok(service.getDetailItem(productName));
    }
}
