with open('e1.txt', 'r') as file:
    result = 0
    line = file.readline()
    ranges = str(line).split(",")
    for r in ranges:
        boundries = [int(x) for x in str(r).split("-")]
        ids=list(range(boundries[0],boundries[1]+1))
        for e in ids:
            digits = list(str(e))
            l = int(len(digits))
            h = int(l/2)
            for i in range(h):
                substring = digits[:i+1] * (l//(i+1))
                if digits == substring:
                    result += e
                    break

    print(result)

