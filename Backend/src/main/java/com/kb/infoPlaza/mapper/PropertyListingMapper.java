package com.kb.infoPlaza.mapper;

import com.kb.infoPlaza.dto.DistrictCodeDTO;
import com.kb.infoPlaza.dto.PropertyListingDTO;
import java.util.List;

public interface PropertyListingMapper {

    // 모든 매물 조회
    List<PropertyListingDTO> selectAllPropertyListings();

    // 특정 매물 조회
    PropertyListingDTO selectPropertyListingById(int plno); // 메서드 이름 변경

    //모든 구 이름 조회
    List<DistrictCodeDTO> selectDistinctGuNames();


}
