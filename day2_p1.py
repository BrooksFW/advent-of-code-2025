if __name__ == "__main__":

    # Read in the ranges (day_2_input.txt) as a list of commands
    with open("P:\\gitrepos\\advent2025\\input\\day_2_input.txt", "r") as file:
        ranges = file.read().split(",")
        for i in range(len(ranges)):
            ranges[i] = ranges[i].split("-")

    # test ranges
    # ranges = [[11, 22],
    #         [95, 115],
    #         [998, 1012],
    #         [1188511880, 1188511890],
    #         [222220, 222224],
    #         [1698522, 1698528],
    #         [446443, 446449],
    #         [38593856, 38593862]]

    # Iterate through the ranges to find invalid ids
    invalid_ids = []
    for ids in ranges:
        for id in range(int(ids[0]), int(ids[1])+1):

            # Stringify the id for slicing
            s_id = str(id)

            # Check if the id length is even (can be split in two equal chunks)
            odd = len(s_id) % 2
            if not odd:
                # Split the id in half
                half = int(len(s_id)/2)
                first, second = s_id[0:half], s_id[half:]

                # Check if the halves equal each other
                if first == second:
                    invalid_ids.append(int(id))

    # Sum the invalid ids
    sum = 0
    for id in invalid_ids:
        sum += id

    print(sum)