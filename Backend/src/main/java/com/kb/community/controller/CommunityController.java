package com.kb.community.controller;
import com.kb.community.dto.CategoryDTO;
import com.kb.community.dto.PostDTO;
import com.kb.community.service.CategoryService;
import com.kb.community.service.CommunityService;
import io.swagger.annotations.Api;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/community")
@RequiredArgsConstructor
@Slf4j
@Api(value = "CommunityController", tags = "커뮤니티")
public class CommunityController {

    private final CategoryService categoryService;
    private final CommunityService communityService;

    // 모든 카테고리 조회
    @GetMapping("/all-category")
    public ResponseEntity<List<CategoryDTO>> getAllCategories() {
        List<CategoryDTO> categories = categoryService.getAllCategories();
        return ResponseEntity.ok(categories);
    }

    // 카테고리별 게시글 조회
    @GetMapping("/{category}")
    public ResponseEntity<List<PostDTO>> getPostsByCategory(@PathVariable String category) {
        List<PostDTO> posts = communityService.getPostsByCategory(category);
        return ResponseEntity.ok(posts);
    }

    // 게시글 생성
    @PostMapping
    public ResponseEntity<Void> createPost(@RequestBody PostDTO post) {
        communityService.createPost(post);
        return ResponseEntity.ok().build();
    }

    // 게시글 삭제
    @DeleteMapping("/{postId}")
    public ResponseEntity<Void> deletePost(@PathVariable Long postId) {
        communityService.deletePost(postId);
        return ResponseEntity.ok().build();
    }

    // 게시글 수정
    @PutMapping
    public ResponseEntity<Void> updatePost(@RequestBody PostDTO post) {
        communityService.updatePost(post);
        return ResponseEntity.ok().build();
    }
}
