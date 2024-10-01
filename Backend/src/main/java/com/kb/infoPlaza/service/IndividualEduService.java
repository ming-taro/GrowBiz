package com.kb.infoPlaza.service;


import com.kb.infoPlaza.dto.IndividualEduDTO;
import com.kb.infoPlaza.mapper.IndividualEduMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

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


    public IndividualEduDTO selectIndividualEduById(String videoId)
    {
        log.info("get------------------------------");
        IndividualEduDTO dto = mapper.selectIndividualEduById(videoId);
        return Optional.ofNullable(dto)
                .orElseThrow(NoSuchElementException::new);
    }
}
