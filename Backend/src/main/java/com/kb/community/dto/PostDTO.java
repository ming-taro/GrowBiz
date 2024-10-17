package com.kb.community.dto;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;
@Setter
@Getter
@Data
public class PostDTO {
    private long postId;       // 게시글 ID
    private long originalPostId; // 원래 DB post_id
    private String userId;        // 사용자 ID
    private String title;      // 제목
    private String content;    // 내용
    private String createdAt;   // 생성 시간
    private String category;    // 카테고리
    private long view;         // 조회수
    private long recommend;     // 추천 수
    private long noRecommend;   // 비추천 수

}
