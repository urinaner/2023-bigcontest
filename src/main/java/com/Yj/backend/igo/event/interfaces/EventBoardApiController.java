package com.Yj.backend.igo.event.interfaces;

import com.Yj.backend.igo.event.application.EventBoardService;
import com.Yj.backend.igo.event.interfaces.response.EventBoardResponse;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.List;

@RestController
@RequestMapping("/api/event")
public class EventBoardApiController {

    private EventBoardService eventBoardService;

    public EventBoardApiController(EventBoardService eventBoardService){
        this.eventBoardService = eventBoardService;
    }

    @GetMapping
    List<EventBoardResponse> getEventBoardList(){
        return eventBoardService.getEventBoardList();
    }



}
