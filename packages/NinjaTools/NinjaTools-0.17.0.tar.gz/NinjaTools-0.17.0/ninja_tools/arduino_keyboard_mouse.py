from ctypes import windll, Structure, c_long, byref
from time import sleep

import serial
import win32api

from ninja_tools.utils import Utilities
from ninja_tools.processing import ProcessTime
from ninja_tools.com_ports_scan import COMPorts


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


class ArduinoKeyboardMouse:

    def __init__(self, port: str = None,
                 baud_rate: int = 115200,
                 timeout: int = 0,
                 ratio_x: float = 0.0,
                 ratio_y: float = 0.0,
                 com_search: str = None):

        if port is None and com_search is None:
            raise ValueError("Port or com_search must be specified")

        if port is None:
            port = COMPorts.get_device_by_description(description=com_search)

            # Check if port is valid
            if port is None:
                raise ValueError("No COM port found for {0}".format(com_search))

        self.serial = serial.Serial(port=port, baudrate=baud_rate, writeTimeout=timeout)
        self.ratio_x = ratio_x
        self.ratio_y = ratio_y
        self.u = Utilities()

    # Mouse clicks
    def left_click(self):
        self.serial.write(bytes(b'ms1\n'))

    def right_click(self):
        self.serial.write(bytes(b'ms2\n'))

    def middle_click(self):
        self.serial.write(bytes(b'ms3\n'))

    def double_left_click(self):
        self.serial.write(bytes(b'ms4\n'))

    @staticmethod
    def left_pressed():
        return win32api.GetKeyState(0x01) < 0

    @staticmethod
    def right_pressed():
        return win32api.GetKeyState(0x02) < 0

    # Mouse holds
    def left_press(self):
        self.serial.write(bytes(b'ms5\n'))

    def left_release(self):
        self.serial.write(bytes(b'ms6\n'))

    def right_press(self):
        self.serial.write(bytes(b'ms7\n'))

    def right_release(self):
        self.serial.write(bytes(b'ms8\n'))

    def middle_press(self):
        self.serial.write(bytes(b'ms9\n'))

    def middle_release(self):
        self.serial.write(bytes(b'ms10\n'))

    def scroll_up(self, amount: int):
        self.serial.write(bytes("su{0}\n".format(amount), encoding='latin1'))
        sleep((60 * amount) / 1000)

    def scroll_down(self, amount: int):
        self.serial.write(bytes("sd{0}\n".format(amount), encoding='latin1'))
        sleep((60 * amount) / 1000)

    def mouse_move(self, x: int, y: int):
        self.serial.write(bytes("mm{}:{}\n".format(x, y), encoding='latin1'))

    def relative_move(self, x: int, y: int):
        t = ProcessTime()
        init_x, init_y = self.mouse_position()
        target_x, target_y = init_x + x, init_y + y
        i = 0
        self.serial.write(bytes("mm{}:{}\n".format(x, 0), encoding='latin1'))
        self.serial.write(bytes("mm{}:{}\n".format(0, y), encoding='latin1'))
        while target_x != init_x and target_y != init_y:
            if target_x > init_x:
                self.serial.write(bytes("mm{}:{}\n".format(1, 0), encoding='latin1'))
                self.u.pause(1)

            if target_x < init_x:
                self.serial.write(bytes("mm{}:{}\n".format(-1, 0), encoding='latin1'))
                self.u.pause(1)

            if target_y > init_y:
                self.serial.write(bytes("mm{}:{}\n".format(0, 1), encoding='latin1'))
                self.u.pause(1)

            if target_y < init_y:
                self.serial.write(bytes("mm{}:{}\n".format(0, -1), encoding='latin1'))
                self.u.pause(1)

            init_x, init_y = self.mouse_position()
            i += 1
            if i > 50:
                break

        return t.running_time()

    def mouse_move2(self, x: int, y: int):
        self.serial.write(bytes("ma{}:{}\n".format(x, y), encoding='latin1'))

    def read(self):
        line = self.serial.readline().decode('latin1').strip()
        if line:
            return line
        else:
            return None

    @staticmethod
    def point(x, y):
        win32api.SetCursorPos((x, y))

    @staticmethod
    def mouse_position():
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return pt.x, pt.y

    # keyboard press
    def key_press(self, key):
        self.serial.write(bytes("kp{0}\n".format(self.KeyCodes[key]), encoding='latin1'))

    def key_release(self, key):
        self.serial.write(bytes("kr{0}\n".format(self.KeyCodes[key]), encoding='latin1'))

    def press(self, key):
        self.serial.write(bytes("kb{0}\n".format(self.KeyCodes[key]), encoding='latin1'))
        self.u.pause(100)

    def type(self, word):
        for char in word:
            self.press(char)

    @staticmethod
    def is_pressed(key: int):
        return win32api.GetKeyState(key) < 0

    KeyCodes = {
        "LEFT_CTRL": "128",
        "LEFT_SHIFT": "129",
        "LEFT_ALT": "130",
        "LEFT_GUI": "131",
        "RIGHT_CTRL": "132",
        "RIGHT_SHIFT": "133",
        "RIGHT_ALT": "134",
        "RIGHT_GUI": "135",
        "UP_ARROW": "218",
        "DOWN_ARROW": "217",
        "LEFT_ARROW": "216",
        "RIGHT_ARROW": "215",
        "BACKSPACE": "178",
        "TAB": "179",
        "RETURN": "176",
        "ESC": "177",
        "INSERT": "209",
        "DELETE": "212",
        "PAGE_UP": "211",
        "PAGE_DOWN": "214",
        "HOME": "210",
        "END": "213",
        "CAPS_LOCK": "193",
        "F1": "194",
        "F2": "195",
        "F3": "196",
        "F4": "197",
        "F5": "198",
        "F6": "199",
        "F7": "200",
        "F8": "201",
        "F9": "202",
        "F10": "203",
        "F11": "204",
        "F12": "205",
        " ": "32",
        "!": "33",
        "": "34",
        "#": "35",
        "$": "36",
        "%": "37",
        "&": "38",
        "'": "39",
        "(": "40",
        ")": "41",
        "*": "42",
        "+": "43",
        ",": "44",
        "-": "45",
        ".": "46",
        "/": "47",
        "0": "48",
        "1": "49",
        "2": "50",
        "3": "51",
        "4": "52",
        "5": "53",
        "6": "54",
        "7": "55",
        "8": "56",
        "9": "57",
        ":": "58",
        ";": "59",
        "<": "60",
        "=": "61",
        ">": "62",
        "?": "63",
        "@": "64",
        "A": "65",
        "B": "66",
        "C": "67",
        "D": "68",
        "E": "69",
        "F": "70",
        "G": "71",
        "H": "72",
        "I": "73",
        "J": "74",
        "K": "75",
        "L": "76",
        "M": "77",
        "N": "78",
        "O": "79",
        "P": "80",
        "Q": "81",
        "R": "82",
        "S": "83",
        "T": "84",
        "U": "85",
        "V": "86",
        "W": "87",
        "X": "88",
        "Y": "89",
        "Z": "90",
        "[": "91",
        "\\": "92",
        "]": "93",
        "^": "94",
        "_": "95",
        "`": "96",
        "a": "97",
        "b": "98",
        "c": "99",
        "d": "100",
        "e": "101",
        "f": "102",
        "g": "103",
        "h": "104",
        "i": "105",
        "j": "106",
        "k": "107",
        "l": "108",
        "m": "109",
        "n": "110",
        "o": "111",
        "p": "112",
        "q": "113",
        "r": "114",
        "s": "115",
        "t": "116",
        "u": "117",
        "v": "118",
        "w": "119",
        "x": "120",
        "y": "121",
        "z": "122",
        "{": "123",
        "|": "124",
        "}": "125",
        "~": "126",
    }
