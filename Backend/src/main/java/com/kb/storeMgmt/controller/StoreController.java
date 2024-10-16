package com.kb.storeMgmt.controller;

import com.kb.storeMgmt.dto.NeighborhoodDTO;
import com.kb.storeMgmt.service.StoreService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/store")
@RequiredArgsConstructor
@Slf4j
public class StoreController {

    private final StoreService storeService;

    @PostMapping("/insert")
    public ResponseEntity<String> insert(
            @RequestParam("address") String address,
            @RequestParam("id") String id,
            @RequestParam("detailAddress") String detailAddress,
            @RequestParam("rent") int rent,
            @RequestParam("utilityExpenses") int utilityExpenses,
            @RequestParam("laborCost") int laborCost,
            @RequestParam("otherExpenses") int otherExpenses,
            @RequestParam("svcIndutyCdNm") String svcIndutyCdNm,
            @RequestParam(value = "image", required = false) MultipartFile image,
            @RequestParam(value = "existingImage", required = false) String existingImage // 기존 이미지 파일명
    ) {
        String imageUrl = null;  // 이미지가 있을 경우 저장할 URL

        try {
            // 이미지가 있으면 파일 시스템에 저장
            if (image != null && !image.isEmpty()) {
                String fileName = UUID.randomUUID() + "_" + image.getOriginalFilename();
                Path filePath = Paths.get("C:/Users/student/Desktop/final/self-employed/Frontend/src/assets/img/upload", fileName); // 실제 저장 경로로 수정
                Files.copy(image.getInputStream(), filePath);
                image.getInputStream().close();  // 스트림을 명확하게 닫기

                imageUrl = fileName; // 저장 경로를 imageUrl로 설정
            }else if (existingImage != null && !existingImage.isEmpty()) {
                // 새로운 이미지가 없으면 기존 이미지 사용
                imageUrl = existingImage;
            }

            // DTO 생성 및 데이터 설정
            NeighborhoodDTO neighborhoodDTO = NeighborhoodDTO.builder()
                    .address(address)
                    .id(id)
                    .detailAddress(detailAddress)
                    .rent(rent)
                    .utilityExpenses(utilityExpenses)
                    .laborCost(laborCost)
                    .otherExpenses(otherExpenses)
                    .imageUrl(imageUrl)  // 이미지 경로 설정
                    .svcIndutyCdNm(svcIndutyCdNm)
                    .build();



            // 서비스에서 가게 정보를 저장하는 로직 호출
            storeService.saveStore(neighborhoodDTO);

            return ResponseEntity.ok("가게 등록이 완료되었습니다.");
        } catch (Exception e) {
            log.error("Error saving store", e);
            return ResponseEntity.status(500).body("가게 등록 중 오류 발생");
        }
    }

    @GetMapping("/list")
    public List<String> getstoreList() {
        return storeService.getstoreList();
    }


}
