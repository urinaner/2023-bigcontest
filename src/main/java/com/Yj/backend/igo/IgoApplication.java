package com.Yj.backend.igo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class IgoApplication {

	public static void main(String[] args) {
		SpringApplication.run(IgoApplication.class, args);
	}

}
