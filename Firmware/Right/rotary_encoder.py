from kmk.modules.encoder import EncoderHandler as _EncoderHandler
from kmk.quickpin.pro_micro.rp2350 import (
    pinout as pins,  # change this to match your MCU board
)


class EncoderHandler(_EncoderHandler):
    def __init__(self):
        super().__init__()
        self.target_layer = 0
        self.layer_max = 0
        self.pins = (
            (pins[18], pins[19], False, True, 4), 
        )

    

