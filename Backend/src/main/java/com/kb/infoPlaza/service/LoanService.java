package com.kb.infoPlaza.service;

import com.kb.infoPlaza.dto.*;
import com.kb.infoPlaza.mapper.LoanMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@RequiredArgsConstructor
@Service
public class LoanService {
    private final LoanMapper mapper;

    public List<GovernmentFundDTO> getBest4List() {
        return mapper.getBest4List();
    }

    public List<GovernmentFundDTO> getFilteredList(GovernmentFilterDTO governmentFilter) { return mapper.getFilteredList(governmentFilter); }

    public GovernmentFundDTO getDetailItem(String productName) { return mapper.getDetailItem(productName); }
}
