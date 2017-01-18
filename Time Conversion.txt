time=str(input())
if time[len(time)-2:]=="AM":
    if time[:2]=="12":
        print("00",end="")
        print(time[2:len(time)-2])
    else:
        print(time[:len(time)-2])
else:
    if time[:2]=="12":
      print("12",end="")
      print(time[2:len(time)-2])
    else:
      print(int(time[:2])+12,end="")
      print(time[2:len(time)-2])