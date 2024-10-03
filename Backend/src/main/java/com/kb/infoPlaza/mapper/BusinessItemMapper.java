package com.kb.infoPlaza.mapper;

import com.kb.infoPlaza.dto.Best3DTO;
import com.kb.infoPlaza.dto.BusinessClosureDTO;
import com.kb.infoPlaza.dto.BusinessFilterDTO;
import com.kb.infoPlaza.dto.BusinessItemDTO;

import java.util.List;

public interface BusinessItemMapper {
    List<BusinessItemDTO> getBest3List(Best3DTO best3);

    List<BusinessItemDTO> getTotal5();

    List<BusinessItemDTO> getTotal();

    List<BusinessItemDTO> getFilteredList(BusinessFilterDTO businessFilter);

    List<BusinessClosureDTO> getFilteredCloseList(BusinessFilterDTO businessFilter);

    List<String> getDong(String gu);

    List<String> getDongClose(String gu);

    List<BusinessItemDTO> getPortion5(String location);

    List<BusinessItemDTO> getPortion(String location);

    List<BusinessClosureDTO> getRate5();

    List<BusinessClosureDTO> getRate();
}
