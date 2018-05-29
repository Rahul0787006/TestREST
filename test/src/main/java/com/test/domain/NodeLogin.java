package com.test.domain;

import javax.persistence.Entity;
import javax.persistence.OneToOne;

@Entity
public class NodeLogin extends SqlBaseEntity {

    private Long nodeId;
    private String userName;
    private String password;

    public Long getNodeId() {
        return nodeId;
    }

    public void setNodeId(Long nodeId) {
        this.nodeId = nodeId;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
