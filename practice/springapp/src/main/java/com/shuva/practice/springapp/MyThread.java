package com.shuva.practice.springapp;

import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;
import org.slf4j.Logger;

@Component
@Scope("prototype")
public class MyThread implements Runnable {
    private static final Logger LOG = LoggerFactory.getLogger(MyThread.class);

    @Override
    public void run() {
        LOG.info("I am the thread");
    }
}
