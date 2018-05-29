/**
 * 
 */
package com.test.config.env;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.stereotype.Component;

import javax.sql.DataSource;


/**
 * @author abhishek
 *
 */
@Component
public class Datasource {
	@Autowired
	EnvConfig configuration;
	
	@Bean
	public DataSource dataSource(){
		DriverManagerDataSource dataSource = new DriverManagerDataSource();
		dataSource.setDriverClassName(configuration.getDbDriver());
		dataSource.setUrl("jdbc:mysql://"+configuration.getDbIpName()+":"+configuration.getDbPort()+"/"+configuration.getDbName()+"?autoReconnect=true&useSSL=false&useUnicode=yes&characterEncoding=UTF-8");
		dataSource.setUsername(configuration.getDbUserName());
		dataSource.setPassword(configuration.getDbPassword().trim());
		return dataSource;
	}
	
}
