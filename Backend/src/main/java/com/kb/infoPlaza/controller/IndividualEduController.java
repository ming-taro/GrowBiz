package com.kb.infoPlaza.controller;


import com.kb.infoPlaza.dto.IndividualEduDTO;
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



    // 특정 videoId로 교육 정보를 조회하는 API 엔드포인트
    @GetMapping("/{videoId}")
    public ResponseEntity<IndividualEduDTO> getIndividualEduById(@PathVariable String videoId) {
        IndividualEduDTO dto = individualEduService.selectIndividualEduById(videoId);
        return ResponseEntity.ok(dto);  // 200 OK 응답으로 개별 데이터 반환
    }
}