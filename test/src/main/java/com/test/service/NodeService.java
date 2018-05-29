package com.test.service;

import com.test.domain.NodeInfo;
import com.test.repository.NodeInfoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.LocalVariableTableParameterNameDiscoverer;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@Service
public class NodeService {

    @Autowired
    NodeInfoRepository nodeInfoRepository;

    public Map<String, Object> getAllNodeDetails() {
        Map<String, Object> data = new HashMap<>();
        List<NodeInfo> nodeInfos = nodeInfoRepository.findAll();
        if(Optional.ofNullable(nodeInfos).isPresent()){
            data.put("isSuccess", "true");
            data.put("message", "data found");
            data.put("nodeData", nodeInfos);
        } else {
            data.put("isSuccess", "false");
            data.put("message", "data not found");
            data.put("nodeData", null);
        }
        return data;
    }

    public Map<String, Object> getNodeById(Long nodeId) {
        Map<String, Object> data = new HashMap<>();
        NodeInfo nodeInfo = nodeInfoRepository.findById(nodeId);
        if(Optional.ofNullable(nodeInfo).isPresent()){
            data.put("isSuccess", "true");
            data.put("message", "data found");
            data.put("nodeData", nodeInfo);
        } else {
            data.put("isSuccess", "false");
            data.put("message", "data not found");
            data.put("nodeData", null);
        }
        return data;
    }
}
