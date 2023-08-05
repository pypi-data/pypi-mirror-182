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

from io import BytesIO

from pyroge.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyroge.raw.core import TLObject
from pyroge import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MessageViews(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyroge.raw.base.messages.MessageViews`.

    Details:
        - Layer: ``148``
        - ID: ``B6C4F543``

    Parameters:
        views (List of :obj:`MessageViews <pyroge.raw.base.MessageViews>`):
            N/A

        chats (List of :obj:`Chat <pyroge.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyroge.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyroge.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMessagesViews
    """

    __slots__: List[str] = ["views", "chats", "users"]

    ID = 0xb6c4f543
    QUALNAME = "types.messages.MessageViews"

    def __init__(self, *, views: List["raw.base.MessageViews"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.views = views  # Vector<MessageViews>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageViews":
        # No flags
        
        views = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return MessageViews(views=views, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.views))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
