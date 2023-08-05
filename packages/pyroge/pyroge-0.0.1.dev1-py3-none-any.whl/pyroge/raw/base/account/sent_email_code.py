#  Pyroge - Telegram MTProto API Client Library for Python.
#  Copyright (C) 2022-2023 Vckyou <https://github.com/Vckyou>
#
#  This file is part of Pyroge.
#
#  Pyroge is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyroge is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Pyroge.  If not, see <http://www.gnu.org/licenses/>.

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyroge import raw
from pyroge.raw.core import TLObject

SentEmailCode = Union[raw.types.account.SentEmailCode]


# noinspection PyRedeclaration
class SentEmailCode:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyroge.raw.types

        .. autosummary::
            :nosignatures:

            account.SentEmailCode

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyroge.raw.functions

        .. autosummary::
            :nosignatures:

            account.SendVerifyEmailCode
    """

    QUALNAME = "pyroge.raw.base.account.SentEmailCode"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/sent-email-code")
