package com.test.repository;

import com.test.domain.NodeInfo;
import org.springframework.data.jpa.repository.JpaRepository;

import java.io.Serializable;

public interface NodeInfoRepository extends JpaRepository<NodeInfo, Serializable> {

    public NodeInfo findById(Long nodeId);
}
