def input_bug_counts(bug_type):
    return int(input(f"Enter the count of {bug_type} bugs: "))
    

def calculate_percent(total, count):
    return count/total 

def input_bug_type_and_count():
    bug_type = input("Enter the type of bug: ")
    count = input_bug_counts(bug_type)
    return bug_type, count

def display_table(bug1, count1, bug2, count2, bug3, count3):
    total = count1 + count2 + count3
    print()
    print(f"{'Bug Type':<20}{'Count':>5}{'Percentage':>15}")
    print("="*40)
    print(f"{bug1:<20}{count1:>5}{calculate_percent(total, count1):>15.2%}")
    print(f"{bug2:<20}{count2:>5}{calculate_percent(total, count2):>15.2%}")
    print(f"{bug3:<20}{count3:>5}{calculate_percent(total, count3):>15.2%}")
    print("="*40)
    print(f"{'Total':<20}{total:>5}{total/total:>15.2%}")

bug1, count1 = input_bug_type_and_count()
bug2, count2 = input_bug_type_and_count()
bug3, count3 = input_bug_type_and_count()

display_table(bug1, count1, bug2, count2, bug3, count3)


