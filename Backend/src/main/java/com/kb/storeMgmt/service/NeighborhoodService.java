package com.kb.storeMgmt.service;

import com.kb.storeMgmt.dto.NeighborhoodDTO;
import com.kb.storeMgmt.mapper.NeighborhoodMapper;
import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.*;

@Service
public class NeighborhoodService {

    @Value("${kakao.api.key}")
    private String kakaoApiKey;

    @Autowired
    private NeighborhoodMapper neighborhoodMapper;

    public NeighborhoodDTO getAddressById(NeighborhoodDTO neighborhoodDTO) {
        return neighborhoodMapper.findAddressById(neighborhoodDTO.getId());
    }

    public Map<String, Object> getNearbyInfo(String address) {
        Map<String, Object> result = new HashMap<>();
        Coordinate centerCoord = getCoordinates(address);
        if (centerCoord == null) {
            return result;
        }
        result.put("center", centerCoord);
        List<String> nearbyDongs = getNearbyDongsByCoordinates(centerCoord);
        result.put("nearbyDongs", nearbyDongs);
        List<Coordinate> convenienceStores = getConvenienceStores(nearbyDongs);
        result.put("convenienceStores", convenienceStores);
        return result;
    }

    Coordinate getCoordinates(String address) {
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

    List<String> getNearbyDongsByCoordinates(Coordinate center) {
        Set<String> nearbyDongs = new HashSet<>();
        List<Coordinate> points = generatePointsInRadius(center, 1);
        for (Coordinate point : points) {
            try {
                String urlStr = String.format("https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=%.7f&y=%.7f", point.x, point.y);
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
                for (int i = 0; i < documents.length(); i++) {
                    JSONObject document = documents.getJSONObject(i);
                    String dongName = document.getString("region_3depth_name");
                    nearbyDongs.add(dongName);
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return new ArrayList<>(nearbyDongs);
    }

    private List<Coordinate> generatePointsInRadius(Coordinate center, double radiusKm) {
        List<Coordinate> points = new ArrayList<>();
        double earthRadius = 6371; // 지구 반지름 (km)
        double latDelta = (radiusKm / earthRadius) * (180 / Math.PI);
        double lonDelta = latDelta / Math.cos(center.y * Math.PI / 180);
        // 중심점만 포함
        points.add(center);
        // 북, 동, 남, 서 방향의 점 추가
        points.add(new Coordinate(center.x, center.y + latDelta));
        points.add(new Coordinate(center.x + lonDelta, center.y));
        points.add(new Coordinate(center.x, center.y - latDelta));
        points.add(new Coordinate(center.x - lonDelta, center.y));
        return points;
    }

    private List<Coordinate> getConvenienceStores(List<String> dongs) {
        List<Coordinate> stores = new ArrayList<>();

        for (String dong : dongs) {

            try {
                String encodedDong = URLEncoder.encode(dong + " 편의점", StandardCharsets.UTF_8);
                String urlStr = "https://dapi.kakao.com/v2/local/search/keyword.json?query=" + encodedDong;
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
                for (int i = 0; i < documents.length(); i++) {
                    JSONObject document = documents.getJSONObject(i);
                    double x = document.getDouble("x");
                    double y = document.getDouble("y");
                    stores.add(new Coordinate(x, y));
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return stores;
    }

    public static class Coordinate {
        public double x, y;

        public Coordinate(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }
}
