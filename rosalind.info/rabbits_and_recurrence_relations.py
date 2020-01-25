def rabbit_fibonacci(months, pairs):
    #start with the first two months already done
    rabbits = [1, 1]
    month = 2
    while month < months:
        #fibonacci sequence with slight modification for pairs
        new_rabbits = pairs*rabbits[month-2]+ rabbits[month-1]
        #add rabbits to list, move on to the next month
        rabbits.append(new_rabbits)
        month += 1
    print(rabbits[months-1])
    

 
        