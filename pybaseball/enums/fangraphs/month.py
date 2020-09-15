from enum import unique
from pybaseball.enums.enum_base import EnumBase


@unique
class FangraphsMonth(EnumBase):
    ALL               = 0
    MARCH_APRIL       = 4
    MAY               = 5
    JUNE              = 6
    JULY              = 7
    AUGUST            = 8
    SEPTEMBER_OCTOBER = 9
