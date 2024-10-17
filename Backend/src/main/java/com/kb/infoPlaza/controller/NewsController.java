package com.kb.infoPlaza.controller;

import org.json.JSONArray;
import org.json.JSONObject;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/news")
public class NewsController {

    @Value("${naver.api.key}")
    private String naverApiKey;

    @Value("${naver.secret}")
    private String naverSecret;

    // 날짜 기반으로 뉴스를 가져오도록 변경된 API
    @GetMapping("")
    public ResponseEntity<Map<String, Object>> getNews(@RequestParam String query,
                                                       @RequestParam String startDate,
                                                       @RequestParam String endDate) throws IOException {

        // 네이버 뉴스 API 요청 URL 구성 (날짜 추가)
        String apiUrl = "https://openapi.naver.com/v1/search/news.json?query=" + query +
                "&display=10&start=1&sort=date" +
                "&startDate=" + startDate + "&endDate=" + endDate;

        // 네이버 API 요청
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.set("X-Naver-Client-Id", naverApiKey);
        headers.set("X-Naver-Client-Secret", naverSecret);

        HttpEntity<String> entity = new HttpEntity<>(headers);
        ResponseEntity<String> response = restTemplate.exchange(apiUrl, HttpMethod.GET, entity, String.class);

        // 뉴스 데이터를 JSON으로 변환
        JSONObject jsonResponse = new JSONObject(response.getBody());
        JSONArray items = jsonResponse.getJSONArray("items");

        List<Map<String, String>> newsList = new ArrayList<>();

        // 각 뉴스 항목별로 썸네일 추출
        for (int i = 0; i < items.length(); i++) {
            JSONObject item = items.getJSONObject(i);

            String title = item.getString("title");
            String link = item.getString("link");
            String description = item.getString("description");

            // 썸네일과 본문 추출을 위한 크롤링
            String thumbnail = "";
            String content = "";
            try {
                Document doc = Jsoup.connect(link).get();
                Element imgElement = doc.selectFirst("meta[property=og:image]");
                Element contentElement = doc.selectFirst("p");

                if (imgElement != null) {
                    thumbnail = imgElement.attr("content");
                }
                if (contentElement != null) {
                    content = contentElement.text();
                }
            } catch (Exception e) {
                e.printStackTrace();
                thumbnail = "default_thumbnail.png"; // 크롤링 실패 시 기본 썸네일 설정
            }

            // 뉴스 항목 정보 저장
            Map<String, String> newsData = new HashMap<>();
            newsData.put("title", title);
            newsData.put("link", link);
            newsData.put("description", description);
            newsData.put("thumbnail", thumbnail);
            newsData.put("content", content);

            newsList.add(newsData);
        }

        // 결과 데이터 반환
        Map<String, Object> responseData = new HashMap<>();
        responseData.put("news", newsList);

        return ResponseEntity.ok(responseData);
    }
}
