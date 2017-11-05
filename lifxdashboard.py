#test
import sys
from lifxlan import LifxLAN
from prettytable import PrettyTable

lan = LifxLAN()
lights = lan.get_lights()

headers = "Name","IP Address","Power","Pow Lvl","Hue","Sat","Temp K"
table = PrettyTable(headers)

for light in lights:
    name = light.get_label()
    ipaddr = light.get_ip_addr()
    power = light.get_power()
    getcolor = light.get_color()
    powlvl = getcolor[2]/65535
    hue = getcolor[0]
    sat = getcolor[1]
    temp = getcolor[3]
    table.add_row([name,ipaddr,power,powlvl,hue,sat,temp])

table.align["Name"] = "l"
table.align["IP Address"] = "l"
print (table.get_string(sortby="Name"))
