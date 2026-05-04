def main():
    print("ET0735 (DevOps for AIoT) - Lab2 - Introduction to ")
    display_main_menu()
    num_list=get_user_input()
    calc_average(num_list)
    calc_maxandmin(num_list)
    calc_median(num_list)




def display_main_menu():
    print("Enter some number separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input=input()

    string_list= user_input.split(",")

    float_list=[]

    for num_str in string_list:
        float_list.append(float(num_str))

    return float_list


def calc_average(float_list):
    list_length = len(float_list)
    avg=sum(float_list)/list_length
    print(f"the average temperature of reading is {avg}")

def calc_maxandmin(float_list):
    max_number=max(float_list)
    min_number=min(float_list)
    print(f"the max number is {max_number}")
    print(f"the min number is {min_number}")


def calc_median(float_list):
    sorted_list = sorted(float_list)
    list_length = len(sorted_list)

    if list_length % 2 == 0:
        mid1 = sorted_list[list_length // 2 - 1]   
        mid2 = sorted_list[list_length // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_list[list_length // 2]
    print(f"the median is {median}")


if _name_ == "_main_":
  main()