""" RiZoeLX 2022 © pyRiZoeLX """

from pyrogram.errors import MessageDeleteForbidden, RPCError

async def purge_(RiZoeL, message):
   if message.chat.id == message.from_user.id:
       return

   if message.reply_to_message:
        message_ids = list(range(message.reply_to_message.id, message.id))

        def divide_(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        _list = list(divide_(message_ids))

        try:
            for list in _list:
                await RiZoeL.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=list,
                    revoke=True,
                )
            await message.delete()
        except MessageDeleteForbidden:
            await message.reply_text("Cannot delete all messages. The messages may be too old, I might not have delete rights, or this might not be a supergroup.")
            return
        except RPCError as ef:
            await message.reply_text(f"Some error occured! \n\n **Error:** `{ef}`")
            return

        sah = await message.reply_text(f"Deleted __{len(message_ids)}__messages")
        await sleep(3)
        await sah.delete()
        return
   await message.reply_text("Reply to a message to start purge !")
   return
