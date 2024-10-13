package com.kb.infoPlaza.mapper;

import com.kb.infoPlaza.dto.DistrictCodeDTO;
import com.kb.infoPlaza.dto.PropertyListingDTO;
import java.util.List;

public interface PropertyListingMapper {

    // 모든 매물 조회
    List<PropertyListingDTO> selectAllPropertyListings();

    //동 이름으로 매물동 코드 조회
    String selectDongCodeByDongName(String dongName);

    //동 코드로 매물조회
    List<PropertyListingDTO> selectPropertyListingByDongCode(String dongCode);

    PropertyListingDTO findById(String id);
}
