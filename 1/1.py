data = open("input.txt", "r")
#data = open("test.txt", "r")

lines = [line.strip() for line in data]
ins = [(line[0],int(line[1::])) for line in lines]


def turn_dial(instruction):
    global dial
    global count
    global part_two_count
    zero = 0
    dir = instruction[0]
    rotation = instruction[1]
    if dir == "L":
        turn = dial - rotation
        if dial == 0:
            zero_rota = rotation 
        else:
            zero_rota = rotation + (100 - dial) 
        dial = turn % 100
        zero = abs(zero_rota // 100)    
    elif dir == "R":
        turn = dial + rotation
        dial = turn % 100
        zero = turn // 100
    if dial == 0:  
        count += 1
    part_two_count += zero




dial = 50
count = 0
part_two_count = 0

for i in ins:
    turn_dial(i)

print("p1:",count)
print("p2:",part_two_count)
