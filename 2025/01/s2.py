import math

with open('data.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    current = 50
    for line in lines:
        if line.strip():
            clicks=int(line[1:])
            newLocation = 0

            if line[0] == "L":
                newLocation = current - clicks
                if current != 0 and newLocation % 100  > current or newLocation % 100 == 0:
                    result += 1
            if line[0] == "R":
                newLocation = current + clicks
                if current != 0 and newLocation % 100 < current:
                    result += 1

            additionalTurns = clicks / 100
            result += math.ceil(additionalTurns)-1
 
            current = newLocation % 100
    print (result)
