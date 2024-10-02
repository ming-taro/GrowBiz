package com.kb.infoPlaza.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class IndividualEduDTO {
        private int vno;
        private String videoUrl;              // video_id -> vno (camelCase)
        private String thumbnail;            // thumbnail -> thumbnail (camelCase)
        private String title;                // title -> title (camelCase)
        private String content;              // content -> content (camelCase)
        private String briefIntroduction;    // brief_introduction -> briefIntroduction (camelCase)
        private String learningGoal;         // learning_goal -> learningGoal (camelCase)
        private String category;             // category -> category (camelCase)
        private String eduTime;              // edu_time -> eduTime (camelCase)
        private String hashtag;              // hashtag -> hashtag (camelCase)
        private String industrySubcategory;  // industry_subcategory -> industrySubcategory (camelCase)
}

