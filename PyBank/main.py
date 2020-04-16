import os
import csv

bdpath = os.path.join("Resources", "Budget_Data.csv")

with open(bdpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    next(csvreader)

    Months=0
    MonthMax=0
    MonthMin=0
    BudgetList=[]

    for row in csvreader:
        BudgetList.append(int(row[1]))
        Months+=1
        Total = sum(BudgetList)
        Avg = round (sum(BudgetList) / len(BudgetList))
        Max = max(BudgetList)
        Min = min(BudgetList)

    for row in csvreader:
        if Max(BudgetList)==row[1]:
            MonthMax==row[0]
        if Max(BudgetList)==row[1]:
            MonthMin==row[0]

analysis = os.path.join("Analysis", "analysis.txt")
with open(analysis,'w') as text_file:        
    print("Financial Analysis",file=text_file)
    print("---------------------------------------------",file=text_file)
    print(f"Total Months: {Months}",file=text_file)
    print(f"Total: ${Total}",file=text_file)
    print(f"Average Change: ${Avg}",file=text_file)
    print(f"Greatest increase in profits: ${Max} {MonthMax}",file=text_file)
    print(f"Greatest decrease in losses: ${Min} {MonthMin}",file=text_file)
    print("---------------------------------------------",file=text_file)