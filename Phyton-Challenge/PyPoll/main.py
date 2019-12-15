import os
import csv
 
count = 0
candidate = []
solo = []
vote = []
percent = []

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        count = count + 1
        candidate.append(row[2])

    for d in set(candidate):
        solo.append(d)
        w = candidate.count(d)
        vote.append(w)
        v = round((w/count)*100, 2)
        percent.append(v)
        
    winning_vote_count = max(vote)
    winner = solo[vote.index(winning_vote_count)]

print("Election Results")  
print("----------------") 
print("Total Votes :" + str(count))    
print("----------------")
for i in range(len(solo)):
            print(solo[i] + ": " + str(percent[i]) +"% (" + str(vote[i])+ ")")
print("-----------------")
print("The winner is: " + winner)

# Dear TA - The text file creation kept erroring out