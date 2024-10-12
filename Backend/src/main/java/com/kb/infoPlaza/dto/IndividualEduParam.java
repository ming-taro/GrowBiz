package com.kb.infoPlaza.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@NoArgsConstructor
@AllArgsConstructor
@Data
public class IndividualEduParam {
    // html - form의 name과 일치하는 파라메터
    private String searchType;
    private String searchKeyword;
//    private int amount;
    private List<String> Option;
//
//    // 페이징 인자, 요청 할 값
//    private int page = 1;
//
//    // mybatis에서 사용 할 limit, offset
//    private int limit;
//    private int offset;

}