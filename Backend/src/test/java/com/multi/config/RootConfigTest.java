package com.multi.config;

import com.kb._config.RootConfig;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import javax.sql.DataSource;

import java.sql.Connection;
import java.sql.SQLException;

import static org.junit.jupiter.api.Assertions.*;

@ExtendWith(SpringExtension.class)
@ContextConfiguration(classes= {RootConfig.class})
@Slf4j
class RootConfigTest {

    @Autowired
    private DataSource dataSource;

    @Autowired
    private SqlSessionFactory sqlSessionFactory;


    @Test
    @DisplayName("DataSource 연결이 된다.")
    public void dataSource() throws SQLException {
        try(Connection con = dataSource.getConnection()){
            log.info("DataSource 준비 완료", con);
        }
    }

    @Test
    public void testSqlSessionFactory() {
        try (
                SqlSession session = sqlSessionFactory.openSession();
                Connection con = session.getConnection();
        ) {
            log.info(session.toString());
            log.info(String.valueOf(con));
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }


}
