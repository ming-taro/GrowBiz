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

    public List<MortgageDTO> getBestMortgage4List() { return mapper.getBestMortgage4List(); }

    public List<GovernmentFundDTO> getFilteredList(GovernmentFilterDTO governmentFilter) { return mapper.getFilteredList(governmentFilter); }

    public List<PersonalCreditLoanDTO> getFilteredCreditLoanList(PersonalFilterDTO personalFilter) {
        return mapper.getFilteredCreditLoanList(personalFilter);
    }

    public List<JeonseDTO> getFilteredJeonseList(JeonseFilterDTO jeonse) {
        return mapper.getFilteredJeonseList(jeonse);
    }

    public List<MortgageDTO> getFilteredMortgageList(JeonseFilterDTO jeonse) {
        return mapper.getFilteredMortgageList(jeonse);
    }

    public GovernmentFundDTO getDetailItem(String productName) { return mapper.getDetailItem(productName); }

    public PersonalCreditLoanDTO getDetailItemCreditLoan(Long id) {
        return mapper.getDetailItemCreditLoan(id);
    }

    public JeonseDTO getDetailItemJeonse(Long id) {
        return mapper.getDetailItemJeonse(id);
    }

    public MortgageDTO getDetailItemMortgage(Long id) {
        return mapper.getDetailItemMortgage(id);
    }

    public List<KBLoanDTO> getAllKBLoanInfo() {
        return mapper.getAllKBLoanInfo();
    }

    public KBLoanDTO getKBLoanInfoByLoanKey(String loanKey) {
        return mapper.getKBLoanInfoByLoanKey(loanKey);
    }

    public List<KBLoanDTO> getKBLoanBest4Info() {
        return mapper.getKBLoanBest4Info();
    }

    public List<KBLoanDTO> getKBLoanRecommand() { return mapper.getKBLoanRecommand();}

    public List<KBLoanDTO> getFilteredKBLoan(KBFilterDTO kbFilter) { return mapper.getFilteredKBLoan(kbFilter); }
}

