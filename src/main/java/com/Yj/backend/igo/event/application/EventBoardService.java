package com.Yj.backend.igo.event.application;

import com.Yj.backend.igo.event.domain.EventBoard;
import com.Yj.backend.igo.event.inflastructure.EventBoardRepository;
import com.Yj.backend.igo.event.interfaces.response.EventBoardResponse;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import lombok.Data;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class EventBoardService {

    private final EventBoardRepository eventBoardRepository;

    public EventBoardService(EventBoardRepository eventBoardRepository){
        this.eventBoardRepository = eventBoardRepository;
    }

    public List<EventBoardResponse> getEventBoardList(){
        return eventBoardRepository.findAll().stream().map(this::transform).collect(Collectors.toList());
    }

    private EventBoardResponse transform(EventBoard eventBoard) { //entity -> DTO
        return EventBoardResponse.builder()
                .id(eventBoard.getId())
                .codename(eventBoard.getCodename())
                .guname(eventBoard.getGuname())
                .title(eventBoard.getTitle())
                .dateTime(eventBoard.getDateTime())
                .place(eventBoard.getPlace())
                .orgName(eventBoard.getOrgName())
                .useTarget(eventBoard.getUseTarget())
                .useFee(eventBoard.getUseFee())
                .playerInfo(eventBoard.getPlayerInfo())
                .program(eventBoard.getProgram())
                .etcDesc(eventBoard.getEtcDesc())
                .orgLink(eventBoard.getOrgLink())
                .mainImg(eventBoard.getMainImg())
                .rgstDate(eventBoard.getRgstDate())
                .ticket(eventBoard.getTicket())
                .startDate(eventBoard.getStartDate())
                .endDate(eventBoard.getEndDate())
                .themeCode(eventBoard.getThemeCode())
                .latitude(eventBoard.getLatitude())
                .longitude(eventBoard.getLongitude())
                .isFree(eventBoard.getIsFree())
                .hmpgAddr(eventBoard.getHmpgAddr())
                .build();
    }

    public void init(String jsondata){ //json -> entity
        JsonParser parser = new JsonParser();
        JsonObject obj = parser.parse(jsondata).getAsJsonObject();
        JsonArray result = obj.getAsJsonObject("culturalEventInfo").getAsJsonArray("row");

        for (int i = 0; i < result.size(); i++) {
            JsonObject jObj = result.get(i).getAsJsonObject();

            eventBoardRepository.save(EventBoard.builder()
                    .codename(getSafeString(jObj, "CODENAME"))
                    .guname(getSafeString(jObj, "GUNAME"))
                    .title(getSafeString(jObj, "TITLE"))
                    .dateTime(getSafeString(jObj, "DATE"))
                    .place(getSafeString(jObj, "PLACE"))
                    .orgName(getSafeString(jObj, "ORG_NAME"))
                    .useTarget(getSafeString(jObj, "USE_TRGT"))
                    .useFee(getSafeString(jObj, "USE_FEE"))
                    .playerInfo(getSafeString(jObj, "PLAYER"))
                    .program(getSafeString(jObj, "PROGRAM"))
                    .etcDesc(getSafeString(jObj, "ETC_DESC"))
                    .orgLink(getSafeString(jObj, "ORG_LINK"))
                    .mainImg(getSafeString(jObj, "MAIN_IMG"))
                    .ticket(getSafeString(jObj, "TICKET"))
                    .themeCode(getSafeString(jObj, "THEMECODE"))
                    .latitude(getSafeDouble(jObj, "LAT"))
                    .longitude(getSafeDouble(jObj, "LOT"))
                    .isFree(getSafeString(jObj, "IS_FREE"))
                    .hmpgAddr(getSafeString(jObj, "HMPG_ADDR"))
                    .build());
        }
    }

    private String getSafeString(JsonObject obj, String key) {
        return obj.has(key) && !obj.get(key).isJsonNull() ? obj.get(key).getAsString() : "";
    }

    private double getSafeDouble(JsonObject obj, String key) {
        return obj.has(key) && !obj.get(key).isJsonNull() ? obj.get(key).getAsDouble() : 0.0;
    }


}
