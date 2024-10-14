package com.kb.storeMgmt.controller;

import com.kb.storeMgmt.dto.CategoriesDTO;
import com.kb.storeMgmt.dto.SalesInfoDTO;
import com.kb.storeMgmt.service.ChartService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/chart")
@RequiredArgsConstructor
@Slf4j
public class ChartController {

    @Autowired
    private ChartService chartService;

    @GetMapping("/doughnut/{svcIndutyCdNm}")
    public List<CategoriesDTO> getAddress(CategoriesDTO categoriesDTO) {
        return chartService.getDoughnut(categoriesDTO);
    }

    @GetMapping("/mixchart/{svcIndutyCdNm}")
    public List<CategoriesDTO> getMixAddress(CategoriesDTO categoriesDTO) {

        return chartService.getMixAddress(categoriesDTO);
    }

    @GetMapping("/mcfirst/{svcIndutyCdNm}")
    public List<SalesInfoDTO> getmcfirst(@RequestParam String dongname, SalesInfoDTO salesInfoDTO) {
        // 쉼표로 구분된 문자열을 리스트로 변환하면서 각 동 이름의 공백을 제거
        List<String> dongnameList = Arrays.stream(dongname.split(","))
                .map(String::trim)  // 각 항목에 대해 trim() 적용
                .collect(Collectors.toList());

        salesInfoDTO.setDongname(dongnameList);
        return chartService.getmcfirst(salesInfoDTO);
    }

    @GetMapping("/mcsecend/{svcIndutyCdNm}")
    public List<CategoriesDTO> getmcsecend(CategoriesDTO categoriesDTO) {
        return chartService.getmcsecend(categoriesDTO);
    }

    @GetMapping("/sum/{svcIndutyCdNm}")
    public CategoriesDTO getsum(CategoriesDTO categoriesDTO) {
        return chartService.getsum(categoriesDTO);
    }
}
