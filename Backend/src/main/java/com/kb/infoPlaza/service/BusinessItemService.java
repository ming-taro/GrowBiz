package com.kb.infoPlaza.service;

import com.kb.infoPlaza.dto.Best3DTO;
import com.kb.infoPlaza.dto.BusinessClosureDTO;
import com.kb.infoPlaza.dto.BusinessItemDTO;
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
