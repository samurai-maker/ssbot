from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"<b>Hi  {m.from_user.mention}.\n\nI'm Screenshot Generator Bot. I can provide screenshots from </b> "
        "<b>your video files without downloading the entire file (almost instantly). For more details check /help.</b>
        "<i>visit our chat groups 👇",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton("WWM MOVIE GROUP", url="https://t.me/WORLD_WIDE_MOVIES")],
                    [InlineKeyboardButton("MALAYALAM CHATTING", url="https://t.me/MALAYALAM_CHATTING")
                ]
            ]
        ),
    )
