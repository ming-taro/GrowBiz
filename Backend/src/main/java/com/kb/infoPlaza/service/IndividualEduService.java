package com.kb.infoPlaza.service;


import com.kb.infoPlaza.dto.IndividualEduDTO;
import com.kb.infoPlaza.dto.IndividualEduParam;
import com.kb.infoPlaza.mapper.IndividualEduMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.*;

@Slf4j
@RequiredArgsConstructor
@Service
public class IndividualEduService {


    private final IndividualEduMapper mapper;


    public List<IndividualEduDTO> selectAllIndividualEdu() {
        List<IndividualEduDTO> list = mapper.selectAllIndividualEdu();
        return list;
    }


    public IndividualEduDTO selectIndividualEduById(int vno) {
        IndividualEduDTO individualEduDTO = mapper.selectIndividualEduById(vno);
        return Optional.ofNullable(individualEduDTO)
                .orElseThrow(() -> new NoSuchElementException("Can't find video number" + vno ));
    }

    public List<IndividualEduDTO> searchIndividualEduByOption(IndividualEduParam param) {
        // Option 배열이 존재하면 category에서 검색
        System.out.println("searchIndividualEduByOption");
        if (param.getOption() != null && !param.getOption().isEmpty()) {
            return mapper.searchIndividualEduByOption(param);
        }
        // Option이 없을 경우 기본 검색 처리 (필요시 전체 데이터를 반환하거나 에러 처리 가능)
        return new ArrayList<>();  // 예: 빈 리스트 반환
    }

    public List<IndividualEduDTO> searchIndividualEdu(IndividualEduParam param) {
        List<IndividualEduDTO> list = new ArrayList<>();
        System.out.println("searchIndividualEdu");
        // 필터 타입에 따라 적절한 게시글 리스트 가져오기
        switch (param.getSearchType()) {
            case "title":
                list = mapper.searchIndividualEduByTitle(param);
                break;
            case "content":
                list = mapper.searchIndividualEduByContent(param);
                break;
            case "all":
                list = mapper.searchIndividualEdu(param);
                break;
            default:
                throw new IllegalArgumentException("Invalid filter type: " + param.getSearchType());
        }
        return list;
    }

    public List<IndividualEduDTO> searchIndividualEduByKeyword(IndividualEduParam param) {
        if (param.getSearchKeyword() == null || param.getSearchKeyword().isEmpty()) {
            return new ArrayList<>(); // 검색어가 없을 경우 빈 리스트 반환
        }

        switch (param.getSearchType()) {
            case "title":
                return mapper.searchIndividualEduByTitle(param);
            case "content":
                return mapper.searchIndividualEduByContent(param);
            case "all":
                return mapper.searchIndividualEduByKeyword(param); // 전체 검색
            default:
                throw new IllegalArgumentException("Invalid search type: " + param.getSearchType());
        }
    }
}
