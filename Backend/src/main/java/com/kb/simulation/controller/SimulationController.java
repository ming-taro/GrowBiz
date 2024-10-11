package com.kb.simulation.controller;

import com.kb.simulation.dto.question.Question;
import com.kb.simulation.service.SimulationService;
import lombok.RequiredArgsConstructor;
import org.bson.Document;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequiredArgsConstructor
@RestController
@RequestMapping("/api/simulation")
public class SimulationController {
    private final SimulationService service;
    private final SimulationService simulationService;

    @GetMapping("/question/{id}")
    public ResponseEntity<Question> findQuestionById(@PathVariable int id) {
        Question question = service.findQuestionById(id);
        if (question == null) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.ok(question);
    }

    @GetMapping("/question")
    public ResponseEntity<List<Question>> findQuestions() {
        List<Question> storeQuestions = service.findQuestions();
        if (storeQuestions.isEmpty()) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.ok(storeQuestions);
    }

    @PostMapping("/answer")
    public ResponseEntity<Document> postAnswer(@RequestBody String answer) {
        Document savedData = simulationService.saveAnswer(answer);

        Document responseData = new Document("answer", savedData.get("answer"))
                .append("id", savedData.getObjectId("_id").toString());

        if (savedData == null) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.ok(responseData);
    }
}
