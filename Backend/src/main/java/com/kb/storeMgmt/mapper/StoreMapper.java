package com.kb.storeMgmt.mapper;

import com.kb.storeMgmt.dto.NeighborhoodDTO;
import com.kb.storeMgmt.dto.SalesInfoDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface StoreMapper {

    // 가게 정보 삽입 메서드 (매퍼 XML에서 구현)
    void insertStore(NeighborhoodDTO neighborhoodDTO);

    List<String> getstoreList();

    void updateStore(NeighborhoodDTO neighborhoodDTO);
}
