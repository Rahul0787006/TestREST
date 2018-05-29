package com.test.controller;

import com.test.service.NodeService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import com.test.utils.ResponseHandler;
import java.util.Map;


@RestController
public class PublicController {

    @Autowired
    NodeService nodeService;

    private final Logger logger = LoggerFactory.getLogger(this.getClass());

    @RequestMapping(value = "/getAllNodeDetails", method = RequestMethod.GET)
    Object  getAllNodeDetails(HttpServletRequest request) {
        Map<String,Object> result = nodeService.getAllNodeDetails();
        if (result.get("isSuccess").equals("true")) {
            return ResponseHandler.generateResponse(HttpStatus.OK, true,
                    "data found", result.get("nodeData"));
        } else {
            return ResponseHandler.generateResponse(HttpStatus.BAD_REQUEST, false,
                    "data not found", result.get("nodeData"));
        }
    }

    @RequestMapping(value = "/getNode/{nodeId}", method = RequestMethod.GET)
    Object getNodeById(@PathVariable (value = "nodeId") Long nodeId, HttpServletRequest request) {
        Map<String,Object> result = nodeService.getNodeById(nodeId);
        if (result.get("isSuccess").equals("true")) {
            return ResponseHandler.generateResponse(HttpStatus.OK, true,
                    "data found", result.get("nodeData"));
        } else {
            return ResponseHandler.generateResponse(HttpStatus.BAD_REQUEST, false,
                    "data not found", result.get("nodeData"));
        }
    }

}
