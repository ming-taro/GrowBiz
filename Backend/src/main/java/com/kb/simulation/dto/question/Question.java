package com.kb.simulation.dto.question;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;

@ToString
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Document(collection = "questions")
public class Question<T> {
    @Id
    private String id;
    private int ind;               // 질문 순서
    private String fullTexts;
    private List<T> choices;
    private String questionType;
}