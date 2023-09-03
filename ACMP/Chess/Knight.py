start = input().split(' ')
end = input().split(' ')

possible_positions = [[], [], [], [], [], [], [], [], []]

possible_positions[0].append(int(start[0]) + 2)
possible_positions[0].append(int(start[1]) + 1)

possible_positions[1].append(int(start[0]) + 1)
possible_positions[1].append(int(start[1]) + 2)

possible_positions[2].append(int(start[0]) - 1)
possible_positions[2].append(int(start[1]) - 2)

possible_positions[3].append(int(start[0]) - 2)
possible_positions[3].append(int(start[1]) - 1)

possible_positions[4].append(int(start[0]) - 2)
possible_positions[4].append(int(start[1]) + 1)

possible_positions[5].append(int(start[0]) - 1)
possible_positions[5].append(int(start[1]) + 2)

possible_positions[6].append(int(start[0]) + 1)
possible_positions[6].append(int(start[1]) - 2)

possible_positions[7].append(int(start[0]) + 2)
possible_positions[7].append(int(start[1]) - 1)

i = 0
while i < 8:
    if possible_positions[i][0] == int(end[0]) and possible_positions[i][1] == int(end[1]):
        print("YES")
        break
    i += 1
if i == 8:  
    print("NO")
