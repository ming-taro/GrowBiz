package com.kb.community.mapper;

import com.kb.community.dto.PostDTO;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface CommunityMapper {

    // 카테고리별 게시글 조회
    List<PostDTO> getPostsByCategory(@Param("category") String category);

    PostDTO selectPostById(@Param("postId") long id);

    // 게시글 생성
    void createPost(@Param("category") String category, @Param("post") PostDTO post);

    // 게시글 삭제
    void deletePost(@Param("postId") Long postId);

    // 게시글 수정
    void updatePost(PostDTO post);

    // 조회수 증가
    void incrementViewCount(@Param("postId") long postId);

    // 좋아요 추가
    void incrementLikes(@Param("postId") Long postId);

    // 싫어요 추가
    void incrementDislikes(@Param("postId") Long postId);

    // 제목으로 검색
    List<PostDTO> searchPostsByTitle(@Param("category") String category, @Param("keyword") String keyword);

    // 내용으로 검색
    List<PostDTO> searchPostsByContent(@Param("category") String category, @Param("keyword") String keyword);

    // 작성자로 검색
    List<PostDTO> searchPostsByUserId(@Param("category") String category, @Param("keyword") String keyword);

    // 모두 검색
    List<PostDTO> searchPosts(@Param("category") String category, @Param("keyword") String keyword);
}
