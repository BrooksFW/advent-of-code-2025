if __name__ == "__main__":

    total = 0

    # Read in the battery lines line-by-line (memory efficient)
    # with open("P:\\gitrepos\\advent2025\\input\\day_3_input_test.txt", "r") as file:
    with open("P:\\gitrepos\\advent2025\\input\\day_3_input.txt", "r") as file:
        line = file.readline()
        while line:
            max_value = -1
            for i in range(len(line)-1):
                for j in range(i+1, len(line)-1):
                    if int(f"{line[i]}{line[j]}") > max_value:
                        max_value = int(f"{line[i]}{line[j]}")
            
            # Add the max_value from the current line
            # print(max_value)
            total += max_value

            # Move to next line
            line = file.readline()
    
    # Output total
    print(total)