"""Knobs for ImGui
Python bindings for https://github.com/altschuler/imgui-knobs
"""

from typing import Tuple, Optional
import numpy as np
import enum


from imgui_bundle.imgui import ImColor


ImGuiKnobFlags = int
ImGuiKnobVariant = int


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:imgui-knobs.h>    ####################
class ImGuiKnobFlags_(enum.Enum):
    no_title = enum.auto()  # (= 1 << 0)
    no_input = enum.auto()  # (= 1 << 1)
    value_tooltip = enum.auto()  # (= 1 << 2)
    drag_horizontal = enum.auto()  # (= 1 << 3)

class ImGuiKnobVariant_(enum.Enum):
    tick = enum.auto()  # (= 1 << 0)
    dot = enum.auto()  # (= 1 << 1)
    wiper = enum.auto()  # (= 1 << 2)
    wiper_only = enum.auto()  # (= 1 << 3)
    wiper_dot = enum.auto()  # (= 1 << 4)
    stepped = enum.auto()  # (= 1 << 5)
    space = enum.auto()  # (= 1 << 6)

""" namespace ImGuiKnobs"""

class color_set:
    base: ImColor
    hovered: ImColor
    active: ImColor

    def __init__(self, base: ImColor, hovered: ImColor, active: ImColor) -> None:
        pass
    def __init__(self, color: ImColor) -> None:
        pass

def knob(
    label: str,
    p_value: float,
    v_min: float,
    v_max: float,
    speed: float = 0,
    format: Optional[str] = None,
    variant: ImGuiKnobVariant = ImGuiKnobVariant_.tick,
    size: float = 0,
    flags: ImGuiKnobFlags = 0,
    steps: int = 10,
) -> Tuple[bool, float]:
    pass

def knob_int(
    label: str,
    p_value: int,
    v_min: int,
    v_max: int,
    speed: float = 0,
    format: Optional[str] = None,
    variant: ImGuiKnobVariant = ImGuiKnobVariant_.tick,
    size: float = 0,
    flags: ImGuiKnobFlags = 0,
    steps: int = 10,
) -> Tuple[bool, int]:
    pass
####################    </generated_from:imgui-knobs.h>    ####################

# </litgen_stub> // Autogenerated code end!
