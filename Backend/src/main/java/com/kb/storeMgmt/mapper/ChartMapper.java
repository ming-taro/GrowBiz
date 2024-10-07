package com.kb.storeMgmt.mapper;

import com.kb.storeMgmt.dto.CategoriesDTO;
import org.apache.ibatis.annotations.Param;

import java.util.List;

public interface ChartMapper {
    public List<CategoriesDTO> getDoughnut(CategoriesDTO categoriesDTO);

    List<CategoriesDTO> getMixAddress(CategoriesDTO categoriesDTO);

}
