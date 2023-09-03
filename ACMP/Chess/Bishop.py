start = input().split(' ')
end = input().split(' ')
diff = int(start[0]) - int(end[0])
if int(start[1]) + diff == int(end[1]) or int(start[1]) - diff == int(end[1]):
    print("YES")
else:
    print("NO")
    
