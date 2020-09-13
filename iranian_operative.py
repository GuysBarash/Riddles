import numpy as np

possible_lockers = range(13, 1300 + 1)


def q1(agent_say_yes=True):
    # Iranian, is the number smaller than 500?
    # syrian, [lie]

    you_know = list()
    iran_know = list()

    for t in possible_lockers:
        lower = t < 500
        higer = not lower
        agent_say_lower = agent_say_yes
        agent_says_higher = not agent_say_lower
        if lower and agent_say_lower:
            iran_know.append(t)
        elif lower and agent_says_higher:
            you_know.append(t)
        elif higer and agent_says_higher:
            iran_know.append(t)
        elif higer and agent_say_lower:
            you_know.append(t)
        else:
            print("<< BAD SELECTION >> ")

    return you_know, iran_know


def q2(agent_say_yes=True):
    # Iranian, is the number has than natural sqrt?
    # syrian, [lie]

    you_know = list()
    iran_know = list()

    nums_with_sqrt = [int(d ** 2) for d in range(40)]
    for t in possible_lockers:
        number_has_sqrt = t in nums_with_sqrt
        number_not_has_sqrt = not number_has_sqrt
        agent_says_num_has_sqrt = agent_say_yes
        agent_says_num_not_has_sqrt = not agent_says_num_has_sqrt

        if number_has_sqrt and agent_says_num_has_sqrt:
            iran_know.append(t)
        elif number_has_sqrt and agent_says_num_not_has_sqrt:
            you_know.append(t)
        elif number_not_has_sqrt and agent_says_num_has_sqrt:
            you_know.append(t)
        elif number_not_has_sqrt and agent_says_num_not_has_sqrt:
            iran_know.append(t)
        else:
            print("<< BAD SELECTION >> ")

    return you_know, iran_know


def q3(agent_say_yes=True):
    # Iranian, is the number has third natural sqrt?
    # syrian, [Truth]

    you_know = list()
    iran_know = list()

    nums_with_sqrt = [int(d ** 3) for d in range(40)]
    for t in possible_lockers:
        number_has_sqrt = t in nums_with_sqrt
        number_not_has_sqrt = not number_has_sqrt
        agent_says_num_has_sqrt = agent_say_yes
        agent_says_num_not_has_sqrt = not agent_says_num_has_sqrt

        if number_has_sqrt and agent_says_num_has_sqrt:
            iran_know.append(t)
            you_know.append(t)
        elif number_has_sqrt and agent_says_num_not_has_sqrt:
            pass
        elif number_not_has_sqrt and agent_says_num_has_sqrt:
            pass
        elif number_not_has_sqrt and agent_says_num_not_has_sqrt:
            iran_know.append(t)
            you_know.append(t)
        else:
            print("<< BAD SELECTION >> ")

    return you_know, iran_know


possible_combinations = [
    [True, True, True],
    [True, True, False],
    [True, False, True],
    [True, False, False],
    [False, True, True],
    [False, True, False],
    [False, False, True],
    [False, False, False],
]


def second_digit_is_1(n):
    s = str(n)
    if len(s) > 1:
        second_digit = int(s[-2])
        return second_digit == 1
    else:
        return False


def translate_combinations(l):
    ret = list()
    for lt in l:
        if lt:
            ret.append(f"{'Yes':<4}")
        else:
            ret.append(f"{'No':<4}")
    return ret


for combination in possible_combinations:
    combination_translated = []
    you1, iran1 = q1(combination[0])
    you2, iran2 = q2(combination[1])
    you3, iran3 = q3(combination[2])

    you_options = [t for t in you1 if (t in you2) and (t in you3)]
    iran_options = [t for t in iran1 if (t in iran2) and (t in iran3)]

    iran_options_with_second_digit_1 = [second_digit_is_1(t) for t in iran_options]
    sum_iran_options_with_second_digit_1 = sum(iran_options_with_second_digit_1)
    iran_options_without_second_digit_1 = [not t for t in iran_options_with_second_digit_1]
    sum_iran_options_without_second_digit_1 = sum(iran_options_without_second_digit_1)

    msg = ''
    msg += f"Option: {str(translate_combinations(combination)) :<25}\t\t Iran options:{len(iran_options):>4}\t\t"
    msg += f"Options with 2 a second digit: {sum_iran_options_with_second_digit_1:>4}\t"
    msg += f"Options with other second digit: {sum_iran_options_without_second_digit_1:>4}\t"

    last_quesion_help_us = sum_iran_options_with_second_digit_1 == 1 and sum_iran_options_without_second_digit_1 == 1

    possible_solution = False
    if last_quesion_help_us:
        msg += '\t\t<<<<< Possible solution'
        possible_solution = True
    else:
        msg += '\t\tlast question is pointless'

    print(msg)
    if possible_solution:
        msg = f"Your legal options are: {you_options}"
        if len(you_options) == 1:
            msg += f', And that is the right solution! {you_options[0]}'
        print(msg)
        print()
