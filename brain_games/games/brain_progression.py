from random import randint


def correct_answer(qwestion: str) -> str:
    qwestion_list = qwestion.split()
    i = qwestion_list.index('..')
    if i > 2:
        lost_num = 2 * int(qwestion_list[i - 1]) - int(qwestion_list[i - 2])
    else:
        lost_num = 2 * int(qwestion_list[i + 1]) - int(qwestion_list[i + 2])
    return str(lost_num)


def generate_qwestion() -> str:
    start = randint(1, 10)
    step = randint(1, 10)
    result = []
    for i in range(10):
        result.append(str(start + i * step))
    miss_index = randint(1, 9)
    result[miss_index] = '..'
    result_str = ' '.join(result)
    return result_str


description = 'What number is missing in the progression?'
