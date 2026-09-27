# ITE 260 - P2 Checkpoint

def avg(sc1, sc2, sc3):
    av = (sc1 + sc2 + sc3) / 3
    return av


ns = int(input("How many students? "))

while ns < 3:
    print("Need at least 3 students.")
    ns = int(input("How many students? "))


for st in range(1, ns + 1):

    print("\nStudent", st)

    nm = input("Name: ")
    sc1 = float(input("Act 1: "))
    sc2 = float(input("Act 2: "))
    sc3 = float(input("Act 3: "))

    av = avg(sc1, sc2, sc3)

    if av >= 90:
        stat = "Excellent"
    elif av >= 80:
        stat = "Very Good"
    elif av >= 75:
        stat = "Passed"
    else:
        stat = "Failed"

    print("\nResult")
    print("Name:", nm)
    print("Act 1:", sc1)
    print("Act 2:", sc2)
    print("Act 3:", sc3)
    print("Average:", round(av, 2))
    print("Status:", stat)