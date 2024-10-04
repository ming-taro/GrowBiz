package com.kb.simulation.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
@AllArgsConstructor
@Builder
public class Question {
    private int ind; // 질문 순서
    private String fullTexts;
    private List<Choice> choices;
}