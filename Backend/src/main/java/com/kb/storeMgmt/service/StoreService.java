package com.kb.storeMgmt.service;

import com.kb.storeMgmt.dto.NeighborhoodDTO;
import com.kb.storeMgmt.mapper.StoreMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class StoreService {

    private final StoreMapper storeMapper;

    @Value("${kakao.api.key}")
    private String kakaoApiKey;

    private final NeighborhoodService neighborhoodService; // 주변 동이름을 가져오는 서비스 추가

    // 가게 저장 로직
    public void saveStore(NeighborhoodDTO neighborhoodDTO) {
        // 주소를 기반으로 좌표 정보 획득
//        NeighborhoodService.Coordinate coordinates = neighborhoodService.getCoordinates(neighborhoodDTO.getAddress());
        NeighborhoodService.Coordinate coordinates = neighborhoodService.getCoordinates(neighborhoodDTO.getAddress());
        if (coordinates != null) {
            // 좌표를 기반으로 주변 동 이름 획득
            List<String> nearbyDongs = neighborhoodService.getNearbyDongsByCoordinates(coordinates);
            String dongname = nearbyDongs.get(0);
//            List<String> nearbydongname = (List<String>) neighborhoodService.getNearbyInfo(dongname);
// 여기 수정 해야 함
//            System.out.println(nearbydongname);

            if (!nearbyDongs.isEmpty()) {
                // 첫 번째 동 이름을 dongname에 저장
                neighborhoodDTO.setAddressname(nearbyDongs.get(0));
            }
        }

        System.out.println(neighborhoodDTO);

        // 저장 로직 실행
//        storeMapper.insertStore(neighborhoodDTO);
    }
}
