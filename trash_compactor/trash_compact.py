import math
from constants import TEST_PATH, EVAL_PATH
def process_expression(expression: list[str]) -> int:
    if expression[-1] == '+':
        return sum(int(item) for item in expression[:-1])
    elif expression[-1] == '*':
        return math.prod(int(item) for item in expression[:-1])

def main(input_file_path):
    expressions = []
    with open(input_file_path) as f:
        for line in f:
            expressions.append(list(item.rstrip('\n') for item in line.split(' ') if item))

    return sum(process_expression(expression) for expression in zip(*expressions))
    

if __name__ == "__main__":
 
    test_result = main(TEST_PATH)
    assert test_result == 4277556
    result = main(EVAL_PATH)
    print(f'Got {result} after compacting trash')