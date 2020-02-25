import csv
f=open('500000 Sales Records.csv')
reader=csv.reader(f)
counter=0
totalUnitsOnline=0
totalUnitsOffline=0
totalRevOnline=0
totalRevOffline=0
i=0
salesChannels={}
for row in reader:
    if counter==0:
        print (row)
    if i!=0:
        salesChannels[row[3]] = row[4]
        if row[13]=="Online":
            totalUnitsOnline+=int(row[8])
            totalRevOnline+=int(row[11])
        counter +=1
  #      elif row[13]=="Offline":
  #          totalUnitsOffline+=int(row[8])
   #         totalRevOffline+=int(row[11])
    else:
        i+=1
f.close()

print("There are %d order records." % (counter))
print("There were %d units sold Offline." % (totalUnitsOffline))
print("There were %d units sold Online." % (totalUnitsOnline))
print("The total revenue of units sold Offline is %d." % (totalRevOffline))
print("The total revenue of units sold Online is %d." % (totalRevOnline))
print("list of sales channels:")

list = salesChannels.keys()
msg = ""
for key in list:
    msg += key + " "

    print(msg)
