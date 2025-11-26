print("abhi")

with open("report.txt", "w") as f:
    f.write("This is a text file generated during Jenkins build.\n")
    f.write("Build successful!")

