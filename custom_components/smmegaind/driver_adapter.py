"""Adapt Industrial Automation driver operations."""

import megaind


def __getattr__(name):
    return getattr(megaind, name)


def get_opto_edge(stack, channel):
    rising = megaind.getOptoRisingCountEnable(stack, channel)
    falling = megaind.getOptoFallingCountEnable(stack, channel)
    return rising | (falling << 1)


def set_opto_edge(stack, channel, edge):
    if edge not in (0, 1, 2, 3):
        raise ValueError("Invalid opto counter edge")
    megaind.setOptoRisingCountEnable(stack, channel, edge & 1)
    megaind.setOptoFallingCountEnable(stack, channel, (edge >> 1) & 1)
