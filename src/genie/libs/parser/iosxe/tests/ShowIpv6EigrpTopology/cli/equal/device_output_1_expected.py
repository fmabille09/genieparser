expected_output = {
    "eigrp_instance":{
        "1":{
            "vrf":{
                "default":{
                    "address_family":{
                        "IPv6":{
                            "eigrp_id":{
                                "2001:0DB8:10::/64":{
                                    "eigrp_routes":{
                                        "2001:0DB8:3::/64":{
                                            "route_code":"P",
                                            "successor_count":1,
                                            "FD":281600,
                                            "route_type":"Passive",
                                            "route":"2001:0DB8:3::/64",
                                            "known_via":"Connected",
                                            "outgoing_interface":"Ethernet1/0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}