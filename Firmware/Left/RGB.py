from kmk.extensions.rgb import RGB as _RGB
from kmk.extensions.rgb import AnimationModes
from kmk.quickpin.pro_micro.rp2350 import (
    pinout as pins,  # change this to match your MCU board
)

class RGB(_RGB):
    def __init__(self):
        super().__init__(pixel_pin=pins[0], )
        self.num_pixels=27,
        self.val_limit=100,
        self.hue_default=0,
        self.sat_default=100,
        self.rgb_order=(1, 0, 2),  # GRB WS2812
        self.val_default=100,
        self.hue_step=5,
        self.sat_step=5,
        self.val_step=5,
        self.animation_speed=1,
        self.breathe_center=1,  # 1.0-2.7
        self.knight_effect_length=3,
        self.animation_mode=AnimationModes.STATIC,
        self.reverse_animation=False,
        self.refresh_rate=60,
