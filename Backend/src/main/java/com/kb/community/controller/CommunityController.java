package com.kb.community.controller;
import com.kb.community.dto.CategoryDTO;
import com.kb.community.dto.CommentDTO;
import com.kb.community.dto.PostDTO;
import com.kb.community.service.CategoryService;
import com.kb.community.service.CommentService;
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
    private final CommentService commentService;

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
    @PostMapping("/{category}/create")
    public ResponseEntity<Void> createPost(@PathVariable String category, @RequestBody PostDTO post) {
        communityService.createPost(category, post);
        return ResponseEntity.ok().build();
    }

    // 게시글 삭제
    @DeleteMapping("/view/{postId}")
    public ResponseEntity<Void> deletePost(@PathVariable Long postId) {
        communityService.deletePost(postId);
        return ResponseEntity.ok().build();
    }

    // 게시글 수정
    @PutMapping("/{category}/edit")
    public ResponseEntity<Void> updatePost(@PathVariable String category, @RequestBody PostDTO post) {
        communityService.updatePost(post);
        return ResponseEntity.ok().build();
    }

    // 특정 게시글 조회 및 조회수 증가
    @GetMapping("/view/{postId}")
    public ResponseEntity<PostDTO> getPostById(@PathVariable long postId) {
        communityService.incrementViewCount(postId);
        PostDTO post = communityService.getPostById(postId);
        return ResponseEntity.ok(post);
    }


    // 특정 게시글의 댓글 조회
    @GetMapping("/comment/{postId}")
    public ResponseEntity<List<CommentDTO>> getCommentsByPostId(@PathVariable Long postId) {
        List<CommentDTO> comments = commentService.getCommentsByPostId(postId);
        return ResponseEntity.ok(comments);
    }

    // 댓글 추가
    @PostMapping("/comment")
    public ResponseEntity<Void> addComment(@RequestBody CommentDTO commentDTO) {
        commentService.addComment(commentDTO);
        return ResponseEntity.ok().build();
    }

    // 댓글 삭제
    @DeleteMapping("/comment/{commentId}")
    public ResponseEntity<Void> deleteComment(@PathVariable Long commentId, @RequestParam("userId") String userId) {
        commentService.deleteComment(commentId, userId); // userId를 파라미터로 추가
        return ResponseEntity.noContent().build();
    }

    // 좋아요 추가
    @PostMapping("/view/{postId}/like")
    public ResponseEntity<Void> likePost(@PathVariable Long postId) {
        communityService.incrementLikes(postId);
        return ResponseEntity.ok().build();
    }

    // 싫어요 추가
    @PostMapping("/view/{postId}/dislike")
    public ResponseEntity<Void> dislikePost(@PathVariable Long postId) {
        communityService.incrementDislikes(postId);
        return ResponseEntity.ok().build();
    }

    // 카테고리와 키워드로 게시글 검색
    @GetMapping("/{category}/search")
    public ResponseEntity<List<PostDTO>> searchPosts(
            @PathVariable String category,
            @RequestParam String keyword,
            @RequestParam String filterType) {
        List<PostDTO> posts = communityService.searchPosts(category, keyword, filterType);
        return ResponseEntity.ok(posts);
    }
}
