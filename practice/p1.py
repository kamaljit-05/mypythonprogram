# Print the pattern: *, **, *
pattern = ["*", "**", "*"]

for line in pattern:
    print(line)


'''
OR


# Generate the same pattern dynamically
rows = [1, 2, 1]  # number of stars in each row

for r in rows:
    print("*" * r)
