package com.test.config.env;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import org.springframework.context.MessageSource;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.support.ReloadableResourceBundleMessageSource;
import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.servlet.LocaleResolver;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;
import org.springframework.web.servlet.i18n.AcceptHeaderLocaleResolver;
import org.springframework.web.servlet.i18n.LocaleChangeInterceptor;

import java.util.Locale;

/**
 * @author abhishek
 *
 */
//@PropertySource({ "classpath:locale/messages.properties" })
@Configuration
public class BaseConfig  extends WebMvcConfigurerAdapter {

	@Bean
    MessageSource messageSource(){
		
		ReloadableResourceBundleMessageSource messageSource =  new ReloadableResourceBundleMessageSource();
		messageSource.setBasenames("classpath:locale/messages", "classpath:locale/errors");
	//	messageSource.setUseCodeAsDefaultMessage(true);
		messageSource.setDefaultEncoding("UTF-8");
		messageSource.setCacheSeconds(3600);
		return messageSource;
		
	}
	
	@Bean
	public LocaleResolver localeResolver(){
	  // SessionLocaleResolver resolver = new SessionLocaleResolver();
		AcceptHeaderLocaleResolver resolver= new AcceptHeaderLocaleResolver();
	   resolver.setDefaultLocale(Locale.ENGLISH);
	   return resolver;
	}

	@Bean
    public LocaleChangeInterceptor localeInterceptor(){
		System.out.println("Am i reached her !!!!!");
        LocaleChangeInterceptor interceptor = new LocaleChangeInterceptor();
        interceptor.setParamName("lang");
        return interceptor;
    }

	@Override
	public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(localeInterceptor());
    }


   /* public void addInterceptors(InterceptorRegistry registry) {
	LocaleChangeInterceptor interceptor = new LocaleChangeInterceptor();
	interceptor.setParamName("locale");
	registry.addInterceptor(interceptor);
    }*/
	@Bean
	public MappingJackson2HttpMessageConverter mappingJackson2HttpMessageConverter() {
		ObjectMapper mapper = new ObjectMapper();
		mapper.configure(SerializationFeature.FAIL_ON_EMPTY_BEANS, false);
		MappingJackson2HttpMessageConverter converter = new MappingJackson2HttpMessageConverter(mapper);
		return converter;
	}

}

