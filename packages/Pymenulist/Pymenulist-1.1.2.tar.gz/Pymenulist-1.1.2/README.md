# start menu list

import Pymenulist
def print_blue():
    print("blue")
def print_red():
    print("red")


menulist = [["1", "print blue", print_blue], ["2", "print red", print_red]]
#["index menu", "name menu", object func]
Pymenulist.start_menu_list(menulist)

