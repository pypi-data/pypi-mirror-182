# py command handler Pycomm 1.0.0
import colorama as col
import pickle as pic
#command input = yes
def cominp(simvol, inpu):
    if simvol == None or simvol == "" or simvol == " ":  #filter bad simvols
        com = input((inpu))
        a = [""]
        n = 0
        for i in com:
            if i != ":":
                a[n] += str(i)
            elif i == ":":
                a.append("")
                n += 1
    else:                       #if not bad simvols
        simvol = str(simvol)
        com = input(str(inpu))
        a = [""]
        n = 0
        for i in com:
            if i != simvol:
                a[n] += str(i)
            elif i == simvol:
                a.append("")
                n += 1
    return a
#input = no
def com(com, simvol=" "):
    if simvol == None or simvol == "":
        a = [""]
        n = 0
        for i in com:
            if i != ":":
                a[n] += str(i)
            elif i == ":":
                a.append("")
                n += 1
    else:
        simvol = str(simvol)
        a = [""]
        n = 0
        for i in com:
            if i != simvol:
                a[n] += str(i)
            elif i == simvol:
                a.append("")
                n += 1
    return a
def start_menu_list(arg):
    b = []
    if type(arg) == list:
        s = 0
        b = [[[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]]]
        st = True
        i = [[],[],[]]
        i = arg
        for r in i:
            print(f"{i[s][0]}.{i[s][1]}")
            g = [i[s][0], i[s][2]]
            b[s] = g
            s += 1
        nres = []
        fin = input("[?]:")
        s = 0
        st = True
        while st == True:
            nres = b[s][0]
            if fin == nres:
                ss = b[s][1]
                ss()
                st = False
            elif fin != nres and s + 1 == len(b):
                fin = input("[?]:")
                s = 0
                st = True
            else:
                s += 1
    else:
        print(f"{col.Fore.RED}{arg} not a list")

if __name__ == "__main__":

    #input = yes

    a = cominp(":", "lol:")
    if a[0] == "l":
        print(a[1])
        print(a[2])
    else:
        print(f"{col.Fore.RED}error not command{col.Style.RESET_ALL}")

    #command input = no

    b = com("l:b:h", ":")
    if b[0] == "l":
        print(b[1])
        print(b[2])
    else:
        print(f"{col.Fore.RED}error not command{col.Style.RESET_ALL}")