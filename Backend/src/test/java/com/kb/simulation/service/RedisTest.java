package com.kb.simulation.service;

import com.kb._config.RootConfig;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.TestPropertySource;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.context.web.WebAppConfiguration;

import java.util.List;


@WebAppConfiguration
@ExtendWith(SpringExtension.class)
@ContextConfiguration(classes = RootConfig.class)
@Slf4j
@TestPropertySource(locations = "classpath:application.properties")
public class RedisTest {
    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @Test
    public void addStoreCount() {
        redisTemplate.opsForHash().put("강남:역삼1동", "스타벅스", String.valueOf(10));
        redisTemplate.opsForHash().put("강남:역삼1동", "투썸플레이스", String.valueOf(11));
        redisTemplate.opsForHash().put("강남:역삼1동", "이디야", String.valueOf(12));

        Assertions.assertEquals(10, Integer.parseInt((String) redisTemplate.opsForHash().get("강남:역삼1동", "스타벅스")));
        Assertions.assertEquals(11, Integer.parseInt((String) redisTemplate.opsForHash().get("강남:역삼1동", "투썸플레이스")));
        Assertions.assertEquals(12, Integer.parseInt((String) redisTemplate.opsForHash().get("강남:역삼1동", "이디야")));
    }

    @Test
    public void deleteStoreCount() {
        List<String> deleteKey =  List.of("스타벅스", "투썸플레이스");

        long delete = redisTemplate.opsForHash().delete("강남:역삼1동", deleteKey.toArray());

        Assertions.assertEquals(delete, deleteKey.size());
    }
}