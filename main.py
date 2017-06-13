import json
import os
import serial

from soundboard import SoundBoard
from controlboard import ControlBoard
from sirboard import SirBoard


def read_sounds():
    fp = 'sounds'
    x = {}
    x['sounds'] = os.listdir(fp)
    x['files'] = []
    for i in x['sounds']:
        f = open(os.path.join(fp, i))
        x['files'].append(f.name)
        f.close()
    w = open('sounds.json', 'w')
    json.dump(x, w)
    w.close()


def get_sounds():
    sounds = os.path.join('json', 'sounds.json')
    return json.load(open(sounds, 'r'))


def get_commands():
    cmd_filename = os.path.join('json', 'commands.json')
    return json.load(open(cmd_filename, 'r'))


def main():
    read_sounds()
    
    try:
        ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
    except serial.serialutil.SerialException as e:
        ser = None
        print ("ERROR: Could not open serial connection.")
        print (e)

    sb = SoundBoard()
    if ser is not None:
        cb = ControlBoard(ser.write)
    else:
        cb = ControlBoard(lambda x: print(x))


    sounds = get_sounds()
    for i, v in enumerate(sounds['sounds']):
        sb.add_sound(v, sounds['files'][i])

    commands = get_commands()
    for i, v in enumerate(commands['names']):
        cb.add_command(v, commands['keys'][i])


    board = SirBoard(sb, cb)

    board.run()

main()
