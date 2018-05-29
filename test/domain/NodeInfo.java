package com.test.domain;

import javax.persistence.Entity;

@Entity
public class NodeInfo extends SqlBaseEntity{
	
	private Long nodeId;
	private String name;
	private String fqdn;
	private String sno;

	public Long getNodeId() {
		return nodeId;
	}

	public void setNodeId(Long nodeId) {
		this.nodeId = nodeId;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getFqdn() {
		return fqdn;
	}

	public void setFqdn(String fqdn) {
		this.fqdn = fqdn;
	}

	public String getSno() {
		return sno;
	}

	public void setSno(String sno) {
		this.sno = sno;
	}
}
