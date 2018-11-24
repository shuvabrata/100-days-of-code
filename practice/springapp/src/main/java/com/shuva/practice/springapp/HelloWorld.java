package com.shuva.practice.springapp;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@EnableAutoConfiguration
@ComponentScan("com.shuva.practice.springapp")
public class HelloWorld {
    public static void main(String[] args) {
        SpringApplication.run(HelloWorld.class, args);
    }

    @Autowired
    private  AsynchronousService asynchronousService;

    @GetMapping("/")
    String get() {
        return "Just saying HelloWorld";
    }

    @GetMapping("/work")
    public String startWorkingAync() {
        asynchronousService.executeAsyncronously();
        return "Started Work";
    }
}
