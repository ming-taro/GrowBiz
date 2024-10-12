package com.kb.infoPlaza.mapper;

import com.kb.infoPlaza.dto.IndividualEduDTO;
import com.kb.infoPlaza.dto.IndividualEduParam;
import io.swagger.models.auth.In;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface IndividualEduMapper {
    List<IndividualEduDTO> selectAllIndividualEdu();

    // 특정 영상 조회
   IndividualEduDTO selectIndividualEduById(int vno);

   List<IndividualEduDTO> searchIndividualEduByOption(IndividualEduParam individualEduParam);
   List<IndividualEduDTO> searchIndividualEdu(IndividualEduParam individualEduParam);
   List<IndividualEduDTO> searchIndividualEduByTitle(IndividualEduParam individualEduParam);
   List<IndividualEduDTO> searchIndividualEduByContent(IndividualEduParam individualEduParam);
    List<IndividualEduDTO> searchIndividualEduByKeyword(IndividualEduParam individualEduParam);

}
