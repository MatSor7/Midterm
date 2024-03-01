def find_b_bob(filename):
    """
    Find patterns of any number of letters, starting with b and ending with Bob
    :param filename: Name of the file
    :return: Number of matches
    """
    punctuation = ",!?.\n"
    # open the file
    with open(filename, "r") as file:
        # go over the file line by line
        for line in file:
            # get the patterns
            patterns = pattern.startswith("b") and pattern.endswith("Bob")
            for pattern in patterns:
                if pattern.startswith("b") and pattern.endswith("Bob"):
                    print(pattern)
    return


find_b_bob('b_Bob')
