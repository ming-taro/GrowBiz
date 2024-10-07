package com.kb.community.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CategoryDTO {
    private Long id;        // 카테고리 ID
    private String name;    // 카테고리 이름
    private String link;    // 카테고리 링크
}
