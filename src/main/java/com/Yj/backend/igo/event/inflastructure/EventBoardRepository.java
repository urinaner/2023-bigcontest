package com.Yj.backend.igo.event.inflastructure;

import com.Yj.backend.igo.event.domain.EventBoard;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EventBoardRepository extends JpaRepository<EventBoard, Long> {
}
