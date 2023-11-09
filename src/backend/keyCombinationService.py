import usb_gadget
from keydictionary import keys


def setupkeyboard():
    gadget = usb_gadget.USBGadget('test_gadget')
    gadget.idVendor = '0x1d6b'
    gadget.idProduct = '0x0104'
    gadget.bcdDevice = '0x0100'
    gadget.bcdUSB = '0x0200'

    strings = gadget['strings']['0x409']
    strings.serialnumber = '0000000001'
    strings.manufacturer = 'roboter5123'
    strings.product = 'MacroTouch'

    config = gadget['configs']['c.1']
    config.bmAttributes = '0x80'
    config.MaxPower = '250'
    config['strings']['0x409'].configuration = 'Test Configuration'

    function = usb_gadget.HIDFunction(gadget, 'keyboard0')
    descriptor = [
        0x05, 0x01,  # Usage Page (Generic Desktop Ctrls)
        0x09, 0x06,  # Usage (Keyboard)
        0xA1, 0x01,  # Collection (Application)
        0x05, 0x07,  # Usage Page (Kbrd/Keypad)
        0x19, 0xE0,  # Usage Minimum (0xE0)
        0x29, 0xE7,  # Usage Maximum (0xE7)
        0x15, 0x00,  # Logical Minimum (0)
        0x25, 0x01,  # Logical Maximum (1)
        0x75, 0x01,  # Report Size (1)
        0x95, 0x08,  # Report Count (8)
        0x81, 0x02,  # Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
        0x95, 0x01,  # Report Count (1)
        0x75, 0x08,  # Report Size (8)
        0x81, 0x03,  # Input (Const,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
        0x95, 0x06,  # Report Count (6)
        0x75, 0x08,  # Report Size (8)
        0x15, 0x00,  # Logical Minimum (0)
        0x25, 0x65,  # Logical Maximum (101)
        0x05, 0x07,  # Usage Page (Kbrd/Keypad)
        0x19, 0x00,  # Usage Minimum (0x00)
        0x29, 0x65,  # Usage Maximum (0x65)
        0x81, 0x00,  # Input (Data,Array,Abs,No Wrap,Linear,Preferred State,No Null Position)
        0xC0,  # End Collection
    ]
    function.protocol = '0'
    function.subclass = '0'
    function.report_length = '8'
    function.report_desc = bytes(descriptor)
    gadget.link(function, config)

    gadget.activate()
    keyboard = usb_gadget.KeyboardGadget(function.device, 6)

    return {"keyboard": keyboard, "gadget": gadget}


def translatekey(key: str) -> str:
    if key not in keys:
        return key
    else:
        return keys.get(key)


def translatekeycombination(splitkeycombination: list[str]) -> list[str]:
    translatedkeycombination: list[str] = []
    for key in splitkeycombination:
        translatedkeycombination.append(translatekey(key))
    return translatedkeycombination


class KeyCombinationService:
    gadgetSetup = setupkeyboard()
    keyboard = gadgetSetup["keyboard"]
    gadget = gadgetSetup["gadget"]

    def executekeycombo(self, keycombination: str) -> None:
        splitkeycombination: List[str] = keycombination.split("%+")
        translatedkeycombination: List[str] = translatekeycombination(splitkeycombination)

        for key in translatedkeycombination:
            self.keyboard.press(key)

        for key in translatedkeycombination:
            self.keyboard.release(key)

    def __del__(self):
        self.gadget.destroy()

    def __init__(self):
        pass
