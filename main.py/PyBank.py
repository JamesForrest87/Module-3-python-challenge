#Import dependencies
import csv
import pandas as pd

#Upload CSV file and output file
file_to_load = "c:/Users/llman/Downloads/Starter_Code (26)/Starter_Code/PyBank/Resources/budget_data.csv"
file_to_output = "Starter_Code/PyBank/Resources/PyBank_Analysis.txt"

#Revenue ranges
total_months = 0
prev_revenue = 0
revenue_change = []
revenue_change_list = []
profit_increase = ["",0]
profit_decrease = ["", 999999999999]
total_revenue = 0

#Read CSV and convert into a list of dictionaries
with open(file_to_load) as budget_data:
    reader = csv.DictReader(budget_data)

    for row in reader:
        #Totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        #Revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        # month_of_change = month_of_change + [row["Date"]]

        #Calculate profit increase
        if revenue_change > profit_increase[1]:
            profit_increase[0] = row["Date"]
            profit_increase[1] = revenue_change

        #Calculate profit decrease
        if revenue_change < profit_decrease[1]:
            profit_decrease[0] = row["Date"]
            profit_decrease[1] = revenue_change

#Calculate avg revenue change
revenue_avg = round(sum(revenue_change_list) / len(revenue_change_list),2)


#Print output
output = (
    f"\nFinancial Analysis\n"
    f"\n--------------------\n"
    f"\nTotal Months: {total_months}\n"
    f"\nTotal: ${total_revenue}\n"
    f"\nAverage Change: ${revenue_avg}\n"
    f"\nGreatest Increase in Profits: {profit_increase[0]} (${profit_increase[1]})\n"
    f"\nGreatest Decrease in Profits: {profit_decrease[0]} (${profit_decrease[1]})\n"
    )
#Print output
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)