from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from MadmaxXMusic import app

from config import SUPPORT_CHAT


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_CHAT),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                ),
            ]
        ]
    )
    return upl

def add_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=True&admin=delete_messages+invite_users"),
           ],
        ]
    )
    return upl

def suppclose_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                 InlineKeyboardButton(
                text="✨ꜱᴜᴘᴘᴏʀᴛ✨", url=SUPPORT_CHAT,
            ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl

def source_markup(_):
    upl = InlineKeyboardMarkup(
        [
           [ 
                InlineKeyboardButton(
                        text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper"
                    ),
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ", callback_data=f"close"
                    ),
           ],
        ]
    )
    return upl

def lood_markup(_):
    upl = InlineKeyboardMarkup(
        [
                [
                    InlineKeyboardButton(
                        text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/STATUSDAIRY2"
                    ),

                    InlineKeyboardButton(
                        text="ᴍᴜsɪᴄ ɢʀᴏᴜᴘ", url="https://t.me/vohmusic"
                    ),
                    
                ],
                [
                    InlineKeyboardButton(
                        text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/ABOUT_SASHIKANT/3"
                    ),

                    InlineKeyboardButton(
                        text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/VOICEOFHEART0"
                    ),
                    
                ],
                [
                    InlineKeyboardButton(
                        text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper"
                    )
                ],
            ]
    )
    return upl
