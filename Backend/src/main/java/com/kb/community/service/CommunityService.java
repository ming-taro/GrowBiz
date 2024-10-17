package com.kb.community.service;
import com.kb.community.dto.PostDTO;
import com.kb.community.mapper.CommunityMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

@Slf4j
@Service
@RequiredArgsConstructor
public class CommunityService {

    private final CommunityMapper communityMapper;


    // 카테고리별 게시글 조회
    public List<PostDTO> getPostsByCategory(String category) {
        List<PostDTO> posts = communityMapper.getPostsByCategory(category);

        // 만약 posts가 비어있지 않다면
        if (!posts.isEmpty()) {
            // 가장 최근 게시글을 위로 오도록 내림차순 정렬 (created_at 기준)
            posts.sort(Comparator.comparing(PostDTO::getCreatedAt).reversed());

            // post_id를 가장 최근의 게시글에 대해 1부터 시작하도록 설정
            long postCount = posts.size();
            for (int i = 0; i < posts.size(); i++) {
                PostDTO post = posts.get(i);
                post.setOriginalPostId(post.getPostId());
                posts.get(i).setPostId(postCount - i); // 가장 최근 게시글에 대해 큰 id 할당
            }
        }
        return posts;
    }


    public PostDTO getPostById(long postId) {
        return communityMapper.selectPostById(postId);
    }

    // 게시글 생성
    @Transactional
    public void createPost(String category, PostDTO post) {
        communityMapper.createPost(category, post);
    }

    // 게시글 삭제
    @Transactional
    public void deletePost(Long postId) {
        communityMapper.deletePost(postId);
    }

    // 게시글 수정
    @Transactional
    public void updatePost(PostDTO post) {
        communityMapper.updatePost(post);
    }

    // 조회수 증가
    @Transactional
    public void incrementViewCount(long postId) {
        communityMapper.incrementViewCount(postId);
    }

    // 좋아요 추가
    @Transactional
    public void incrementLikes(Long postId) {
        communityMapper.incrementLikes(postId);
    }

    // 싫어요 추가
    @Transactional
    public void incrementDislikes(Long postId) {
        communityMapper.incrementDislikes(postId);
    }

    // 키워드 검색
    @Transactional
    public List<PostDTO> searchPosts(String category, String keyword, String filterType) {
        List<PostDTO> posts = new ArrayList<>();

        // 필터 타입에 따라 적절한 게시글 리스트 가져오기
        switch (filterType) {
            case "title":
                posts = communityMapper.searchPostsByTitle(category, keyword);
                break;
            case "content":
                posts = communityMapper.searchPostsByContent(category, keyword);
                break;
            case "user":
                posts = communityMapper.searchPostsByUserId(category, keyword);
                break;
            case "all":
                posts = communityMapper.searchPosts(category, keyword);
                break;
            default:
                throw new IllegalArgumentException("Invalid filter type: " + filterType);
        }

        // 검색 결과가 비어있지 않다면
        if (!posts.isEmpty()) {
            // 가장 최근 게시글을 위로 오도록 내림차순 정렬 (created_at 기준)
            posts.sort(Comparator.comparing(PostDTO::getCreatedAt).reversed());

            // post_id를 가장 최근의 게시글에 대해 1부터 시작하도록 설정
            long postCount = posts.size();
            for (int i = 0; i < posts.size(); i++) {
                PostDTO post = posts.get(i);
                post.setOriginalPostId(post.getPostId());
                posts.get(i).setPostId(postCount - i); // 가장 최근 게시글에 대해 큰 id 할당
            }
        }

        return posts;
    }
}
