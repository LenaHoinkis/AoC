with open('e1.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    currentRotation = 50
    for line in lines:
        if line.strip():
            clicks=int(line[1:]) % 100
            if line[0] == "L":
                currentRotation -= clicks
            if line[0] == "R":
                currentRotation += clicks
            if currentRotation < 0:
                currentRotation= 100 + currentRotation 
            elif currentRotation >= 100:
                currentRotation = currentRotation % 100
            if currentRotation == 0:
                result +=1
    print (result)
