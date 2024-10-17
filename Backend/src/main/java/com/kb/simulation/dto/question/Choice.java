package com.kb.simulation.dto.question;

import lombok.*;

@ToString
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class Choice {
    private String text;
    private String value;
}
