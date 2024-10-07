package com.kb.simulation.dto.question;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.util.List;

@ToString
@AllArgsConstructor
@Setter
@Getter
public class Seoul {
    private String district;
    private List<String> neighborhoods;
}
