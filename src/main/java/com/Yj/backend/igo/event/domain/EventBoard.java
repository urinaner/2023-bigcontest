package com.Yj.backend.igo.event.domain;

import jakarta.persistence.*;
import lombok.*;

import java.util.Date;

@Entity
@Table(name = "event")
@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class EventBoard {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "codename")
    private String codename;

    @Column(name = "guname")
    private String guname;

    @Column(name = "title")
    private String title;

    @Column(name = "date_time")
    private String dateTime;

    @Column(name = "place")
    private String place;

    @Column(name = "org_name")
    private String orgName;

    @Column(name = "use_trgt")
    private String useTarget;

    @Column(name = "use_fee")
    private String useFee;

    @Column(name = "player_info")
    private String playerInfo;

    @Column(name = "program")
    private String program;

    @Column(name = "etc_desc")
    private String etcDesc;

    @Column(name = "org_link")
    private String orgLink;

    @Column(name = "main_img")
    private String mainImg;

    @Column(name = "rgst_date")
    private Date rgstDate;

    @Column(name = "ticket")
    private String ticket;

    @Column(name = "start_date")
    private Date startDate;

    @Column(name = "end_date")
    private Date endDate;

    @Column(name = "theme_code")
    private String themeCode;

    @Column(name = "latitude")
    private Double latitude;

    @Column(name = "longitude")
    private Double longitude;

    @Column(name = "is_free")
    private String isFree;

    @Column(name = "detail_addr")
    private String hmpgAddr;

}