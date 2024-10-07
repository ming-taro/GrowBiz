package com.kb.infoPlaza.mapper;

import com.kb.infoPlaza.dto.*;

import java.util.List;

public interface LoanMapper {
    List<GovernmentFundDTO> getBest4List();

    List<PersonalCreditLoanDTO> getBestCreditLoan4List();

    List<GovernmentFundDTO> getFilteredList(GovernmentFilterDTO governmentFilter);

    List<PersonalCreditLoanDTO> getFilteredCreditLoanList(PersonalFilterDTO personalFilter);

    GovernmentFundDTO getDetailItem(String productName);

    PersonalCreditLoanDTO getDetailItemCreditLoan(Long id);
}
