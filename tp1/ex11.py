import turtle as tu

sep = [
    ['fd',50]
]
carree = [
    ['fl', True],
    ['fd', 50],
    ['rt', 90],
    ['fd', 50],
    ['rt', 90],
    ['fd', 50],
    ['rt', 90],
    ['fd', 50],
    ['fl', False],
    ['rt', 90],
    ['fd', 50],
]

triangle = [
    ['fl', True],
    ['fd', 50],
    ['rt', 120],
    ['fd', 50],
    ['rt', 120],
    ['fd', 50],
    ['rt', 120],
    ['fl', False],
    ['fd', 50],
]

def draw_carree():
    for step in carree:
        if step[0] == 'fd':
            tu.fd(step[1] / 2)
        elif step[0] == 'rt':
            tu.rt(step[1])

    for step in sep:
        if step[0] == 'fd':
            tu.fd(step[1] / 2)
        elif step[0] == 'rt':
            tu.rt(step[1])

def draw_triangle():
    for step in triangle:
        if step[0] == 'fd':
            tu.fd(step[1] / 2)
        elif step[0] == 'rt':
            tu.rt(step[1])

    for step in sep:
        if step[0] == 'fd':
            tu.fd(step[1] / 2)
        elif step[0] == 'rt':
            tu.rt(step[1])


pattern_count = int(input('Combien de patterns : '))

for step in sep:
    if step[0] == 'fd':
        tu.fd(step[1] / 2)
    elif step[0] == 'rt':
        tu.rt(step[1])

for i in range(pattern_count):
    draw_carree()
    draw_triangle()

tu.done()