#!/usr/bin/env python
import re
import sys
import cisco
import syslog
from cli import *
#======= functions definitions ========
def f_route_check(route):
#"route" - variable passed from CLI execution of this script
# print('\nexecuting route_check')
 route_search = cli('show ip route '+route+' static')
 route_test = re.search(route+', ubest/mbest:', route_search)
 if route_test != None:
  return True
 else:
  return False
  
#-------
def f_ping_test(host_IP):
# print('\nexecuting ping_test')
 pingTest = cli('ping '+host_IP+' count 2 timeout 1')
 pingFailedRegex = re.compile(r'0 packets received, 100.00% packet loss')
 pingTEST = pingFailedRegex.search(pingTest)
# print('ping test -> ' + str(pingTEST))
 if pingTEST == None:
  return True
 else:
  return False
#--------
def f_syslog(var_logg):
 #severity for USERS log 3
 syslog.syslog(3,var_logg)
 
#============ MAIN SCRIPT =============
def main():
# print('<route> <route_nexthop> <ping_test_host>')
 arg_table = sys.argv
# print(arg_table)
 #----
 var_route = arg_table[1]
 var_nexthop = arg_table[2]
 var_ping_host = arg_table[3] 
 cmd_add_route = 'conf t ; ip route '+var_route+' '+var_nexthop
 cmd_remove_route = 'conf t ; no ip route '+var_route+' '+var_nexthop
 #----
 if f_ping_test(var_ping_host) == True:
  #If ping succeeded and route is not there - add route
#  print('function ping ->' + str(f_ping_test(var_ping_host)))
  if f_route_check(var_route) == False:
   cli(cmd_add_route)
#   print('function route ->' + str(f_route_check(var_route)))
   msg = 'ADDING static route to: ' + var_route
   f_syslog(msg)
#   print('ping OK, no route')
  #If ping succeeded and route is already there - do nothing
 else:
 #If ping failed and route is already there - remove route 
  if f_route_check(var_route) == True:
   cli(cmd_remove_route)
#   print('ping BAD, route exists')
   msg = 'REMOVING static route to: ' + var_route
   f_syslog(msg)
 
 
#============= EXECUTION ============= 
main() 
