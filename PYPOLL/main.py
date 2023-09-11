election_data = r"/Users/saiyaraislam/Desktop/Starter_Code/PyPoll/Resources/election_data.csv"

count = 0  #setting count to zero
unique_candidates = set() #setting unique candidates to an empty set 
count_c = 0   #setting count of candidate votes to 0
count_r = 0   #setting count of second candidate to 0
count_d = 0   #setting count of third candidate to 0

with open(election_data, "r") as f:  #opening election data file as f 
    next(f)  #skipping header 
    for line in f:    #using forloop to find unqiue candidates 
        count += 1    
        columns = line.split(',')
        cand = columns[2].strip()
        unique_candidates.add(cand)

uniq_cand_lst = list(unique_candidates)   #creating a variable that sets unique candidates to list 
with open(election_data, "r") as f:       
    next(f)  
    for line in f:                        #using a forloop to count how many votes each candidate recieved 
        columns = line.split(',')
        cand = columns[2].strip()
        if cand == uniq_cand_lst[0]:
            count_c +=1
        elif cand == uniq_cand_lst[1]:
            count_r +=1
        elif cand == uniq_cand_lst[2]:
            count_d +=1

percentage_c = (count_c/count)*100       #calculating the percentage of votes each candidates recieved 
cd1p = (f"{percentage_c:.3f}%") 
percentage_r = (count_r/count)*100
cd2p = (f"{percentage_r:.3f}%") 
percentage_d = (count_d/count)*100
cd3p = (f"{percentage_d:.3f}%") 

total = count                          
un_cd = list(unique_candidates)
cd1 = count_c
cd1pp = cd1p
cd2 = count_r
cd2pp = cd2p
cd3 = count_d
cd3pp = cd3p

if cd1 > cd2 and cd1 > cd3:           #using an if statement to find out the winner 
    winner = un_cd[0]
elif cd2 > cd1 and cd2 > cd3:
    winner = un_cd[1]
elif cd3 > cd1 and cd3 > cd2:
    winner = un_cd[2]
    
print('Election Results')             #printing all answers 
print('--------------------')
print(f'Total Votes: {total}')
print(f'{un_cd[0]}: {cd1pp} ({cd1})')
print(f'{un_cd[1]}: {cd2pp} ({cd2})')
print(f'{un_cd[2]}: {cd3pp} ({cd3})')
print(f'Winner: {winner}')




with open('election_results.txt', 'w') as f:     #opening txt file as f to write all the answers to 
    f.write('Election Results\n\n')
    f.write('--------------------\n\n')
    f.write(f'Total Votes: {total}\n\n')
    f.write('--------------------\n\n')
    f.write(f'{un_cd[0]}: {cd1pp} ({cd1})\n\n')
    f.write(f'{un_cd[1]}: {cd2pp} ({cd2})\n\n')
    f.write(f'{un_cd[2]}: {cd3pp} ({cd3})\n\n')
    f.write('--------------------\n\n')
    f.write(f'Winner: {winner}\n\n')
    f.write('--------------------\n')

