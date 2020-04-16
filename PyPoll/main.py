import os
import csv

edpath = os.path.join("Resources", "Election_Data.csv")

with open(edpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    Total = 0
    TotalK = 0
    TotalC = 0
    TotalL = 0
    TotalO = 0

    for row in csvreader:
        ElectionList=str(row[2])
        Total+=1
        if ElectionList=="Khan":
            TotalK += 1
        elif ElectionList=="Correy":
            TotalC += 1
        elif ElectionList=="Li":
            TotalL += 1
        elif ElectionList=="O'Tooley":
            TotalO += 1

    if TotalK > TotalC and TotalL and TotalO:
        Winner = "Khan"
    elif TotalC > TotalK and TotalL and TotalO:
        Winner = "Correy"
    elif TotalL > TotalK and TotalC and TotalO:
        Winner = "Li"
    elif TotalO > TotalK and TotalC and TotalL:
        Winner = "O'Tooley"

    analysis = os.path.join("Analysis", "analysis.txt")

    with open(analysis,'w') as text_file:
            print("Election Results",file=text_file)    
            print("------------------------------------",file=text_file)        
            print(f"Total Votes: {Total}",file=text_file)
            print("------------------------------------",file=text_file)
            print(f"Total Votes Khan: {TotalK} ({round(TotalK/Total*100,1)})%",file=text_file)
            print(f"Total Votes Correy: {TotalC} ({round(TotalC/Total*100,1)})%",file=text_file)  
            print(f"Total Votes Li: {TotalL} ({round(TotalL/Total*100,1)})%",file=text_file)
            print(f"Total Votes O'Tooley: {TotalO} ({round(TotalO/Total*100,1)})%",file=text_file)
            print("------------------------------------",file=text_file)
            print(f"Winner: {Winner}",file=text_file)




