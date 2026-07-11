data = True
line = 1
word = "python"
with open ("sample.txt", "r") as f:
    while data:
        data = f.readline() 
        if(word in data):
            print(f"{word} found at line no {line}")
            break
        line += 1
 