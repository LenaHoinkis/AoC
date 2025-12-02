with open('data.txt', 'r') as file:
    result = 0
    line = file.readline()
    ranges = str(line).split(",")
    for r in ranges:
        boundries = [int(x) for x in str(r).split("-")]
        ids=list(range(boundries[0],boundries[1]+1))
        evens = [num for num in ids if int(len(str(num))) % 2 == 0]
        for e in evens:
            digits = list(str(e))
            h = int(len(digits)/2)
            if digits[:h] == digits[h:]:
                result += e

    print(result)

