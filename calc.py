from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


clear()

main_logo = '''
                   _________    __    ________  ____    ___  __________  ____
                  / ____/   |  / /   / ____/ / / / /   /   |/_  __/ __ \/ __ \\
                 / /   / /| | / /   / /   / / / / /   / /| | / / / / / / /_/ /
                / /___/ ___ |/ /___/ /___/ /_/ / /___/ ___ |/ / / /_/ / _, _/
                \____/_/  |_/_____/\____/\____/_____/_/  |_/_/  \____/_/ |_
                                                                     v 1.0
                                    author: Mahid alam
==================================================================================================

'''
print(main_logo)
user_select_number = input(
    '\n\n\tType\n\n[1] Plus\n[2] Minus\n[3] Division\n[4] Multiplication\n[5] Exponentiation\n: ')
collecting_user_first_vlue = int(input('Type first value ==> '))
collecting_user_last_vlue = int(input('Type last value ==> '))

doing_plus = collecting_user_first_vlue + collecting_user_last_vlue
doing_minus = collecting_user_first_vlue - collecting_user_last_vlue
doing_simple_division = collecting_user_first_vlue / collecting_user_last_vlue
# This is for how many time's it goes in the value atlast
doing_atlast_division_point = collecting_user_first_vlue // collecting_user_last_vlue
# This is for what value is remine after multipication go
doing_final_number_after_division = collecting_user_first_vlue % collecting_user_last_vlue
doing_multiplication = collecting_user_first_vlue * collecting_user_last_vlue
doing_exponentiation = collecting_user_first_vlue ** collecting_user_last_vlue
doing_give_prof = doing_atlast_division_point * collecting_user_last_vlue
doing_give_prof_2nd = collecting_user_first_vlue - doing_give_prof
if_in_division = f'[ {collecting_user_first_vlue} ] can\'t be divide with [ {collecting_user_last_vlue} ]\nAt lest this division can go to [ {doing_atlast_division_point} ] see This [ {doing_atlast_division_point}*{collecting_user_last_vlue}={doing_give_prof} ] [ {collecting_user_first_vlue}-{doing_give_prof}={doing_give_prof_2nd} ]'
if_in_extra_division = f'After division [ {doing_final_number_after_division} ] is extra and can\'t be divided anymore with [ {collecting_user_last_vlue} ]'

if user_select_number == '1':
    print(
        f'Answere is [ {doing_plus} ] \n\n[ {collecting_user_first_vlue}+{collecting_user_last_vlue} ]=[ {doing_plus} ]')
elif user_select_number == '2':
    print(
        f'Answere is [ {doing_minus} ] \n\n[ {collecting_user_first_vlue}-{collecting_user_last_vlue} ]=[ {doing_minus} ]')
elif user_select_number == '3':
    if doing_simple_division == doing_atlast_division_point:
        print(
            f'[ {collecting_user_first_vlue}/{collecting_user_last_vlue} ] is [ {doing_simple_division} ] \n\nAnsware is [ {doing_simple_division} ]')
    else:
        print(
            f'\nIf it force answere will be [ {doing_simple_division} ]\nOtherwise,\nMaximum division is [ {doing_atlast_division_point} ] ,And extra value is [ {doing_final_number_after_division} ]\nIf you want to know how, You can read below explanation\n\n{if_in_division} \n{if_in_extra_division}')
elif user_select_number == '4':
    print(f'Answere is [ {doing_multiplication} ] \n\n[ {collecting_user_first_vlue}X{collecting_user_last_vlue} ]=[ {doing_multiplication} ]')
elif user_select_number == '5':
    print(f'Answere is [ {doing_exponentiation} ] \n\n[ {collecting_user_first_vlue}^{collecting_user_last_vlue} ]=[ {doing_exponentiation} ]')
