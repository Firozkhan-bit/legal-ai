import json
case = {
    "case name": "Revolutionary Army vs World Government",
    "case id": "BA345KL0934",
    "year": 2006,
    "verdict": "not innocent",
    "judges": ["Judge Karasu", "Judge Katakuri"]
}
while True:
    ch = int(input("Menu:\n1. View Case\n2. Edit Case\n3. Update Case to JSON\n4. Exit\n"))
    if ch == 1:
        cha = int(input("1. View All\n2. View Specific Detail\n"))
        if cha == 1:
            print("Case Name:", case["case name"])
            print("Case ID:", case["case id"])
            print("Year:", case["year"])
            print("Verdict:", case["verdict"])
            print("Judges:", ", ".join(case["judges"]))
        elif cha == 2:
            detail = input("Enter detail :")
            if detail.lower() in case:
                print(detail, ":", case[detail])
            else:
                print("Detail not found.")
        else:
            print("Invalid choice.")
    elif ch == 2:
        detail = input("Enter detail to edit :")
        if detail.lower() in case:
            if(detail.lower() == "year"):
                new = int(input("Change " + str(case[detail]) + " to :"))
            elif(detail.lower() == "judges"):
                chb = int(input("1. Add Judge\n2. Remove Judge\n3. Change Judges\n"))
                if chb == 1:
                    judge = input("Enter judge name to add: ")
                    case[detail.lower()].append(judge)
                elif chb == 2:
                    judge = input("Enter judge name to remove: ")
                    if judge in case[detail.lower()]:
                        case[detail.lower()].remove(judge)
                    else:
                        print("Judge not found.")
                elif chb == 3:
                    new_judges = input("Enter new judges (comma-separated): ").split(",")
                    case[detail.lower()] = [judge.strip() for judge in new_judges]
            else:
                new = input("Change " + case[detail] + " to :")
                case[detail.lower()] = new
                print("Detail updated.")
        else:
            print("Detail not found.")
    elif ch == 3:
        j = json.dumps(case)
        with open('case.json','w') as f:
            f.write(j)
        print("Case updated.")
    elif ch == 4:
        print("Exiting...")
        exit()
    else:
        print("Invalid choice.")
