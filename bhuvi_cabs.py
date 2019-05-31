# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:21:59 2019

@author: test01
"""

i=0
while(i<10000):
    choice="yes"
    while(choice=="yes"):
        date=int(input("enter the date:"))
        month=int(input("enter the month:"))  
        year=int(input("enter the year:")) 
        day=input("enter the day:")
        print("the rate for type of vehicle is","A=15","B=25","C=40","D=60","for AC RS.5 EXTRA")
        choice_of_ac=input("enter whether AC or NON-AC:")
        type_of_vehicle=input("enter the type of vehicle:")
        distance_to_travel=eval(input("distance_to_travel:"))
        if(type_of_vehicle=="A"):
            bill_amount=15*distance_to_travel
        elif(type_of_vehicle=="B"):
            bill_amount=25*distance_to_travel
        elif(type_of_vehicle=="C"):
            bill_amount=40*distance_to_travel
        elif(type_of_vehicle=="D"):
            bill_amount=60*distance_to_travel
        if(choice_of_ac=="AC"):
            bill_amount=bill_amount+200
        elif(choice_of_ac=="NON-AC"):
            bill_amount=bill_amount
        else
            ("print invalid chooice")
         print("BHUVI CAB SERVICES")
         print("---------------------")
         print("bill no:",i)
         print(day,"/",month,"/",year,"        ",day)
         print("vehicle type:",type_of_vehicle)
         print("total distance travelled is:",distance_to_travel)
         print("total ride cost:",bill_amount)
         print("thankyou come again")
    print("do you want to continue? enter yes or no")
    choice=input("enter your choice yes or no:")
    i=i+1