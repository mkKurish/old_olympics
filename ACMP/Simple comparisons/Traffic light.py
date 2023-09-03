frst = input()
scnd = input()
thrd = input()
if thrd == "green":
    if frst == "black" and scnd == "black":
        print(f"black\nblack\nGREEN")
    else:
        print("error")
elif thrd == "GREEN":
    if frst == "black" and scnd == "black":
        print(f"black\nyellow\nblack")
    else:
        print("error")
elif thrd == "black":
    if frst == "black" and scnd == "yellow":
        print(f"red\nblack\nblack")
    elif frst == "red" and scnd == "black":
        print(f"red\nyellow\nblack")
    elif frst == "red" and scnd == "yellow":
        print(f"black\nblack\ngreen")
    elif frst == "black" and scnd == "YELLOW":
        print(f"black\nYELLOW\nblack")
    else:
        print("error")
else:
    print("error")
