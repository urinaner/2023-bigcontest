package com.Yj.backend.igo.api.application;

import com.Yj.backend.igo.event.application.EventBoardService;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class ApiScheduler {
    private final int day = 1000;
    private final ApiScrapService apiScrapService;

    public ApiScheduler(ApiScrapService apiScrapService) {
        this.apiScrapService = apiScrapService;
    }

    @Scheduled(fixedDelay = day)
    public void dummy(){
        apiScrapService.sync();
    }

}
