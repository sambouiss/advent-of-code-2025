import math

def process_expression(expression: list[str]) -> int:
    if expression[-1] == '+':
        return sum(int(item) for item in expression[:-1])
    elif expression[-1] == '*':
        return math.prod(int(item) for item in expression[:-1])

def main():
    expressions = []
    with open('trash_compactor\input.txt') as f:
        for line in f:
            expressions.append(list(item.rstrip('\n') for item in line.split(' ') if item))
    print(list(zip(*expressions)))

    return sum(process_expression(expression) for expression in zip(*expressions))
    

if __name__ == "__main__":
    result = main()
    print(f'Got {result} after compacting trash')