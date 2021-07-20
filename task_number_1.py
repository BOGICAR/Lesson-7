# Задание №1 - сделано
def task_7_1(funk):
    def in_list(*args, **kwags):
        split_ = funk(*args, **kwags)
        split_ = split_.split()
        return split_
    return in_list


@task_7_1
def user_input():
    u_input = input('Enter some text: ')
    return u_input


print(user_input())
