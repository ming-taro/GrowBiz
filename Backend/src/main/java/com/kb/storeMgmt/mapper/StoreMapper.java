package com.kb.storeMgmt.mapper;

import com.kb.storeMgmt.dto.NeighborhoodDTO;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface StoreMapper {

    // 가게 정보 삽입 메서드 (매퍼 XML에서 구현)
    void insertStore(NeighborhoodDTO neighborhoodDTO);
}
