package com.kb.community.mapper;

import com.kb.community.dto.CategoryDTO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface CategoryMapper {
    List<CategoryDTO> getAllCategories(); // 모든 카테고리 가져오기
}
