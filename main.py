for ctr1 in range(7):
    for ctr2 in range(5):
        if (ctr2 == 0 or ctr2 == 4) or ((ctr1 == 0 or ctr1 == 3) and (0 < ctr2 < 4)):
            print("*", end="")
        else:
            print(end=" ")
    print()

