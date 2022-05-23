# day=int(input("enter the day"))
# month=int(input("enter the month"))
# if month<1 and month>2:
#     print("wrong input")
# elif month>=3 and month<=4:
#     if month==3 and day>=3:
#         print(day,"/", month,"is spring season")
#     elif month==3 and day<3:
#         print(day,"/", month,"is winter season")
#     else:
#         print(day,"/",month, "is spring season")
# if month<=2 and month>=11:
#     print(day,"/",month,"is winter season")
# elif month>=5 and month<=8:
#     if month==5 and day>=5:
#         print(day,"/",month,"is summer season")
#     elif month==5 and day<5:
#         print(day,"/",month,"is spring season")
#     else:
#         print(day,"/",month,"is summer season")
# if month>=9 and month<=10:
#     if month==9 and day>=5:
#         print(day,"/",month,"is rainy season")
#     elif month==9 and day<5:
#          print(day,"/",month,"is summer season")
#     else:
#         print(day,"/",month,"is rainy season")
# else:
#     print("winter season")

# user=float(input("enter the first number"))
# user1=float(input("enter the second number")) 
# user2=float(input("enter the third number")) 
# if user>user1:
#     if user<user2:
#         median=user
#     elif user1>user2:
#         median=user1
#     else:
#         print("user2")
# else:
#     if user>user2:
#         median = user
#     elif user1<user2:
#         median=user1
#     else:
#         median=user2
#     print("the median is",median)

# user=int(input("enter the first number"))
# user1=int(input("enter the second number")) 
# user2=int(input("enter the third number")) 
# if user>user1:
#     if user<user2:
#         median=user
#     elif user1>user2:
#         median=user1
#     else:
#         print("user2")
# else:
#     if user>user2:
#         median = user
#     elif user1<user2:
#         median=user1
#     else:
#         median=user2
#     print("the median is",median)

# d=int(input("enter the day"))
# m=int(input("enter the month"))
# y=int(input("enter the year"))
# if((y%4==0)and(y%100!=0)) or (y%400==0):
#     if m==2:
#        d1=29
#     elif m==1 or m==3 or m==5 or m==7 or m==8 or m==12:
#         d1=31
#     else:
#         d1=30
# else:
#     if m==2:
#         d1=28
#     elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
#         d1=31
#     else:
#         d1=30
# if d==31 and m==12:
#     d=1
#     m=1
#     y=y+1
# elif d1-d==0:
#     m=m+1
#     d=1
# else:
#     d=d+1
#     print("next day is:",d,"/",m,"/",y)

# if True:
#     print("A")
# if False:
#     print("B")
# if 1:
#     print("S")
# if 0:
#     print("h")
# if "false":
#     print("A")
# if "true":
#     print("M")
# if "":
#     print("R")
# if "0":
#     print("D")
# if "1":
#     print("0")

# years=int(input("enter the year"))
# if years%4==0:
#     print("leap year")
#     if years%400==0:  
#         print("century leap year")
#     else:    
#          print("not century year")
# else:
#     print("not leap year") 

# age=int(input("enter the age"))
# sex=input("enter the sex m/f")
# if sex=='f' :
#     print("she will work in urbans only")
#     if sex=='m':
#         if age>=20 and age<=40: 
#             print("he may work in anywhere")
#         if age>40 and age<=60 :
#             print("may work only in urban")
# else:
#     print("invalid")
# sex=input("enter the sex")
# age=int(input("enter the age"))
# marital_status=input("enter the status yes/no")
# if sex=="male":
#     if marital_status=="yes":
#         print("married")
#     if age>=20 and age<=40:
#         print("can work anywhere")
#     elif age>40 and age<=60:
#         print("work olny in urban")
#     else:
#         print("sorry")
# elif sex=="female":
#     print("work in urban areas")
# else:
#     print("error")

# date=int(input("enter the days"))
# if date and num<=1:
#     print("no fine")
#     if num>0 and num<=10:
#         fine=15*num
#         print("fine will be minimum")
#     else:
#         print("maximum")
#     if num>=12:
#         fine=500*num
#         print("expected month")
#         if num>=365:
#             fine=10000*num
#             print("fine to be given")
#         else:
#             print("error")
# else:
#     print("expected")

# public class Solution {
# public static void main(String[] args) {
 
#   Scanner in=new Scanner(System.in);
 
