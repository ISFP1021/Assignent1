import csv

f = open("500000 Sales Records.csv", 'rt')

reader = csv.reader(f)
counter = 0
total = 0
totalUnitsOnline=0
totalRevOnline=0
totalUnitsOffline=0
totalRevOffline=0
i = 0
salesChannels = {}
for row in reader:
     if counter == 0:
          print(row)
     if i != 0:
          total+=int(row[8])
          salesChannels[row[3]] = row[4]
     if row[3]=="Offline":
          totalUnitsOffline+=int(row[8])
          totalRevOffline+=float(row[11])
     if row[3]=="Online":
          totalUnitsOnline+=int(row[8])
          totalRevOnline+=float(row[11])
     else:
          i+=1
          counter+=1
print("order records from Europe %d"%counter)
print("total amount of units sold %d"%total)

print ("list of item types:")
list = salesChannels.keys()
msg =""
for key in list:
   msg+=key + " "

print(msg)

print("There were %d units sold offline." % (totalUnitsOffline))
print("The total revenue of units sold Offline is %d." % (totalRevOffline))
print("There were %d units sold online." % (totalUnitsOnline))
print("The total revenue of units sold online is %d." % (totalRevOnline))
