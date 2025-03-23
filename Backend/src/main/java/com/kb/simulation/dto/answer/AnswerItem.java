package com.kb.simulation.dto.answer;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class AnswerItem {
    private String district;
    private String neighborhoods;
    private String category;
    private String subcategories;
    private String text;
}
