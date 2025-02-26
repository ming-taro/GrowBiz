package com.kb.simulation.dto.answer;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Field;

import java.util.ArrayList;
import java.util.List;

@Data
public class Response {
    @Id
    private String id;
    @Field("user_id")
    private String userId;
    private List<AnswerItem> answers;

    public Response() {
        this.answers = new ArrayList<>();
    }
}