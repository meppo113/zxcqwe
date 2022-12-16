def parse_cdp_neighbors(n):
    with open("C:\\Users\\ks121horoshaev\\Desktop\\sh_cdp_n_sw1.txt") as file:
        with open("C:\\Users\\ks121horoshaev\\Desktop\\sh_cdp_n_r1.txt") as file:
            with open("C:\\Users\\ks121horoshaev\\Desktop\\sh_cdp_n_r2.txt") as file:
                with open("C:\\Users\\ks121horoshaev\\Desktop\\sh_cdp_n_r3.txt") as file:
                    n = file.read()
                    q = {}
                    q1= {}
                    q2= {}
                    q3 = {}
                    n = n.split('\n')
        for line in n:
            main = []
            second = []
            if line.find('>') != -1:
                main_machine = line[:line.find('>')]
            elif line.find('Eth') != -1:
                second_machine, main_eth, main_inter, *other, second_eth, second_inter = line.split()
                main.append(main_machine)
                second.append(second_machine)
                main_interface = main_eth + main_inter
                second_interface = second_eth + second_inter
                main.append(main_interface)
                second.append(second_interface)
                main_tuple = tuple(main)
                second_tuple = tuple(second)
                q[main_tuple] = second_tuple
    return q
if __name__ == "__main__":
    q = parse_cdp_neighbors("sh_cdp_n_sw1.txt")
    q1 = parse_cdp_neighbors("sh_cdp_n_r1.txt")
    q2 = parse_cdp_neighbors("sh_cdp_n_r2.txt")
    q3 = parse_cdp_neighbors("sh_cdp_n_r3.txt")
    print(q,q1,q2,q3)
   
