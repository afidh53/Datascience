def total_marks(m1, m2, m3,):
    return m1 + m2 + m3

def percentage(total):
    return (total / 150) * 100

def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"


m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))
total = total_marks(m1, m2, m3,)
per = percentage(total)
g = grade(per)

#result
print("\nTotal Marks =", total)
print("Percentage =", per)
print("Grade =", g)