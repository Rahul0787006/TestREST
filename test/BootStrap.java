package com.test;

import com.test.config.env.EnvConfig;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.stereotype.Component;

@Component
public class BootStrap implements ApplicationListener<ContextRefreshedEvent> {
	private static Logger logger = LoggerFactory.getLogger(BootStrap.class);

	@Autowired
	private EnvConfig envConfig;

	@Override
	public void onApplicationEvent(ContextRefreshedEvent arg0) {

	}

}
