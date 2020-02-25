import csv

import datetime

date_object = datetime.date.today()

f = open("500000 Sales Records.csv", 'rt')

reader = csv.reader(f)
counter = 0
total = 0
totalUnits=0

totalRev=0
totalUnitsOnline=0
totalRevOnline=0
totalUnitsOffline=0
totalRevOffline=0

totalUnitsSA=0
totalRevSA=0
totalUnitsME=0
totalRevME=0
totalUnitsAO=0
totalRevAO=0
totalUnitsE=0
totalRevE=0
totalUnitsA=0
totalRevA=0
totalUnitsCA=0
totalRevCA=0
totalUnitsNA=0
totalRevNA=0







i = 0
salesChannels = {}
regionsAnalysed = {}

for row in reader:
    if counter == 0:
        print(row)
    if i != 0:
        totalUnits += int(row[8])
        totalRev += float(row[11])
        total+=int(row[8])
        salesChannels[row[3]] = row[4]
        regionsAnalysed[row[0]] = row[1]
    if row[3]=="Offline":
        totalUnitsOffline+=int(row[8])
        totalRevOffline+=float(row[11])
    if row[3]=="Online":
        totalUnitsOnline+=int(row[8])
        totalRevOnline+=float(row[11])
    if row[0]=="Sub-Saharan Africa":
        totalUnitsSA+=int(row[8])
        totalRevSA+=float(row[11])
    if row[0]=="Middle East and North Africa":
        totalUnitsME+=int(row[8])
        totalRevME+=float(row[11])
    if row[0]=="Australia and Oceania":
        totalUnitsAO+=int(row[8])
        totalRevAO+=float(row[11])
    if row[0]=="Europe":
        totalUnitsE+=int(row[8])
        totalRevE+=float(row[11])
    if row[0]=="Asia":
        totalUnitsA+=int(row[8])
        totalRevA+=float(row[11])
    if row[0]=="Central America and the Caribbean":
        totalUnitsCA+=int(row[8])
        totalRevCA+=float(row[11])
    if row[0]=="North America":
        totalUnitsNA+=int(row[8])
        totalRevNA+=float(row[11])

    else:
        i+=1
        counter+=1
avgRevOnline=totalRevOnline/totalUnitsOnline
avgRevOffline=totalRevOffline/totalUnitsOffline
avgRev=totalRev/totalUnits
avgRevSA=totalRevSA/totalUnitsSA
avgRevME=totalRevME/totalUnitsME
avgRevAO=totalRevAO/totalUnitsAO
avgRevE=totalRevE/totalUnitsE
avgRevA=totalRevA/totalUnitsA
avgRevCA=totalRevCA/totalUnitsCA
avgRevNA=totalRevNA/totalUnitsNA




#Step 3 1. A list of sales channels
print ("list of Sales Channels:")
list = salesChannels.keys()
msg =""
for key in list:
    msg+=key + " "
print(msg)

#Step 3 2. Totals per sales channel
print("There were %d units sold offline." % (totalUnitsOffline))
print("The total revenue of units sold Offline is %.2f." % (totalRevOffline))
print("The average revenue of units sold Offline is %.2f." % (avgRevOffline))
print("There were %d units sold online." % (totalUnitsOnline))
print("The total revenue of units sold online is %f." % (totalRevOnline))
print("The average revenue of units sold Online is %.2f." % (avgRevOnline))

#Step 3 3. Big Totals are shown in the report produced by step 4

#Step 4
print ("\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tSales Report")
print ("\t\t\t\t\t\t\t\t\t\t\t------------")
print ("\t\t\t\t\t\t\t\t\t\tProduced on: ", end="")
print(date_object)
print ("\nRegions analysed: ", end="")
list = regionsAnalysed.keys()
msg =""
k=0
for key in list:
    if k==0:
        msg += key
    else:
        msg+=", " + key
    k += 1
print(msg)
print ("\nTotal, %d regions."%k)



print("\nSub-Saharan Africa\n")
print("\tTotal units sold:\t\t\t\t\t\t", end="")
print(f"{totalUnitsSA:,d}")
print("\tAverage revenue per unit:\t\t\t\t", end="")
print(f"${avgRevSA:,.2f}")
print("\tTotal revenue of sales:\t\t\t\t\t", end="")
print(f"${totalRevSA:,.2f}")

print("\nMiddle East and North Africa\n")
print("\tTotal units sold:\t\t\t\t\t\t", end="")
print(f"{totalUnitsME:,d}")
print("\tAverage revenue per unit:\t\t\t\t", end="")
print(f"${avgRevME:,.2f}")
print("\tTotal revenue of sales:\t\t\t\t\t", end="")
print(f"${totalRevME:,.2f}")

print("\nAustralia and Oceania\n")
print("\tTotal units sold:\t\t\t\t\t\t", end="")
print(f"{totalUnitsAO:,d}")
print("\tAverage revenue per unit:\t\t\t\t", end="")
print(f"${avgRevAO:,.2f}")
print("\tTotal revenue of sales:\t\t\t\t\t", end="")
print(f"${totalRevAO:,.2f}")

print("\nEurope\n")
print("\tTotal units sold:\t\t\t\t\t\t", end="")
print(f"{totalUnitsE:,d}")
print("\tAverage revenue per unit:\t\t\t\t", end="")
print(f"${avgRevE:,.2f}")
print("\tTotal revenue of sales:\t\t\t\t\t", end="")
print(f"${totalRevE:,.2f}")

print("\nAsia\n")
print("\tTotal units sold:\t\t\t\t\t\t", end="")
print(f"{totalUnitsA:,d}")
print("\tAverage revenue per unit:\t\t\t\t", end="")
print(f"${avgRevA:,.2f}")
print("\tTotal revenue of sales:\t\t\t\t\t", end="")
print(f"${totalRevA:,.2f}")

print("\nCentral America and the Caribbean\n")
print("\tTotal units sold:\t\t\t\t\t\t", end="")
print(f"{totalUnitsCA:,d}")
print("\tAverage revenue per unit:\t\t\t\t", end="")
print(f"${avgRevCA:,.2f}")
print("\tTotal revenue of sales:\t\t\t\t\t", end="")
print(f"${totalRevCA:,.2f}")

print("\nNorth America\n")
print("\tTotal units sold:\t\t\t\t\t\t", end="")
print(f"{totalUnitsNA:,d}")
print("\tAverage revenue per unit:\t\t\t\t", end="")
print(f"${avgRevNA:,.2f}")
print("\tTotal revenue of sales:\t\t\t\t\t", end="")
print(f"${totalRevNA:,.2f}")

print("\nGrand Totals\n")
print("\tTotal units sold:\t\t\t\t\t\t", end="")
print(f"{totalUnits:,d}")
print("\tAverage revenue per unit:\t\t\t\t", end="")
print(f"${avgRev:,.2f}")
print("\tTotal revenue of sales:\t\t\t\t\t", end="")
print(f"${totalRev:,.2f}")
#f"{totalRev:,}"
#format(totalRev, ",")

f.close()

