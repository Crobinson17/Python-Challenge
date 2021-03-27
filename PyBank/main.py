import csv
import os

#Data Path
csvpath = os.path.join("Python_budget_data.csv")
csvpath_output = ("Python_budget_data.txt")

# Variables 
total_months = 0
total_profit_loss = 0

prev_profit_loss = 0
profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

profit_loss_changes = []

# Read Files
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)

    #Add up the total months and profit losses 
    for row in reader:

        
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
        print(row)

        # Keep track of changes
        profit_loss_change = int(row["Profit/Losses"]) - prev_profit_loss
        print(profit_loss_change)

        # Reset the value of prev_profit_loss to the complete row 
        prev_profit_loss = int(row["Profit/Losses"])
        print(prev_profit_loss)

        # Greatest increase
        if (profit_loss_change > greatest_increase[1]):
            greatest_increase[1] = profit_loss_change
            greatest_increase[0] = row["Date"]

        if (profit_loss_change < greatest_decrease[1]):
            greatest_decrease[1] = profit_loss_change
            greatest_decrease[0] = row["Date"]

        # Profit loss changes list
        profit_loss_changes.append(int(row["Profit/Losses"]))

    # Profit loss average
    profit_loss_avg = sum(profit_loss_changes) / len(profit_loss_changes)
    
    #Output
    print("Finacial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total : " + "$" + str(total_profit_loss))
    print("Average Change: " + "$" + str(round(sum(profit_loss_changes) / len(profit_loss_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    
    
    
    
