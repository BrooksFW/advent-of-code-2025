from itertools import groupby

def splitId(id, pattern_size):
    """
    Docstring for splitId
    
    :str id: string that needs to be split into "pattern_size" amounts 
    :int pattern_size: amount of chunks needed of id
    """
    split_id = []

    num_items = len(id) / pattern_size
    i = 0
    while i < num_items:
        split_id.append(id[:pattern_size])
        id = id[pattern_size:]
        i += 1
    return split_id

def allEqual(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

if __name__ == "__main__":

    # Read in the ranges (day_2_input.txt) as a list of commands
    with open("P:\\gitrepos\\advent2025\\input\\day_2_input.txt", "r") as file:
        ranges = file.read().split(",")
        for i in range(len(ranges)):
            ranges[i] = ranges[i].split("-")

    # test ranges
    # ranges = [[11, 22],                   #11 and 22
    #         [95, 115],                    #99 and 111
    #         [998, 1012],                  #999 and 1010
    #         [1188511880, 1188511890],     #1188511885
    #         [222220, 222224],             #222222
    #         [1698522, 1698528],           #None
    #         [446443, 446449],             #446446
    #         [38593856, 38593862],         #38593859
    #         [565653, 565659],             #565656
    #         [824824821, 824824827],       #824824824
    #         [2121212118, 2121212124]]     #2121212121

    # Iterate through the ranges to find invalid ids
    invalid_ids = []
    for ids in ranges:
        for id in range(int(ids[0]), int(ids[1])+1):

            # Stringify the id for slicing
            s_id = str(id)

            # iterate up to (length floored 2)
            for pattern_size in range(len(s_id) // 2):
                
                # try to split the id
                split_id = splitId(s_id, pattern_size+1)
                
                # If all items equal, add it and break
                if allEqual(split_id):
                    invalid_ids.append(int(id))
                    break

    # Sum the invalid ids
    sum = 0
    for id in invalid_ids:
        sum += id
    print(sum)

