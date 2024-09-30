package com.kb.infoPlaza.mapper;

import com.kb.infoPlaza.dto.IndividualEduDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public class IndividualEduMapper {

    List<IndividualEduDTO> selectAllIndividualEdu();

    // 특정 매물 조회
   IndividualEduDTO selectIndividualEduById(String videoId);
}
