package com.kb.community.service;
import com.kb.community.dto.CategoryDTO;
import com.kb.community.mapper.CategoryMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Slf4j
@Service
@RequiredArgsConstructor
public class CategoryService {

    private final CategoryMapper categoryMapper;

    // 모든 카테고리 조회
    public List<CategoryDTO> getAllCategories() {
        List<CategoryDTO> categories = categoryMapper.getAllCategories();
        if (categories == null || categories.isEmpty()) {
            categories = new ArrayList<>();
        }
        return categories;
    }

}
