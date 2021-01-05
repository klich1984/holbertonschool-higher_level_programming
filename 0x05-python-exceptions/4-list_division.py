#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    idx = 0

    while idx < list_length:
        try:
            new_list.append(my_list_1[idx]/my_list_2[idx])
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            pass
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            idx += 1
    return new_list
