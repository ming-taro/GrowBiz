package com.kb.storeMgmt.controller;

import com.kb.storeMgmt.dto.FlowPopulationDTO;
import com.kb.storeMgmt.service.ChartService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/chart")
@RequiredArgsConstructor
@Slf4j
public class ChartController {

    @Autowired
    private ChartService chartService;

    @GetMapping("/doughnut/{adstrdCdNm}")
    public FlowPopulationDTO getAddress(FlowPopulationDTO flowPopulationDTO) {
        return chartService.getFlpopCobyDongname(flowPopulationDTO);
    }
}
