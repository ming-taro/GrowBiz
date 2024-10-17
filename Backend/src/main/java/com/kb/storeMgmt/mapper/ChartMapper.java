package com.kb.storeMgmt.mapper;

import com.kb.storeMgmt.dto.CategoriesDTO;
import com.kb.storeMgmt.dto.SalesInfoDTO;

import java.util.List;

public interface ChartMapper {
    public List<CategoriesDTO> getDoughnut(CategoriesDTO categoriesDTO);

    List<CategoriesDTO> getMixAddress(CategoriesDTO categoriesDTO);

    List<SalesInfoDTO> getmcfirst(SalesInfoDTO salesInfoDTO);

    List<CategoriesDTO> getmcsecend(CategoriesDTO categoriesDTO);

    CategoriesDTO getsum(CategoriesDTO categoriesDTO);

}
