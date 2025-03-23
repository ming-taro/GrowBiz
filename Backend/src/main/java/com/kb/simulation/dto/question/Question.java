package com.kb.simulation.dto.question;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
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
    @JsonProperty("_id")
    private String id;
    private int ind;               // 질문 순서
    private String fullTexts;
    private List<T> choices;
    private String questionType;
}