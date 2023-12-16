from string_correct import string_correction
import time


while True:
    lines = []
    while True:
        line = input("Enter a string (type 'exit' to quit, 'r' to run): ")
        if line.lower() == "exit":
            exit()
        elif line.lower() == "r":
            break
        else:
            lines.append(line)

    for line in lines:
        start_time = time.time()
        print(string_correction(line))
        end_time = time.time()
        execution_time = end_time-start_time
        print(execution_time)
