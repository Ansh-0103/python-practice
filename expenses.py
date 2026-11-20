import csv

with open("expenses.csv") as f:
    reader = csv.DictReader(f)
    total = 0
    cat = {}
    biggest = 0
    biggest_cat = ""
    for line_no, row in enumerate(reader, start=2):
        try:
            a = float(row["amount"])
        except(ValueError):
            print("Skipping line", line_no, "- bad amount:", row)
            continue    
        c = row["category"]
        total += a
        if c in cat:
            cat[c] += [a]
        else:
            cat[c] = [a]
        if a > biggest:
            biggest = a
            biggest_cat = c
    #writing summary to another file using writer
with open("summary.csv", "w", newline="") as out:    
    writer=csv.writer(out)
    writer.writerow(["category", "total"])
    for category,amount in cat.items():
        writer.writerow([category,sum(amount)])        

print(total)
print(cat)
print("Biggest expense:", biggest, "in", biggest_cat)

