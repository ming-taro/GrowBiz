package com.kb.storeMgmt.service;

import com.kb.storeMgmt.dto.CategoriesDTO;
import com.kb.storeMgmt.dto.SalesInfoDTO;
import com.kb.storeMgmt.mapper.ChartMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ChartService {

    @Autowired
    private ChartMapper chartMapper;

    public List<CategoriesDTO> getDoughnut(CategoriesDTO categoriesDTO) {
        return chartMapper.getDoughnut(categoriesDTO);
    }

    public List<CategoriesDTO> getMixAddress(CategoriesDTO categoriesDTO){
        return chartMapper.getMixAddress(categoriesDTO);
    }

    public List<SalesInfoDTO> getmcfirst(SalesInfoDTO salesInfoDTO){
        return chartMapper.getmcfirst(salesInfoDTO);
    }

    public List<CategoriesDTO> getmcsecend(CategoriesDTO categoriesDTO){
        return chartMapper.getmcsecend(categoriesDTO);
    }

    public CategoriesDTO getsum (CategoriesDTO categoriesDTO){
        return chartMapper.getsum(categoriesDTO);
    }

}
