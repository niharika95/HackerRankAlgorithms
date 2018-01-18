# import sys
#
# # print ("12 HOUR FORMAT")
# # hours12 = input("Hours: ")
# # minutes12 = input("Minutes: ")
# # seconds12 = input("Seconds: ")
# # ampm12 = input("AM(1) or PM(2): ")
# #
# # hh = hours12
# # mm = minutes12
# # ss = seconds12
# s = '07:05:45PM'
# li = s.split(':')
# li.append(li[-1][2:])
# li[-2] = (li[-2])[:2]
#
# hours12 = li[0]
# minutes12 = li[1]
# seconds12 = li[2]
# ampm12 = li[3]
#
# if (hours12>=1 and hours12<=12 and minutes12>=0 and minutes12<=59 and seconds12>=0 and seconds12<=59):
#     time12 = (str(hours12) + ":" + str(minutes12) + ":" + str(seconds12))
#     if ampm12 == 1:
#         print ("Time in 12 hour format: " + time12 + "AM")
#     if ampm12 == 2:
#         print ("Time in 12 hour format: " + time12 + "PM")
#
#     if (ampm12 == 2):
#         hours24 = hours12
#     elif (ampm12 == 1):
#         if (hours12 == 12):
#             hours24 = '00'
#     minutes24 = minutes12
#     seconds24 = seconds12
#
#     result = (str(hours24) + ":" + str(minutes24) + ":" + str(seconds24))
#     # print ("Time in 24 hour format: " + result)
# # else:
# #     print "Incorrect Information!"









#!/bin/python3

import sys

def timeConversion(s):
    li = s.split(':')
    li.append(li[-1][2:])
    li[-2] = (li[-2])[:2]

    hours12 = li[0]
    minutes12 = li[1]
    seconds12 = li[2]
    ampm12 = li[3]

    if(int(hours12)>=1 and int(hours12)<=12 and int(minutes12)>=0 and int(minutes12)<=59 and int(seconds12)>=0 and int(seconds12)<=59):
        time12 = (str(hours12) + ":" + str(minutes12) + ":" + str(seconds12))
        if ampm12 == 1:
            print ("Time in 12 hour format: " + time12 + "AM")
        if ampm12 == 2:
            print ("Time in 12 hour format: " + time12 + "PM")

        hours24 = 0
        if (ampm12 == 2):
            hours24 = hours12 + 12
        elif (ampm12 == 1):
            if (hours12 == 12):
                hours24 = '00'
            else:
                hours24 = hours12
        minutes24 = minutes12
        seconds24 = seconds12

        return (str(hours24) + ":" + str(minutes24) + ":" + str(seconds24))
        # print ("Time in 24 hour format: " + result)

s = input().strip()
result = timeConversion(s)
print(result)
