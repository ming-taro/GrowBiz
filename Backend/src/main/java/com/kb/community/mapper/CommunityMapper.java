package com.kb.community.mapper;

import com.kb.community.dto.PostDTO;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface CommunityMapper {

    // 카테고리별 게시글 조회
    List<PostDTO> getPostsByCategory(@Param("category") String category);

    // 게시글 생성
    void createPost(PostDTO post);

    // 게시글 삭제
    void deletePost(@Param("postId") Long postId);

    // 게시글 수정
    void updatePost(PostDTO post);
}
