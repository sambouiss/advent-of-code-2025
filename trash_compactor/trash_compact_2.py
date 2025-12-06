from constants import TIMES, PLUS, TEST_PATH, EVAL_PATH

def process_expression(expressions: list[tuple[str]]) -> int:
   
    result = 0
    ops = {TIMES, PLUS}
    curr = 0
    curr_op = PLUS
    for line in expressions:
        num = ''
        for item in line:
            if item.isdigit():
                num +=item
            if item in ops:
                result += curr
                if item == PLUS:
                    curr_op = PLUS
                    curr = 0
                else: 
                    curr_op = TIMES
                    curr = 1
        if num:
            num = int(num)
            if curr_op == PLUS:
                curr += num
            elif curr_op == TIMES:
                curr *= num
    else:
        result += curr
    return result

        
def main(input_file_path):
    expressions = []
    with open(input_file_path) as f:
        for line in f:
            expressions.append(line)

    return process_expression(list(zip(*expressions)))

    
    

if __name__ == "__main__":
    test_result = main(TEST_PATH)
    assert test_result == 3263827
    result = main(EVAL_PATH)
    print(f'Got {result} after compacting trash')