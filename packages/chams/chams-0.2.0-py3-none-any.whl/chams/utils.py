import random


def get_random_color(i):
    colors = ["#74ac6d", "#aca46d", "#6d74ac", "#a46dac", "#6daca4", "#ac6d74"]
    if i:
        return colors[i % len(colors)]
    else:
        return random.choice(colors)


def generate_temperatures(number, start, end):
    return [random.randint(start, end) for _ in range(number)]
