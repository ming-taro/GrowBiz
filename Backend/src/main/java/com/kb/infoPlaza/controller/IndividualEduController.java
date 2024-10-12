package com.kb.infoPlaza.controller;


import com.kb.infoPlaza.dto.IndividualEduDTO;
import com.kb.infoPlaza.dto.IndividualEduParam;
import com.kb.infoPlaza.service.IndividualEduService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/infoPlaza/education")
@RequiredArgsConstructor
@Slf4j
public class IndividualEduController {
//    http://localhost:8080/api/infoPlaza/education/list
    private final IndividualEduService individualEduService;

    // 모든 교육 정보를 조회하는 API 엔드포인트
    @GetMapping("/list")
    public ResponseEntity<List<IndividualEduDTO>> getAllIndividualEdu() {
        List<IndividualEduDTO> list = individualEduService.selectAllIndividualEdu();

        return ResponseEntity.ok(list);  // 200 OK 응답으로 리스트 반환
    }

    // 특정 vno로 교육 정보를 조회하는 API 엔드포인트
    @GetMapping("/video/{vno}")
    public ResponseEntity<IndividualEduDTO> getIndividualEduById(@PathVariable int vno) {
        IndividualEduDTO dto = individualEduService.selectIndividualEduById(vno);
        return ResponseEntity.ok(dto);  // 200 OK 응답으로 개별 데이터 반환
    }
    // 검색 엔드포인트: 옵션으로 검색
    @GetMapping("/search")
    public ResponseEntity<List<IndividualEduDTO>> searchIndividualEdu(IndividualEduParam individualEduParam) {
        List<IndividualEduDTO> result;
        if (individualEduParam.getSearchType() != null){
            result = individualEduService.searchIndividualEdu(individualEduParam);
        }
        else {
            result = individualEduService.searchIndividualEduByOption(individualEduParam);
        }
        return ResponseEntity.ok(result);
    }
    @GetMapping("/search/keyword")
    public ResponseEntity<List<IndividualEduDTO>> searchIndividualEduByKeyword(IndividualEduParam individualEduParam) {
        List<IndividualEduDTO> result = individualEduService.searchIndividualEduByKeyword(individualEduParam);
        return ResponseEntity.ok(result);
    }
}