#   int DA=in.nextInt();
#   int MA=in.nextInt();
#   int YA=in.nextInt();
 
#   int DE=in.nextInt();
#   int ME=in.nextInt();
#   int YE=in.nextInt();
 
#   int fine=10000;

#   if(YA>YE)
#     System.out.println(fine);
#   else if(YA<YE)
#     {
#      {
#       fine=0; 
#       System.out.println(fine);
#       }
#      }
#     else if(ME<MA)
#        {
#       fine=500*Math.abs(MA-ME);
#       System.out.println(fine);
#        }
#     else if(MA==ME)
#     {
#        if(DA>DE)
#        {
#         fine=1*15*Math.abs(DE-DA);
#         System.out.println(fine);
#       }
#     else
#         {
#         fine=0; 
#         System.out.println(fine);
#         }
#       }
#      else
#         {
#          fine=0; 
#          System.out.println(fine);

# DA=int(input("enter the day"))
# MA=int(input("enter the day"))
# YA=int(input("enter the day"))
# DE=int(input("enter the day"))
# ME=int(input("enter the day"))
# YE=int(input("enter the day"))
# int ==10000
# if (YA>YE):
#     print("fine")
# if (YA<YE):
#     fine=0
#     print("fine")
# if (ME<MA):
#     fine=500*math(MA-ME)
#     print("fine")
# if(MA==ME):
#     if(DA>DE):
#         fine=15*math(DE-DA)
#         print("fine")
# else:
#     fine=0
#     print("fine")

# expect_day=int(input("enter the day"))
# expect_month=int(input("enter the month"))
# expect_year=int(input("enter the year"))
# return_day=int(input("enter the return_day"))
# return_month=int(input("enter the return_month"))
# return_year=int(input("enter the return_year"))
# if expect_year==return_year:
#     if expect_month==return_month:
#         if expect_day==return_day:
#            print("no fine")
#         else:
#             print("cost of book",(return_day-expect_day)*15)
#     else:
#         print("cost of book",(return_month-expect_month)*500)
# else:
#     print("cost of book",(return_year-expect_month)*10000)
    
# post=input("enter the post")
# name=input("enter the name")
# work=input("enter the work")
# if post=="FM":
#     if name=="onring and lalitha":
#         if work=="food management":
#             print("post=",post)
#             print("name=",name)
#             print("work=",work)
#         else:
#             print("error")
# elif post=="FC":
#     if name=="seminao and likita":
#         if work=="food co-ordinater":
#             print("post=",post)
#             print("name=",name)
#             print("work=",work)
#         else:
#             print("invalid")
# elif post=="disco":
#     if name =="worshim and raji":
#         if work=="discipline":
#             print("post=",post)
#             print("name=",name)
#             print("work=",work)
#         else:
#             print("work")    
# elif post=="TNP":
#     if name=="anisha and grace":
#         if work=="training and placement":
#             print("post=",post)
#             print("name=",name)
#             print("work=",work)
#         else:
#             print("training")
# elif post=="IT":
#     if name=="swarna":
#         if work=="information technology":
#             print("post=",post)
#             print("name=",name)
#             print("work=",work)
#         else:
#             print("technology")
 
# day=input("enter the day")
# mealtime=input('enter the mealtime')
# if day=="monday":
#     if mealtime=="breakfast":
#         print("breakfast=","sambhar rice")
#         if mealtime=="lunch":
#             print("sambharrice")
#             if mealtime=="dinner":
#                 print("chicken rice")
#         else:
#             print("sambhar rice")
# elif day=="tuesday":
#     if mealtime=="lunch":
#        print("breakfast=","poorisabji")
#     else:
#         print("nothing")
# elif mealtime=="dinner":
#         print("rajmarice")
# elif day=="tuesday":
#     if mealtime=="dinner":
#         print("breakfast=","poha")
#         print("lunch=","rajmarice")
#     else:  
#         print("dinner=","rotisabji")        

