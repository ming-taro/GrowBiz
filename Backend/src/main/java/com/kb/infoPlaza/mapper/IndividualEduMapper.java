package com.kb.infoPlaza.mapper;

import com.kb.infoPlaza.dto.IndividualEduDTO;
import com.kb.infoPlaza.dto.IndividualEduParam;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface IndividualEduMapper {
    List<IndividualEduDTO> selectAllIndividualEdu();

    // 특정 영상 조회
   IndividualEduDTO selectIndividualEduById(int vno);

   List<IndividualEduDTO> searchIndividualEduByKeyword(IndividualEduParam individualEduParam);
//   List<IndividualEduDTO> searchIndividualEduByOption(IndividualEduParam param);
}
