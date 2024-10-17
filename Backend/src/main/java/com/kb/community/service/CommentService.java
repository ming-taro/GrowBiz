package com.kb.community.service;

import com.kb.community.dto.CommentDTO;
import com.kb.community.mapper.CommentMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
public class CommentService {
    private final CommentMapper commentMapper;

    // 특정 게시글의 댓글 조회
    public List<CommentDTO> getCommentsByPostId(Long postId) {
        return commentMapper.findByPostId(postId);
    }

    // 댓글 추가
    @Transactional
    public void addComment(CommentDTO commentDTO) {
        commentMapper.insertComment(commentDTO);
    }

    // 댓글 삭제
    @Transactional
    public void deleteComment(Long commentId, String userId) {
        commentMapper.deleteComment(commentId, userId); // userId를 파라미터로 추가
    }
}
