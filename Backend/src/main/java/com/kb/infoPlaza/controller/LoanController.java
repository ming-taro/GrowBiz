package com.kb.infoPlaza.controller;

import com.kb.infoPlaza.dto.*;
import com.kb.infoPlaza.service.BusinessItemService;
import com.kb.infoPlaza.service.LoanService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/infoPlaza/loan")
@RequiredArgsConstructor
@Slf4j
public class LoanController {
    private final LoanService service;

    @GetMapping("/getBest4")
    public ResponseEntity<List<GovernmentFundDTO>> getBest4List() {
        return ResponseEntity.ok(service.getBest4List() );
    }

    @GetMapping("/getBestCreditLoan4List")
    public ResponseEntity<List<PersonalCreditLoanDTO>> getBestCreditLoan4List() {
        return ResponseEntity.ok(service.getBestCreditLoan4List() );
    }

    @GetMapping("/getBestJeonse4List")
    public ResponseEntity<List<JeonseDTO>> getBestJeonse4List() {
        return ResponseEntity.ok(service.getBestJeonse4List() );
    }

    @GetMapping("/getBestMortgage4List")
    public ResponseEntity<List<MortgageDTO>> getBestMortgage4List() {
        return ResponseEntity.ok(service.getBestMortgage4List() );
    }

    @GetMapping("/getFilteredList")
    public ResponseEntity<List<GovernmentFundDTO>> getFilteredList(GovernmentFilterDTO governmentFilter) {
        return ResponseEntity.ok(service.getFilteredList(governmentFilter));
    }

    @GetMapping("/getFilteredCreditLoanList")
    public ResponseEntity<List<PersonalCreditLoanDTO>> getFilteredCreditLoanList(PersonalFilterDTO personalFilter) {
        return ResponseEntity.ok(service.getFilteredCreditLoanList(personalFilter));
    }

    @GetMapping("/getFilteredJeonseList")
    public ResponseEntity<List<JeonseDTO>> getFilteredJeonseList(JeonseFilterDTO jeonseFilter) {
        return ResponseEntity.ok(service.getFilteredJeonseList(jeonseFilter));
    }

    @GetMapping("/getFilteredMortgageList")
    public ResponseEntity<List<MortgageDTO>> getFilteredMortgageList(JeonseFilterDTO jeonseFilter) {
        return ResponseEntity.ok(service.getFilteredMortgageList(jeonseFilter));
    }

    @GetMapping("/getDetailItem")
    public ResponseEntity<GovernmentFundDTO> getDetailItem(String productName) {
        return ResponseEntity.ok(service.getDetailItem(productName));
    }

    @GetMapping("/getDetailItemCreditLoan")
    public ResponseEntity<PersonalCreditLoanDTO> getDetailItemCreditLoan(Long id) {
        return ResponseEntity.ok(service.getDetailItemCreditLoan(id));
    }

    @GetMapping("/getDetailItemJeonse")
    public ResponseEntity<JeonseDTO> getDetailItemJeonse(Long id) {
        return ResponseEntity.ok(service.getDetailItemJeonse(id));
    }

    @GetMapping("/getDetailItemMortgage")
    public ResponseEntity<MortgageDTO> getDetailItemMortgage(Long id) {
        return ResponseEntity.ok(service.getDetailItemMortgage(id));
    }

    @GetMapping("/getKBLoanAll")
    public ResponseEntity<List<KBLoanDTO>> getAllKBLoanInfo() {
        return ResponseEntity.ok(service.getAllKBLoanInfo());
    }

    @GetMapping("/getKBLoan/{loanKey}")
    public ResponseEntity<KBLoanDTO> getKBLoanInfoByLoanKey(@PathVariable String loanKey) {
        return ResponseEntity.ok(service.getKBLoanInfoByLoanKey(loanKey));
    }

    @GetMapping("/getKBLoanBest4")
    public ResponseEntity<List<KBLoanDTO>> getKBLoanBest4Info() {
        return ResponseEntity.ok(service.getKBLoanBest4Info());
    }

    @GetMapping("/getKBLoanRecommand")
    public ResponseEntity<List<KBLoanDTO>> getKBLoanRecommand() {
        return ResponseEntity.ok(service.getKBLoanRecommand());
    }

    @GetMapping("/getFilteredKBLoan")
    public ResponseEntity<List<KBLoanDTO>> getFilteredKBLoan(KBFilterDTO kbFilter) {
        return ResponseEntity.ok(service.getFilteredKBLoan(kbFilter));
    }


}
