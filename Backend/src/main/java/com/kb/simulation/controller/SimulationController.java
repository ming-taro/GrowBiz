package com.kb.simulation.controller;

import com.kb.simulation.dto.question.Question;
import com.kb.simulation.service.SimulationService;
import lombok.RequiredArgsConstructor;
import org.bson.Document;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.print.Doc;
import java.util.List;
import java.util.Map;

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

        storeQuestions.sort((o1, o2) -> o1.getInd() - o2.getInd());

        if (storeQuestions.isEmpty()) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.ok(storeQuestions);
    }

    @PostMapping("/answer")
    public ResponseEntity<Document> createResponse(@RequestBody String answer) {
        Document savedData = simulationService.createResponse(answer);

        Document responseData = new Document("answer", savedData.get("answer"))
                .append("id", savedData.getObjectId("_id").toString());

        if (savedData == null) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.ok(responseData);
    }

    @GetMapping("/answer/{id}")
    public ResponseEntity<Document> findResponseById(@PathVariable("id") String id) {
        Document response = simulationService.findResponseById(id);

        if (response == null) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.ok(response);
    }

    @PostMapping("/start")
    public ResponseEntity<String> executeSimulation(@RequestBody Map<String, String> requestBody) {
        String id = requestBody.get("id");
        String reportId = simulationService.executeSimulation(id);

        if (reportId == null) {
            return ResponseEntity.badRequest().build();
        }
        return ResponseEntity.ok(reportId);
    }
}
