package com.kb.storeMgmt.controller;

import com.kb.storeMgmt.dto.CategoriesDTO;
import com.kb.storeMgmt.service.ChartService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/chart")
@RequiredArgsConstructor
@Slf4j
public class ChartController {

    @Autowired
    private ChartService chartService;

    @GetMapping("/doughnut")
    public List<CategoriesDTO> getAddress(CategoriesDTO categoriesDTO) {
        return chartService.getDoughnut(categoriesDTO);
    }

    @GetMapping("/mixchart")
    public List<CategoriesDTO> getMixAddress(CategoriesDTO categoriesDTO) {
        return chartService.getMixAddress(categoriesDTO);
    }

}
