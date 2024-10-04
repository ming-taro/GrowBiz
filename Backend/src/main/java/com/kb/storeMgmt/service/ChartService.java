package com.kb.storeMgmt.service;

import com.kb.storeMgmt.dto.FlowPopulationDTO;
import com.kb.storeMgmt.mapper.ChartMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ChartService {

    @Autowired
    private ChartMapper chartMapper;
    
    public FlowPopulationDTO getFlpopCobyDongname(FlowPopulationDTO flowPopulationDTO){
        return chartMapper.getFlpopCobyDongname(flowPopulationDTO.getAdstrdCdNm());
    }
}
