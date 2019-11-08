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

def draw_carree(multiplicateur):
    for step in carree:
        if step[0] == 'fd':
            tu.fd((step[1] / 2)*multiplicateur)
        elif step[0] == 'rt':
            tu.rt(step[1])

    for step in sep:
        if step[0] == 'fd':
            tu.fd((step[1] / 2)*multiplicateur)
        elif step[0] == 'rt':
            tu.rt(step[1])

def draw_triangle(multiplicateur):
    for step in triangle:
        if step[0] == 'fd':
            tu.fd((step[1] / 2)*multiplicateur)
        elif step[0] == 'rt':
            tu.rt(step[1])

    for step in sep:
        if step[0] == 'fd':
            tu.fd((step[1] / 2)*multiplicateur)
        elif step[0] == 'rt':
            tu.rt(step[1])


pattern_count = int(input('Combien de patterns : '))

for step in sep:
    if step[0] == 'fd':
        tu.fd(step[1] / 2)
    elif step[0] == 'rt':
        tu.rt(step[1])

for i in range(1,pattern_count+1):
    draw_carree(i/2)
    draw_triangle(i/2)

tu.done()