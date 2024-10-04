package com.kb.infoPlaza.mapper;

import com.kb.infoPlaza.dto.*;

import java.util.List;

public interface LoanMapper {
    List<GovernmentFundDTO> getBest4List();

    List<GovernmentFundDTO> getFilteredList(GovernmentFilterDTO governmentFilter);

    GovernmentFundDTO getDetailItem(String productName);
}
