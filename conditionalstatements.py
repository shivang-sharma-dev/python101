#and keyword is use to join to multiple if/elif statements together to add more conditions to a output . 


#combining if and elif multi statements using and operator 

aws_marks= 750
python=True 

if aws_marks>=750 and python==True:
    print("You get a Macbook")
elif aws_marks>=900 or python==True:
    print("You Get AWS Coupons")
elif aws_marks>=600 and python==True:
    print("You get a Smart watch")
elif aws_marks>=500 and python==True:
    print("You get a Power Bank")

else:
    print("You get nothing") 



#solved example 

eating_sugar = True
telling_lies = True

if eating_sugar == True and telling_lies == True :
    print("Open your mouth")    



#Repord Card Using if else statements 

score = 28

if score == 100:
    print ("Outstanding")
elif score >=80 and score <=100:
    print ("Excellent")
elif score >=60 and score <=81:
    print ("Good")
elif score==60 or score<=60:
    print ("Can do better!")

#Electricity Count 
units = 241

if units >=201 and units <=300:
  print(units*4.0)
  