# day=input("enter the day")
# time=input("enter the time")
# if day=="monday":
#     if time=="morning":
#         print("exercise")
# elif time=="noon":
#     print("coding","lunch")
#     if time=="night":
#         print("english class","dinner","snacks")
#     elif day=="tuesday":
#         if time=="morning":
#             print("going out")
#         elif time=="noon":
#             print("coding","playing")
#         elif time=="night":
#             print("study","dinner")
#         elif day=="sunday":
#             if time=="morning":
#                 print("going to church")
#             elif day=="sunday":
#                 if time=="noon":
#                     print("bible study")
#             elif time=="night":
#                 print("evening worship")
#             elif day=="saturday":
#                 if time=="morning":
#                     print("breakfast")
#                     if time=="noon":
#                         print("hackathon")
#                 if time=="night":
#                     print("task","sleep")
#                 else:
#                     print("not included")
# 
# day=input("enter the day")
# meal_time=input("enter the meal_time") 
# if day=="monday":
#     if meal_time=="breakfast":
#         print("porri sabji")
#     elif meal_time=="lunch":
#         print("sambhar rice") 
#     else:
#         print("chicken rice")
# elif day=="tuesday":
#     if meal_time=="breakfast":
#         print("poha")
#     elif meal_time=="lunch":
#         print("rajma chawal")
#     else:
#         print("roti sabji") 
# else:
#     print("nothing")     

# language=input("enter the language") 
# if language=="english":
#     print("welcome to Manipur rural bank\swipe your card")
#     balance=20000
#     print("transaction:\n1.balance inquiry:\n2.withdrawal:\n3.deposit:\n4.transfer_money:\n5.exit")
#     transaction=int(input("enter the transaction:")) 
#     if transaction==1 or transaction==2 or transaction==3 or transaction==4:
#         atm_pin=int(input("enter the pin"))
#         if atm_pin==5656:
#             if transaction==1:
#                print("balance is",balance)  
#             elif transaction==2:
#                withdrawal_amount=int(input("enter the withdrawal_amount"))
#                if withdrawal_amount<=balance:
#                   total=balance-withdrawal_amount
#                   print(total)   
#                   print("collect your cash\.thank you") 
#             elif transaction==3:
#                 deposit=int(input("enter the deposit_amount"))
#                 if deposit>0:
#                     total=balance+deposit
#                     print(total)  
#                     print("your deposit successful\.thank you")
#                 else:
#                     print("no deposit")
#             elif transaction==4:
#                 transfer_money=int(input("enter the transfer_money")) 
#                 if transfer_money>0:
#                     total=balance-transfer_money
#                     print(total) 
#                     print("your money has been transfer\.thank you")  
#                 else:
#                     print("transfer failed") 
#     elif transaction==5:
#         exit=input("do you want to exit?:") 
#         if exit=="yes":
#             print("thank you for visiting")
#         else:
#             print("choose your transaction")
# else:
#     print("language does not exit")

# import datetime
# now=datetime.datetime.now()
# print("current date and time:")
# print(now.strftime("%Y-%m-%d,%H:%M:%S"))

# date=int(input("enter the date"))
# month=int(input("enter the month"))
# year=int(input("enter the year"))
# sec=int(input("enter the  sec"))
# minute=int(input("enter the minute"))
# hour=int(input("enter the hour"))
# if date==1 or date<=31:
#     if month>=1 and month<=12:
#         if year>=0:
#             print("",date,month,year,"\n")
# if sec>=0 and sec<=60:
#     if minute>=0 and minute<=60:
#         if hour>=0 and hour<=12:
#             print("",sec,minute,hour)
# else:
#     print("time error")

# date=int(input("enter the date"))
# month=int(input("enter the month"))
# year=int(input("enter the year"))
# sec=float(input("enter the  sec"))
# minute=float(input("enter the minute"))
# hour=int(input("enter the hour"))
# if date==1 or date<=31:
#     if month>=1 and month<=12:
#         if year>=0:
#             print("",date,":",month,":",year,"\n")
# if sec>=0 and sec<=60:
#     if minute>=0 and minute<=60:
#         if hour>=0 and hour<=12:
#             print("",sec,":",minute,":",hour)
# else:
#     print("time error")

# password=input("enter the number")
# if len(password)>=8:
#     if"a"or"#"or"$"or"%"or"&"or"-" in password:
#         if "0"or"9"is password:
#             if "a"or"A"is password:
#                 print("strong pasword")
#             else:
#                 print("weak password")
#         else:
#              print("wrong")
#     else:
#         print("error")
# else:
#     print("invalid")

# a=input("enter the string")
# if len(a)>=3:
#     if "ing" not in a:
#         print(a+"ing")
#     elif "ing" in a:
#         print(a+"ly")
#     else:
#         print("error")
# else:
#     print(a)




        
