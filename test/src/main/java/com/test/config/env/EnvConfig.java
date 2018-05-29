package com.test.config.env;


import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource({ "classpath:application-${spring.profiles.active}.properties" })
public class EnvConfig {

    @Value("${db.name}")
    private String dbName;
    @Value("${db.driver}")
    private String dbDriver;
    @Value("${db.port}")
    private String dbPort;
    @Value("${db.ip}")
    private String dbIpName;
    @Value("${db.auth.user}")
    private String dbUserName;
    @Value("${db.auth.pass}")
    private String dbPassword;

    public String getDbDriver() {
        return dbDriver;
    }

    public void setDbDriver(String dbDriverName) {
        this.dbDriver = dbDriverName;
    }

    public String getDbPort() {
        return dbPort;
    }

    public void setDbPort(String dbPort) {
        this.dbPort = dbPort;
    }

    public String getDbIpName() {
        return dbIpName;
    }

    public void setDbIpName(String dbIpName) {
        this.dbIpName = dbIpName;
    }

    public String getDbUserName() {
        return dbUserName;
    }

    public void setDbUserName(String dbUserName) {
        this.dbUserName = dbUserName;
    }

    public String getDbPassword() {
        return dbPassword;
    }

    public void setDbPassword(String dbPassword) {
        this.dbPassword = dbPassword;
    }

    public String getDbName() {

        return dbName;
    }

    public void setDbName(String dbName) {
        this.dbName = dbName;
    }
}
