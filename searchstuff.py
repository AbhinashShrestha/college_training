# linear search
mainstuff=["dude1","dude2","dude3"]
i=0
a=len(mainstuff)
a=a-1
print(a)
item_to_search="dude"
for i in range(len(mainstuff)):
    if  mainstuff[i]==item_to_search:
        print("{}".format(item_to_search),"found")
    else:
        print("{}".format(item_to_search),"not found")
