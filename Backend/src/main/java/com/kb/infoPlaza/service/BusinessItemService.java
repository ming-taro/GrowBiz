package com.kb.infoPlaza.service;

import com.kb.infoPlaza.dto.*;
import com.kb.infoPlaza.mapper.BusinessItemMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Log4j
@Service
@RequiredArgsConstructor
public class BusinessItemService {
    private final BusinessItemMapper mapper;

    public List<BusinessItemDTO> getBest3List(Best3DTO best3) {
        return mapper.getBest3List(best3);
    }

    public List<BusinessItemDTO> getTotal5() {
        return mapper.getTotal5();
    }

    public List<BusinessItemDTO> getTotal() {
        return mapper.getTotal();
    }

    public List<BusinessItemDTO> getFilteredList(BusinessFilterDTO businessFilter) { return mapper.getFilteredList(businessFilter); }

    public List<BusinessItemDTO> getFilteredPortionList(BusinessMyLocationFilterDTO businessMyLocationFilter) { return mapper.getFilteredPortionList(businessMyLocationFilter); }

    public List<BusinessClosureDTO> getFilteredCloseList(BusinessFilterDTO businessFilter) { return mapper.getFilteredCloseList(businessFilter); }

    public List<String> getDong(String gu) { return mapper.getDong(gu); }

    public List<String> getDongClose(String gu) { return mapper.getDongClose(gu); }

    public List<BusinessItemDTO> getPortion5(String location) {
        return mapper.getPortion5(location);
    }

    public List<BusinessItemDTO> getPortion(String location) {
        return mapper.getPortion(location);
    }

    public List<BusinessClosureDTO> getRate5() {
        return mapper.getRate5();
    }

    public List<BusinessClosureDTO> getRate() {
        return mapper.getRate();
    }
}
