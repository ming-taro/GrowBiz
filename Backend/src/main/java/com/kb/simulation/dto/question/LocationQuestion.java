package com.kb.simulation.dto.question;

import lombok.*;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;

@ToString(callSuper = true)
@Getter
@Setter
@Document(collection = "questions")
public class LocationQuestion extends Question {
    private List<Seoul> choices;
}
