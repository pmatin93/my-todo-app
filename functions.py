FILEPATH = 'FileBD.txt'

def get_user_input(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        motorcycle_list = file.readlines()
    return motorcycle_list

def update_list(motorcycle_list_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(motorcycle_list_arg)

def del_all():
    open(FILEPATH, "w").close()

if __name__ == "__main__":
    print("Test")