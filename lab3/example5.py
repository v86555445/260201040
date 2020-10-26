month=input("enter the month :")
day=int(input("enter the day :"))
month=month.lower()
months=["january","february","march","april","may","june","july","august","september","october","november","december"]
q=months.index(month)
if day<=0 or day>31:
    print("please enter appropriate day")
else:
    if q==2 or q==3 or q==4:
        season="spring"
        if q==2 and day<20:
            season="winter"
    elif q==11 or q==0 or q==1:
        season="winter"
        if q==11 and day<21:
            season="fall"
    elif q==5 or q==6 or q==7:
        season=="summer"
        if q==5 and day<21:
            season="spring"
    elif q==8 or q==9 or q==10:
        season="fall"
        if q==8 and day<22:
            season="summer"
    print("season is :",season)