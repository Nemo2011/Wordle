""" Hard mode check algorithm. """
# TODO:定义函数
def hard_valid(wordle, word):
    """Check hard mode."""
    types = wordle.stats.log
    colors = wordle.stats.colors
    word = word.upper()
    for rnd, color_s in enumerate(colors):
        for idx, color in enumerate(color_s):
            if color == "g":
                if word[idx] != types[rnd][idx]:
                    dct = {0: "ST", 1: "ND", 2: "RD", 3: "TH", 4: "TH", 5: "TH"}
                    return [
                        False,
                        f"{idx + 1}{dct[idx]} letter must be '{types[rnd][idx]}'. ",
                        types[rnd][idx],
                    ]
            elif color == "y":
                if not types[rnd][idx] in word:
                    return [
                        False,
                        f"'{types[rnd][idx]}' not in the word. ",
                        types[rnd][idx],
                    ]
    return True
