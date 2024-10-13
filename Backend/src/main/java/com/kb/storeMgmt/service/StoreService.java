package com.kb.storeMgmt.service;

import com.kb.storeMgmt.mapper.NeighborhoodMapper;
import org.json.JSONArray;
import org.json.JSONObject;
import com.kb.storeMgmt.dto.NeighborhoodDTO;
import com.kb.storeMgmt.mapper.StoreMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.List;

@Service
@RequiredArgsConstructor
public class StoreService {

    private final StoreMapper storeMapper;

    @Value("${kakao.api.key}")
    private String kakaoApiKey;

    private final NeighborhoodService neighborhoodService; // 주변 동이름을 가져오는 서비스 추가

    private final NeighborhoodMapper neighborhoodMapper;

    // 가게 저장 로직
    public void saveStore(NeighborhoodDTO neighborhoodDTO) {
        // 주소를 기반으로 좌표 정보 획득
//        NeighborhoodService.Coordinate coordinates = neighborhoodService.getCoordinates(neighborhoodDTO.getAddress());
        NeighborhoodService.Coordinate coordinates = neighborhoodService.getCoordinates(neighborhoodDTO.getAddress());
        if (coordinates != null) {
            // 좌표를 기반으로 주변 동 이름 획득
            List<String> nearbyDongs = neighborhoodService.getNearbyDongsByCoordinates(coordinates);
            String dongname = String.join(", ", nearbyDongs.stream()
                    .map(String::valueOf)
                    .toArray(String[]::new));

            if (!nearbyDongs.isEmpty()) {
                // 첫 번째 동 이름을 dongname에 저장
                neighborhoodDTO.setDongname(dongname);
            }
        }

        Coordinate coord = getCoordinates(neighborhoodDTO.getAddress());
        String addressname = getDongByCoordinates(coord);

        neighborhoodDTO.setAddressname(addressname);

        if (neighborhoodMapper.findAddressById(neighborhoodDTO.getId()) != null) {
            storeMapper.updateStore(neighborhoodDTO); // 기존 정보가 있으면 업데이트
        } else {
            storeMapper.insertStore(neighborhoodDTO); // 새로운 정보 삽입
        }

    }

    // 주소 -> 좌표 변환
    private Coordinate getCoordinates(String address) {
        try {
            String encodedAddress = URLEncoder.encode(address, StandardCharsets.UTF_8);
            String urlStr = "https://dapi.kakao.com/v2/local/search/address.json?query=" + encodedAddress;
            URL url = new URL(urlStr);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Authorization", "KakaoAK " + kakaoApiKey);

            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = br.readLine()) != null) {
                response.append(line);
            }
            br.close();

            JSONObject jsonResponse = new JSONObject(response.toString());
            JSONArray documents = jsonResponse.getJSONArray("documents");

            if (documents.length() > 0) {
                JSONObject firstResult = documents.getJSONObject(0);
                double x = firstResult.getDouble("x");
                double y = firstResult.getDouble("y");
                return new Coordinate(x, y);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    // 좌표 -> 행정동 정보 가져오기
    private String getDongByCoordinates(Coordinate coord) {
        try {
            String urlStr = String.format("https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=%.7f&y=%.7f", coord.x, coord.y);
            URL url = new URL(urlStr);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Authorization", "KakaoAK " + kakaoApiKey);

            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = br.readLine()) != null) {
                response.append(line);
            }
            br.close();

            JSONObject jsonResponse = new JSONObject(response.toString());
            JSONArray documents = jsonResponse.getJSONArray("documents");

            // 행정동 정보 추출
            for (int i = 0; i < documents.length(); i++) {
                JSONObject document = documents.getJSONObject(i);
                if (document.getString("region_type").equals("H")) { // H는 행정동
                    return document.getString("region_3depth_name"); // 행정동 이름 반환
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "행정동 정보 없음";
    }

    // 좌표 객체
    public static class Coordinate {
        public double x, y;

        public Coordinate(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    public List<String> getstoreList() {
        return storeMapper.getstoreList();
    }

}
