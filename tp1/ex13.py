import turtle as tu

zone1 = [
    ['fl', True],
    ['fd', 500],
    ['rt', 90],
    ['fd', 150],
    ['rt', 90],
    ['fd', 500],
    ['rt', 90],
    ['fd', 150],
    ['fl', False],
    ['rt', 180],
    ['fd', 150],
]

zone2 = [
    ['fl', True],
    ['rt', -90],
    ['fd', 100],
    ['rt', 90],
    ['fd', 500],
    ['rt', 90],
    ['fd', 100],
    ['rt', 90],
    ['fd', 500],
    ['fl', False],
    ['rt', 180],
    ['fd', 500],
    ['rt', -90],
    ['fd', 100],
]

zone3 = [
    ['fl', True],
    ['rt', -90],
    ['fd', 200],
    ['rt', 90],
    ['fd', 100],
    ['rt', 90],
    ['fd', 200],
    ['rt', 90],
    ['fd', 100],
    ['fl', False],
    ['rt', 180],
    ['fd', 100]
]

zone4 = [
    ['fl', True],
    ['rt', -90],
    ['fd', 500],
    ['rt', 90],
    ['fd', 300],
    ['rt', 90],
    ['fd', 500],
    ['fl', False]
]

zones = {
    'zone1': {'color': 'red', 'layout': zone1},
    'zone2': {'color': 'blue', 'layout': zone2},
    'zone3': {'color': 'orange', 'layout': zone3},
    'zone4': {'color': 'green', 'layout': zone4},
}

for zone,details in zones.items():
    tu.color(details['color'])
    tu.begin_fill()
    for step in details['layout']:
        if step[0] == 'fd':
            tu.fd(step[1] / 2)
        elif step[0] == 'rt':
            tu.rt(step[1])
        elif step[0] == 'fl':
            if step[1] == True:
                tu.begin_fill()
            else:
                tu.end_fill()


tu.done()