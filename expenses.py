import csv


def read_expenses(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        total = 0
        cat = {}
        biggest = 0
        biggest_cat = ""
        for line_no, row in enumerate(reader, start=2):
            try:
                a = float(row["amount"])
            except ValueError:
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
    return cat, total, biggest, biggest_cat


def write_summary(cat, filename):
    with open(filename, "w", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["category", "total"])
        for category, amounts in cat.items():
            writer.writerow([category, sum(amounts)])

def main():
    cat, total, biggest, biggest_cat = read_expenses("expenses.csv")
    write_summary(cat, "summary.csv")
    print(total)
    print(cat)
    print("Biggest expense:", biggest, "in", biggest_cat)
if __name__ == "__main__":
    main()
#if __name__ == "__main__": means "run this only when I am the file being
#executed." If another file imports me, I just provide my functions.    

            
                
                
    

 



