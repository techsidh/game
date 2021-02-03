'''comman=" "
started=False
while comman !="quit":
    comman=input("+").lower()
    if comman=="start":
        if started:
            print('car is already started')
        else:
            started=True
            print("car started")
    elif comman=="stop":
        if not started:
            print("car is already stop")
        else:
            started=False
            print("car stopped")
    elif comman=="help":
        print("""
        start-to start the car
        stop-to stop the car
        quit-to exit""")
        break
    else:
        print("hey what you want")
        break
for item in range(5,45,6):
    print(item)

total=0
for price in [10,20,40]:
    total += price
print(f"total: {total}")

val=int(input(">"))
i=0
for i in range(1,11):
    print(val,"x",i,"=",val*i)

unit_num=int(input("---"))
for bill in range(2):
    if unit_num > 60:
        bill=unit_num*3.3
        print(f"bill price : {bill}")
    elif unit_num >125:
        bill=unit_num*3.95
        print(bill)