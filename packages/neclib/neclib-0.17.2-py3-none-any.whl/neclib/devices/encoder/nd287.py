__all__ = ["ND287"]

from typing import Literal

import astropy.units as u
import ogameasure

from ... import utils
from .encoder_base import Encoder


class ND287(Encoder):
    """Encoder readout."""

    Manufacturer = "HEIDENHAIN"
    Model = "ND287"

    Identifier = "port_az"

    @utils.skip_on_simulator
    def __init__(self) -> None:
        self.driver = {
            "az": ogameasure.HEIDENHAIN.ND287(self.Config.port_az),
            "el": ogameasure.HEIDENHAIN.ND287(self.Config.port_el),
        }

    def get_reading(self, axis: Literal["az", "el"]) -> u.Quantity:
        raw = self.driver[axis.lower()].output_position_display_value()
        return float(raw.strip(b"\x02\x00\r\n").decode()) << u.deg  # type: ignore

    def finalize(self) -> None:
        pass
