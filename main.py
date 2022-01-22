from jump import Jump

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sj = Jump("D:/Avunte SUPER Jump/AvunteSJ.csv", 0)
    sj.plot_force()

    cmj = Jump("D:/Avunte SUPER Jump/AvunteCMJ.csv", 1)
    cmj.plot_force()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
