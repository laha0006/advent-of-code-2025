data = open("input.txt", "r")

lines = [line.strip() for line in data]
ins = [(line[0],int(line[1::])) for line in lines]

count = 0
dial = 50

def turn_dial(instruction):
    global dial
    global count
    dir = instruction[0]
    rotation = instruction[1]
    if dir == "L":
        turn = dial - rotation
        dial = turn % 100
    elif dir == "R":
        turn = dial + rotation
        dial = turn % 100
    if dial == 0:
        count += 1

for i in ins:
     turn_dial(i)
print(count)

