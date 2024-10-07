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

    public List<PersonalCreditLoanDTO> getBestCreditLoan4List() { return mapper.getBestCreditLoan4List(); }

    public List<JeonseDTO> getBestJeonse4List() { return mapper.getBestJeonse4List(); }

    public List<GovernmentFundDTO> getFilteredList(GovernmentFilterDTO governmentFilter) { return mapper.getFilteredList(governmentFilter); }

    public List<PersonalCreditLoanDTO> getFilteredCreditLoanList(PersonalFilterDTO personalFilter) {
        return mapper.getFilteredCreditLoanList(personalFilter);
    }

    public List<JeonseDTO> getFilteredJeonseList(JeonseFilterDTO jeonse) {
        return mapper.getFilteredJeonseList(jeonse);
    }

    public GovernmentFundDTO getDetailItem(String productName) { return mapper.getDetailItem(productName); }

    public PersonalCreditLoanDTO getDetailItemCreditLoan(Long id) {
        return mapper.getDetailItemCreditLoan(id);
    }

    public JeonseDTO getDetailItemJeonse(Long id) {
        return mapper.getDetailItemJeonse(id);
    }
}

