budget_data = r"/Users/saiyaraislam/Desktop/Starter_Code/PyBank/Resources/budget_data.csv"

count = 0 #initiating count as zero
total_sum = 0 #initiating sum as zero 
values_list = [] # empty list of values 
differences = [] #empty list of differences of values 
months = [] #empty lists of months 
with open(budget_data, 'r') as f: #opening file as variable "f"
    next(f)  # skipping header 
    for row in f: #forloop to calculate total number of months 
        count += 1

with open(budget_data, 'r') as f:  
    
    next(f)
    for line in f:
        columns = line.split(',')   #splitting columns on comma delimeter
        month = columns[0].strip()  #setting month = first column & removing empty spaces 
        months.append(month)  #appending indivudal months to the month list 
        total_sum += int(columns[1].strip()) #stripping and summing all values in column two
        value = columns[1].strip() # setting values = second column stripped 
        values_list.append(value)   #appending values to the value list 
    for i in range(len(values_list)-1): #forloop to calculate the differences between each values 
        difference = int(values_list[i+1]) - int(values_list[i])
        differences.append(difference)   #appending differences to differences list 
        max_diff = max(differences)    
        min_diff = min(differences)     
months2 = months[1:]    #setting months2 = a list of values except the first value in lists 

list_zip = zip(months2, differences)  #zipping together the months2 and differences lists 
zipped_list = list(list_zip)      

for (x,y) in zipped_list:     #forloop to find date at max diff 
    if y == max_diff:           
        max_diff_month = x
        
for (x,y) in zipped_list:    #forloop to find date at min diff 
    if y == min_diff:      
        min_diff_month = x
        
avg_change_sum = sum(differences)
avg_change = avg_change_sum / len(differences)

print('Financial Analysis')                #printing answers
print('------------------------------')    
print(f'Total Months: {count}')
print(f'Total Sum: ${total_sum}')
print(f'Average Change: ${avg_change:.2f}')
print(f'Greatest Increase in Profits: {max_diff_month} (${max_diff})')
print(f'Greatest Decrease in Profits: {min_diff_month} (${min_diff})')


with open('financial_analysis.txt', 'w') as f:   #opening txt file to write to 
    f.write('Financial Analysis\n\n')
    f.write('------------------------------\n\n')
    f.write(f'Total Months: {count}\n\n')
    f.write(f'Total Sum: ${total_sum}\n\n')
    f.write(f'Average Change: ${avg_change:.2f}\n\n')
    f.write(f'Greatest Increase in Profits: {max_diff_month} (${max_diff})\n\n')
    f.write(f'Greatest Decrease in Profits: {min_diff_month} (${min_diff})')

