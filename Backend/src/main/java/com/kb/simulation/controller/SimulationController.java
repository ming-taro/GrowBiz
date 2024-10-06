package com.kb.simulation.controller;

import com.kb.simulation.dto.question.LocationQuestion;
import com.kb.simulation.dto.question.Question;
import com.kb.simulation.dto.question.StoreQuestion;
import com.kb.simulation.service.SimulationService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RequiredArgsConstructor
@RestController
@RequestMapping("/api/simulation")
public class SimulationController {
    private final SimulationService service;

    @GetMapping("/question/location")
    public ResponseEntity<LocationQuestion> findLocationQuestion() {
        LocationQuestion question = service.findLocationQuestion();
        if (question == null) {
            return ResponseEntity.noContent().build(); // 데이터가 없을 경우 204 No Content 반환
        }
        return ResponseEntity.ok(question); // 200 OK와 함께 리스트 반환
    }

    @GetMapping("/question/store")
    public ResponseEntity<List<StoreQuestion>> findStoreQuestions() {
        List<StoreQuestion> storeQuestions = service.findStoreQuestions();
        if (storeQuestions.isEmpty()) {
            return ResponseEntity.noContent().build(); // 데이터가 없을 경우 204 No Content 반환
        }
        return ResponseEntity.ok(storeQuestions); // 200 OK와 함께 리스트 반환
    }
}
