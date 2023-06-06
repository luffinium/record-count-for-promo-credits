recordCount = 0
cord = []
recordsList = open(
    "IT244_U5_Data.txt"
    )
for line in recordsList :
        cord.append(line.strip("\n"))
recordsList.close()
cord.append(
    "5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA"
    )
excelFile = open(
    "IT244_U5_PromoCredit.csv","w"
    )
excelFile.write(
    "Customer ID, Last Name, First Name, Address, City, State, Promo Credit \n"
    )
for x in cord:
    x += ",$500\n"
    excelFile.write(x)
    recordCount += 1
excelFile.close()
print(
    "There were", recordCount, "records written to the promo credits csv file."
    )