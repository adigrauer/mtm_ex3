# Test for the 1st part of HW3 in mtm (2022a)
# Written by Uri Sivani

from hw3_part1 import *

TESTS_NUM = 6

class static_vars:
    first_fun_cnt = 1
    second_fun_cnt = 1
    natural_num = 1

def test(fun_num, k=0):

    if k < 0:
        k = 0

    passed = 0

    if fun_num == 1:
        input_file_name = "./hw3_part1--TEST-FILES/inputs/" + str(static_vars.first_fun_cnt) + ".txt"
        output_file = open("./hw3_part1--TEST-FILES/outputs/best/" + str(static_vars.first_fun_cnt) + ".txt", "r")
        output = output_file.readlines()[0]
        output_file.close()
        user_output = find_best_selling_product(input_file_name)
        cnt = static_vars.first_fun_cnt
        static_vars.first_fun_cnt += 1

    if fun_num == 2:
        input_file_name = "./hw3_part1--TEST-FILES/inputs/" + str(static_vars.second_fun_cnt) + ".txt"
        output_file = open("./hw3_part1--TEST-FILES/outputs/most/" + str(static_vars.second_fun_cnt) + ".txt", "r")
        temp = output_file.readlines()
        if len(temp) > k:
            output = temp[k]
        else:
            output = temp[len(temp)-1]
        output_file.close()
        user_output = find_k_most_expensive_products(input_file_name, k)
        cnt = static_vars.natural_num
        static_vars.second_fun_cnt += 1
        static_vars.natural_num += 1

    if output.replace("\n", "") == str(user_output):
        passed = 1

    if passed == 0:
        input_file = open(input_file_name, "r")
        input_lines = input_file. readlines()
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Test Num." + str(cnt) + " Failed")
        print("Input:")
        for i in range(0, len(input_lines)):
            print("\t" + input_lines[i].replace("\n", ""))
        input_file.close()
        print("\nExcepted Output:\n\t" + output)
        print("Your Output:\n\t" + str(user_output))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

    else:
        print("Test Num." + str(cnt) + " Passed")

print("\n---------Best-Selling-Func-Test-Results--------\n")
for i in range(0, TESTS_NUM):
    test(1)

print("\n----------Most-Expensive-Test-Results----------\n")
for j in range(-1, 7):
    for i in range(0, TESTS_NUM):
        test(2, j)
    static_vars.second_fun_cnt = 1
