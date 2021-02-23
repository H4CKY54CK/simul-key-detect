layout = r"""
---------------------------------------------------------------------------------------------------
|{1}|      |{59}|{60}|{61}|{62}|    |{63}|{64}|{65}|{66}|    |{67}|{68}|{87}|{88}| |{99}|{70}|{119}|    HACKYSACK    |
|                                                                                                 |
| {41} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} | {10} | {11} | {12} | {13} |  {14}  |   |{110}|{102}|{104}|   |{69}| {98} | {55} | {74} |
| {15} | {16} | {17} | {18} | {19} | {20} | {21} | {22} | {23} | {24} | {25} | {26} | {27} |  {43}  |   |{111}|{107} |{109}|   | {71} | {72} | {73} |   |
| {58} | {30} | {31} | {32} | {33} | {34} | {35} | {36} | {37} | {38} | {39} | {40} |  {28} |                     | {75} | {76} | {77} | {78} |
| {42}  | {44} | {45} | {46} | {47} | {48} | {49} | {50} | {51} | {52} | {53} |  {54} |        | {103} |        | {79} | {80} | {81} |   |
|{29}|{125} |{56}|           {57}           |{100}|{127}|{97}|    | {105} | {108} | {106} |    |   {82}   | {83} | {96} |
---------------------------------------------------------------------------------------------------
"""

codes = {
    '1': {'name': 'ESC', 'state': 0},
    '59': {'name': 'F1', 'state': 0},
    '60': {'name': 'F2', 'state': 0},
    '61': {'name': 'F3', 'state': 0},
    '62': {'name': 'F4', 'state': 0},
    '63': {'name': 'F5', 'state': 0},
    '64': {'name': 'F6', 'state': 0},
    '65': {'name': 'F7', 'state': 0},
    '66': {'name': 'F8', 'state': 0},
    '67': {'name': 'F9', 'state': 0},
    '68': {'name': 'F10', 'state': 0},
    '87': {'name': 'F11', 'state': 0},
    '88': {'name': 'F12', 'state': 0},
    '99': {'name': 'PRTSC', 'state': 0},
    '70': {'name': 'SCRLK', 'state': 0},
    '119': {'name': 'PAUSE', 'state': 0},
    '41': {'name': '`', 'state': 0},
    '2': {'name': '1', 'state': 0},
    '3': {'name': '2', 'state': 0},
    '4': {'name': '3', 'state': 0},
    '5': {'name': '4', 'state': 0},
    '6': {'name': '5', 'state': 0},
    '7': {'name': '6', 'state': 0},
    '8': {'name': '7', 'state': 0},
    '9': {'name': '8', 'state': 0},
    '10': {'name': '9', 'state': 0},
    '11': {'name': '0', 'state': 0},
    '12': {'name': '-', 'state': 0},
    '13': {'name': '=', 'state': 0},
    '14': {'name': '<--', 'state': 0},
    '110': {'name': 'INS', 'state': 0},
    '102': {'name': 'HOME', 'state': 0},
    '104': {'name': 'PGUP', 'state': 0},
    '69': {'name': 'NUM', 'state': 0},
    '98': {'name': '/', 'state': 0},
    '55': {'name': '*', 'state': 0},
    '74': {'name': '-', 'state': 0},
    '15': {'name': 'TAB', 'state': 0},
    '16': {'name': 'Q', 'state': 0},
    '17': {'name': 'W', 'state': 0},
    '18': {'name': 'E', 'state': 0},
    '19': {'name': 'R', 'state': 0},
    '20': {'name': 'T', 'state': 0},
    '21': {'name': 'Y', 'state': 0},
    '22': {'name': 'U', 'state': 0},
    '23': {'name': 'I', 'state': 0},
    '24': {'name': 'O', 'state': 0},
    '25': {'name': 'P', 'state': 0},
    '26': {'name': '[', 'state': 0},
    '27': {'name': ']', 'state': 0},
    '43': {'name': '\\', 'state': 0},
    '111': {'name': 'DEL', 'state': 0},
    '107': {'name': 'END', 'state': 0},
    '109': {'name': 'PGDN', 'state': 0},
    '71': {'name': '7', 'state': 0},
    '72': {'name': '8', 'state': 0},
    '73': {'name': '9', 'state': 0},
    '78': {'name': '+', 'state': 0},
    '58': {'name': 'CAPS', 'state': 0},
    '30': {'name': 'A', 'state': 0},
    '31': {'name': 'S', 'state': 0},
    '32': {'name': 'D', 'state': 0},
    '33': {'name': 'F', 'state': 0},
    '34': {'name': 'G', 'state': 0},
    '35': {'name': 'H', 'state': 0},
    '36': {'name': 'J', 'state': 0},
    '37': {'name': 'K', 'state': 0},
    '38': {'name': 'L', 'state': 0},
    '39': {'name': ';', 'state': 0},
    '40': {'name': '\'', 'state': 0},
    '28': {'name': 'ENTER', 'state': 0},
    '75': {'name': '4', 'state': 0},
    '76': {'name': '5', 'state': 0},
    '77': {'name': '6', 'state': 0},
    '42': {'name': 'LSHIFT', 'state': 0},
    '44': {'name': 'Z', 'state': 0},
    '45': {'name': 'X', 'state': 0},
    '46': {'name': 'C', 'state': 0},
    '47': {'name': 'V', 'state': 0},
    '48': {'name': 'B', 'state': 0},
    '49': {'name': 'N', 'state': 0},
    '50': {'name': 'M', 'state': 0},
    '51': {'name': ',', 'state': 0},
    '52': {'name': '.', 'state': 0},
    '53': {'name': '/', 'state': 0},
    '54': {'name': 'RSHIFT', 'state': 0},
    '103': {'name': '^', 'state': 0},
    '79': {'name': '1', 'state': 0},
    '80': {'name': '2', 'state': 0},
    '81': {'name': '3', 'state': 0},
    '96': {'name': '<', 'state': 0},
    '29': {'name': 'LCTRL', 'state': 0},
    '125': {'name': 'WIN', 'state': 0},
    '56': {'name': 'LALT', 'state': 0},
    '57': {'name': 'SPACE', 'state': 0},
    '100': {'name': 'RALT', 'state': 0},
    '127': {'name': 'MENU', 'state': 0},
    '97': {'name': 'RCTRL', 'state': 0},
    '105': {'name': '<', 'state': 0},
    '108': {'name': 'v', 'state': 0},
    '106': {'name': '>', 'state': 0},
    '82': {'name': '0', 'state': 0},
    '83': {'name': '.', 'state': 0},
}

import sys



class Keys:

    def __init__(self):
        sys.stdout.write('\x1b[s')
        self.keys = codes.copy()
        self.display()

    def parse(self, values):
        if values[4] == 1:
            key = str(values[5])
            state = values[6]
            self.keys[key]['state'] = state
        self.display()

    def display(self):
        sys.stdout.write('\x1b[u\x1b[2J')
        output = self.get_keyboard()
        sys.stdout.write(output)

    def get_keyboard(self):
        text = layout
        for key, value in self.keys.items():
            k = f'{{{key}}}'
            if value['state'] == 1:
                repl = f"\x1b[1;4;32m{value['name']}\x1b[0m"
            elif value['state'] == 2:
                repl = f"\x1b[1;4;33m{value['name']}\x1b[0m"
            else:
                l = ' ' * len(value['name'])
                repl = f"\x1b[4m{l}\x1b[0m"
            text = text.replace(k, repl)
        return text
