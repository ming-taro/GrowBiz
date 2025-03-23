package com.kb.simulation.dto.question;

public enum QuestionType {
    DISTRICT("district"),
    INDUSTRY("industry"),
    BASIC("basic");

    private final String type;

    QuestionType(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public static QuestionType fromString(String type) {
        for (QuestionType questionType : values()) {
            if (questionType.getType().equals(type)) {
                return questionType;
            }
        }
        return BASIC;
    }
}