package com.kb.storeMgmt.controller;

import com.kb.board.dto.BoardPageResult;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/store")
@RequiredArgsConstructor
@Slf4j
public class StoreMgmtController {
    @GetMapping("")
    public ResponseEntity<BoardPageResult> getList( ) {
        return null;
    }
}
