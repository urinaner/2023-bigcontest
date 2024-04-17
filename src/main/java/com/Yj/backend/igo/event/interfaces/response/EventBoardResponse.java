package com.Yj.backend.igo.event.interfaces.response;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.Date;

@Getter
@Setter
@Builder
public class EventBoardResponse {

    private Long id;
    private String codename;
    private String guname;
    private String title;
    private String dateTime;
    private String place;
    private String orgName;
    private String useTarget;
    private String useFee;
    private String playerInfo;
    private String program;
    private String etcDesc;
    private String orgLink;
    private String mainImg;
    private Date rgstDate;
    private String ticket;
    private Date startDate;
    private Date endDate;
    private String themeCode;
    private Double latitude;
    private Double longitude;
    private String isFree;
    private String hmpgAddr;

}
