# Day 23 - View Saved Results

print("=== View Saved Student Results ===")

try:
    file = open("result.txt", "r")
    content = file.read()

    if content:
        print("\n--- Saved Results ---")
        print(content)
    else:
        print("No results found.")

    file.close()

except FileNotFoundError:
    print("No result file found. Please run Day 22 program first.")
