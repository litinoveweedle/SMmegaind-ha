"""Verify combined edge settings through the published driver."""

import megaind
import pytest

from custom_components.smmegaind.driver_adapter import get_opto_edge, set_opto_edge


@pytest.mark.parametrize("old,new", [(3, 1), (3, 2), (1, 2), (2, 0), (0, 3)])
def test_edge_settings(monkeypatch, old, new):
    registers = {
        megaind.I2C_MEM_OPTO_RISING_ENABLE: (old & 1) | 2,
        megaind.I2C_MEM_OPTO_FALLING_ENABLE: ((old >> 1) & 1) | 2,
    }

    class Bus:
        def read_byte_data(self, _address, register):
            return registers[register]

        def write_byte_data(self, _address, register, value):
            registers[register] = value

        def close(self):
            pass

    monkeypatch.setattr(megaind.smbus2, "SMBus", lambda _: Bus())
    set_opto_edge(0, 1, new)
    assert get_opto_edge(0, 1) == new
    assert get_opto_edge(0, 2) == 3


def test_invalid_edge_is_rejected(monkeypatch):
    def unexpected_write(*_):
        pytest.fail("invalid edge must not write to the card")

    monkeypatch.setattr(megaind, "setOptoRisingCountEnable", unexpected_write)
    with pytest.raises(ValueError, match="Invalid"):
        set_opto_edge(0, 1, 4)
