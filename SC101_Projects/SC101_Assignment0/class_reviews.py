"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


EXIT1 = '-1'
EXIT2 = -1


def main():
    """
    This program will calculate the entered score of SC001 or SC101 and give you the Max, Min and Ave.
    """
    a = 'SC001'
    b = 'SC101'
    sc = input('Which class? ')
    if sc == EXIT1:  # If no data entered no need to continue.
        print('No class scores were entered')
    if sc.upper() == a:  # Check weather the entered class is SC001 or SC101.
        score = int(input('Score: '))
        maximum_a = score  # If the entered class was SC001, only SC001 has score so SC101 start with 0.
        minimum_a = score
        total_a = score
        step_a = 1
        maximum_b = 0
        minimum_b = 0
        total_b = 0
        step_b = 0
    elif sc.upper() == b:
        score = int(input('Score: '))
        maximum_b = score
        minimum_b = score
        total_b = score
        step_b = score
        maximum_a = 0
        minimum_a = 0
        total_a = 0
        step_a = 0
    while True:
        sc = input('Which class? ')
        if sc == EXIT1:
            break
        elif sc.upper() == a:
            score = int(input('Score: '))
            step_a += 1
            if score == EXIT2:
                break
            total_a += score
            if maximum_a != 0:
                if score > maximum_a:
                    maximum_a = score
            else:
                maximum_a = score
            if minimum_a != 0:
                if score < minimum_a:
                    minimum_a = score
            else:
                minimum_a = score
        elif sc.upper() == b:
            score = int(input('Score: '))
            step_b += 1
            if score == EXIT2:
                break
            total_b += score
            if maximum_b != 0:
                if score > maximum_b:
                    maximum_b = score
            else:
                maximum_b = score
            if minimum_b != 0:
                if score < minimum_b:
                    minimum_b = score
            else:
                minimum_b = score
    if total_a > 0:
        average_a = total_a / step_a
        print('=============SC001=============')
        print('Max (001): ' + str(maximum_a))
        print('Min (001): ' + str(minimum_a))
        print('Avg (001): ' + str(average_a))
    else:
        print('=============SC001=============')
        print('No score for SC001')
    if total_b > 0:
        average_b = total_b / step_b
        print('=============SC101=============')
        print('Max (101): ' + str(maximum_b))
        print('Min (101): ' + str(minimum_b))
        print('Avg (101): ' + str(average_b))
    else:
        print('=============SC101=============')
        print('No score for SC101')


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
