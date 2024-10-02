package com.kb.infoPlaza.service;


import com.kb.infoPlaza.dto.IndividualEduDTO;
import com.kb.infoPlaza.dto.IndividualEduParam;
import com.kb.infoPlaza.mapper.IndividualEduMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Slf4j
@RequiredArgsConstructor
@Service
public class IndividualEduService {


    private final IndividualEduMapper mapper;


    public List<IndividualEduDTO> selectAllIndividualEdu() {
        System.out.println("@@@!!!!");
        log.info("getlist-----------------");
        List<IndividualEduDTO> list = mapper.selectAllIndividualEdu();
        return list;
    }


    public IndividualEduDTO selectIndividualEduById(int vno) {
        log.info("get------------------------------");
        IndividualEduDTO individualEduDTO = mapper.selectIndividualEduById(vno);
        return Optional.ofNullable(individualEduDTO)
                .orElseThrow(() -> new NoSuchElementException("Can't find video number" + vno ));
    }

    public List<IndividualEduDTO> searchIndividualEduByKeyword(IndividualEduParam param) {
        // Option 배열이 존재하면 category에서 검색
        if (param.getOption() != null && !param.getOption().isEmpty()) {
            return mapper.searchIndividualEduByKeyword(param);
        }

        // Option이 없을 경우 기본 검색 처리 (필요시 전체 데이터를 반환하거나 에러 처리 가능)
        return new ArrayList<>();  // 예: 빈 리스트 반환
    }

//
//    public List<IndividualEduDTO> searchIndividualEduByKeyword(IndividualEduParam param) {
//
//        // OPTION 배열을 이용한 검색 조건
//        if (param.getOption() != null && !param.getOption().isEmpty()) {
//            return mapper.searchByOption(param);
//        }
//
//        // searchType과 searchValue가 있을 경우 추가 검색 조건 처리
//        if (!param.getSearchType().isEmpty() && !param.getSearchValue().isEmpty()) {
//            return mapper.searchByKeyword(param);
//        }
//
//        // 기본 검색 로직 (OPTION이 없을 경우)
//        return mapper.findAll();
//    }

//    public List<IndividualEduDTO> searchIndividualEduByOption(IndividualEduParam individualEduParam){
//        List<IndividualEduDTO> list = mapper.searchIndividualEduByOption(individualEduParam);
//        if (list == null || list.isEmpty()){
//            list = new ArrayList<>();
//        }
//        return list;
//    }

}
