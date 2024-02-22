def factorial(i: int):
    if i == 0:
        return 0
    return i + factorial(i - 1)


def factorial_cap(high: int):
    n = 1
    i = 1
    while i < high:
        n += 1
        i += n
    return n


def decode(message_file: str):
    with open(message_file, "r") as f:
        text_dict = {
            int(entry.split(" ")[0]): entry.split(" ")[1].strip()
            for entry in f.readlines()
        }

    high = len(text_dict)
    inc = factorial_cap(high)
    sentence = []
    while inc > 0:
        sentence.append(text_dict[high])
        high -= inc
        inc -= 1
    sentence.reverse()
    print(" ".join(sentence))
