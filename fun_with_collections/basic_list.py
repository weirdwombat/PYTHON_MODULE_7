def make_list():
    user_list = []
    if len(user_list) < 4:
        get_input()
    else:
        print(user_list)
    return user_list


def get_input():
    for user_input in string:
        if user_input.isnumeric():
            int(user_input)
            user_list.append(user_input)
        else:
            print("Input is invalid, please try again")
            make_list()


if __name__ == '__main__':
    make_list()
