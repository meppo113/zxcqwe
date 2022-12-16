with open("config_sw1.txt", "r+") as f:
    for line in f:
        if "!" in line:
            continue
        else:
            print(line, end="")