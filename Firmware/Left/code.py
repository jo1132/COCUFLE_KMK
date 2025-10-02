# HANgeul-Annotated Resoluxe's Efficient, Updated main.py (HAN-AREUm) for Ferris Sweep
# <0부터 시작하는 스플릿 키보드> WikiDocs 가이드에 배포된, Ferris Sweep / KMK 전용 main.py
# https://wikidocs.net/book/9749
# 본인 입맛에 맞게 자유롭게 수정해서 이용하세요!

# Replicates default Ferris keymap from QMK
# Credit: Pierre Chevalier, 2020
# https://github.com/qmk/qmk_firmware/tree/master/keyboards/ferris/keymaps/default

# Original KMK Keymap from:
# https://github.com/KMKfw/kmk_firmware/blob/master/boards/ferris_sweep/main.py

# 키보드의 초기 세팅입니다. 중심 모듈과 기능 모듈을 불러옵니다.
# 다른 기능을 추가하려면 여기에서 import하는 것에서 시작!
import board
from kb import KMKKeyboard
from rotary_encoder import EncoderHandler
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.split import Split, SplitSide
from kmk.extensions.international import International

# KMKKeyboard의 인스턴스를 keyboard라는 이름으로 생성
keyboard  =  KMKKeyboard()
encoder_handler = EncoderHandler()


# 불러온 기능들을 구체적인 키맵으로 활용하기 위하여 keyboard.modules 리스트에 추가합니다.
# 현재 사양으로는 split은 무조건 holdtap 다음에 추가되어야 합니다!!
keyboard.modules.append(HoldTap())
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
split = Split(data_pin=board.GP17, data_pin2=board.GP16, use_pio=True, split_side=SplitSide.LEFT)
keyboard.modules.append(split)
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(International())

from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes
rgb = RGB(pixel_pin=board.GP0,
        num_pixels=30,
        val_limit=100,
        hue_default=0,
        sat_default=100,
        rgb_order=(1, 0, 2),  # GRB WS2812
        val_default=100,
        hue_step=5,
        sat_step=5,
        val_step=5,
        animation_speed=1,
        breathe_center=1,  # 1.0-2.7
        knight_effect_length=3,
        animation_mode=AnimationModes.STATIC,
        reverse_animation=False,
        refresh_rate=60,
        )
keyboard.extensions.append(rgb)

# 비어있는 키들을 정의하는 부분.
# KC.TRNS는 VIA로 치면 역삼각형과 동일.
# KC.NO는 각 레이어에서 해당 자리를 사용하지 못하게 막는 것.
# (해당 키맵의 원작자는 좀 더 직관적으로 _와 X로 표현한 듯 합니다.)

_______  = KC.TRNS
XXXXXXX  = KC.NO

# 홀드탭 키를 정의하는 부분.
# 맨날 KC.HT 어쩌고 쓰려면 기니까 다른 이름의 변수에 할당합시다.
# A_SFT  = KC.HT(KC.A, KC.LSFT,prefer_hold=False)
# SCLN_SFT  = KC.HT(KC.SCLN, KC.LSFT,prefer_hold=False)
# X_CTL  = KC.HT(KC.X, KC.LCTRL,prefer_hold=False)
# C_ALT  = KC.HT(KC.C, KC.LALT,prefer_hold=False)
# COM_ALT  = KC.HT(KC.COMM, KC.LALT,prefer_hold=False)
# DOT_CTL  = KC.HT(KC.DOT, KC.LCTRL,prefer_hold=False)
# CTL_ALT  = KC.LCTRL(KC.LALT)


# 레이어 키를 정의하는 부분.
### 초기화
default_layer = 0
KC.DF(default_layer)

en_L1 = KC.TO(0)
en_L2 = KC.MO(1)
en_L3 = KC.TO(2)

k_L1 = KC.LT(0, KC.SPC)
k_L2 = KC.LT(1, KC.SPC)

dot_HT = KC.HT(KC.COMMA, KC.DOT)
minus_HT = KC.HT(KC.N9, KC.MINUS)
plus_HT = KC.HT(KC.N0, KC.PLUS)
equl_HT = KC.HT(KC.N0, KC.EQUAL)
quote_HT = KC.HT(KC.SCOLON, KC.QUOTE)
LBRC_HT = KC.HT(KC.O, KC.LBRACKET)
RBRC_HT = KC.HT(KC.P, KC.RBRACKET)
# D_L1  = KC.LT(1, KC.D)
# F_L3  = KC.LT(3, KC.F)
# J_L4  = KC.LT(4, KC.J)
# K_L2  = KC.LT(2, KC.K)
# L_L6  = KC.LT(6, KC.L)
# SPC_L7  = KC.LT(7, KC.SPC)

# 위에서 불러온 기능과 정의한 키를 이용해, 키매핑을 해 봅시다!
keyboard.keymap = [
    [
        KC.GESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4, KC.N5,                       KC.N6, KC.N7, KC.N8,   minus_HT,plus_HT,  KC.BSPC,
        KC.TAB,   KC.Q,    KC.W,    KC.E,    KC.R,  KC.T,                        KC.Y,  KC.U,  KC.I,    KC.O,    KC.P,     KC.BSLASH,
        KC.LSHIFT,KC.A,    KC.S,    KC.D,    KC.F,  KC.G,                        KC.H,  KC.J,  KC.K,    KC.L,    quote_HT, KC.ENTER,
        KC.LCTRL, KC.Z,    KC.X,    KC.C,    KC.V,  KC.B,                        KC.B,  KC.N,  KC.M,    dot_HT,  KC.SLASH, KC.RSHIFT,
                  KC.LALT, KC.LEFT, KC.RGHT, KC.SPC,en_L1,KC.RGB_TOG, KC.RGB_TOG,en_L2, KC.SPC,KC.HAEN, KC.UP,   KC.DOWN,
    ],
    [
        KC.GESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4, KC.N5,                       _______, KC.DELETE,KC.END,  KC.HOME,    KC.EQUAL,    KC.BSPC,
        KC.TAB,   KC.Q,    KC.W,    KC.E,    KC.R,  KC.T,                        _______, _______,  KC.UP,   KC.LBRACKET,KC.RBRACKET, KC.BSLASH,
        KC.LSHIFT,KC.A,    KC.S,    KC.D,    KC.F,  KC.G,                        _______, KC.LEFT,  KC.DOWN, KC.RGHT,    _______,     KC.ENTER,
        KC.LCTRL, KC.Z,    KC.X,    KC.C,    KC.V,  KC.B,                        _______, _______,  _______, _______,    _______,     _______,
                  KC.LALT, KC.LEFT, KC.RGHT, KC.SPC,en_L1,KC.RGB_TOG, KC.RGB_TOG,_______, KC.SPC,   KC.HAEN, KC.UP,      KC.DOWN,
    ],
]


# Right encoder is mapped to move layer
### Encoder init

# right_encoder_fn = (encoder_handler.target_layer_up, encoder_handler.target_layer_down, KC.TG(encoder_handler.target_layer))
# encoder_handler.map = [ ((KC.A, KC.Z, False),), # Extra
#                         ((KC.A, KC.Z, False),), # NumPad not yet properly configured
#                         ((KC.A, KC.Z, False),), # Gaming not yet properly configured
#                         ]

encoder_handler.map = [ ((KC.MW_RIGHT, KC.MW_LEFT, False),), # Extra
                        ((KC.MW_RIGHT, KC.MW_LEFT, False),), # NumPad not yet properly configured
                    ]
# 마지막은 항상 이걸로 끝납니다.
if  __name__  ==  "__main__":
    keyboard.go()
