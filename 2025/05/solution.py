with open('data.txt', 'r') as file:
    
    #parse
    block = file.read().strip().split("\n\n")
    ranges =[list(map(int, item.split("-"))) for item in block[0].split("\n")]
    ids = [int(x) for x in block[1].split("\n")]

    def reduceOverlaps(ranges):
        fresh = []
        found_overlap = False
        for r in ranges:
            overlap = False
            for f in fresh:
                if f[0] <= r[0] <=f[1]:
                    f[1] = max(r[1],f[1])
                    overlap = True
                if f[0] <= r[1] <= f[1]:
                    f[0] = min(r[0],f[0])
                    overlap = True
                if r[0] <= f[0] and r[1] >= f[1]:
                    f[0] = r[0]
                    f[1] = r[1]
                    overlap = True
            if not overlap:
              fresh.append([r[0], r[1]])
            else:
                found_overlap = True  
        return found_overlap, fresh

    found = True
    while found:
        found, ranges = reduceOverlaps(ranges)
    print(ranges)

    #part1
    result=0
    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                result+=1
    print(result)

    #part2
    result=0
    for r in ranges:
        result+=len(range(r[0],r[1]+1))
    print(result)

