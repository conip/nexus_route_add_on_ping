# nexus_route_add_on_ping
script adds/removes static route on NEXUS platform based on PING result

tested in the following LAB environment on EVE-NG
NX-(10.1.1.1/24)------------(10.1.1.2/24)RTR(lo 0 – 8.8.8.8)

on NEXUS:
```
scheduler job name TEST
  python bootflash:/scripts/nx_route_track.py 10.10.0.0/16 10.1.1.2 8.8.8.8
 
end-job
 
scheduler schedule name ALA
  job name TEST
  time start now  repeat 00:00:01
```


to execute and test do the following
python nx_route_track.py <route> <route_nexthop> <ping_test_host>
