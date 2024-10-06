package com.kb.simulation.dto.question;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;

@ToString(callSuper = true)
@Getter
@Setter
@Document(collection = "questions")
public class StoreQuestion extends Question{
    private List<Choice> choices;
}
