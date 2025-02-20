package com.kb.simulation.dto.question;

import lombok.*;

import java.util.List;

@ToString
@AllArgsConstructor
@NoArgsConstructor
@Setter
@Getter
public class Seoul {
    private String district;
    private List<String> neighborhoods;
}
