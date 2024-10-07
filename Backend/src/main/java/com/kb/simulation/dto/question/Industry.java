package com.kb.simulation.dto.question;

import lombok.*;

import java.util.List;

@ToString
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class Industry {
    private String category;
    private List<Choice> subcategories;
}
