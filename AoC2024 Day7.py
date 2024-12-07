import itertools


def parse_input():
    with open("Day7.txt", "r") as file:
        equation = []
        for line in file:
            test_value_str, numbers_str = line.split(':')
            test_value = int(test_value_str.strip())
            numbers = list(map(int, numbers_str.strip().split()))
            equation.append((test_value, numbers))
        return equation


def evaluate_expression_p1(equations):
    total_result = 0
    operands = ["+", "*"]

    for equation in equations:
        n = len(equation[1])

        for ops in itertools.product(operands, repeat=n - 1):
            result = int(equation[1][0])
            for num, op in zip(equation[1][1:], ops):
                if op == "+":
                    result += num
                elif op == "*":
                    result *= num

            test_result = equation[0]

            if result == test_result:
                total_result += result
                break

    print(total_result)


def evaluate_expression_p2(equations):
    total_result = 0
    operands = ["+", "*", "||"]

    for equation in equations:
        n = len(equation[1])

        for ops in itertools.product(operands, repeat=n - 1):
            result = int(equation[1][0])
            for num, op in zip(equation[1][1:], ops):
                if op == "+":
                    result += num
                elif op == "*":
                    result *= num
                elif op == "||":
                    result = int(str(result) + str(num))

            test_result = equation[0]

            if result == test_result:
                total_result += result
                break

    print(total_result)


evaluate_expression_p1(parse_input())
evaluate_expression_p2(parse_input())
