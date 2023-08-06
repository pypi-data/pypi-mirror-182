""" Some Telethon functions """

async def get_user_telethon(message):
    try:
        args = message.text.split(" ", 1)[1].split(" ", 1)
    except IndexError:
        args = None
    if message.reply_to_msg_id:
        previous_message = await message.get_reply_message()
        user = await message.client.get_entity(previous_message.sender_id)
        extra = "".join(args) if args else ""
    elif args:
        extra = None
        x = args[0]
        if len(args) == 2:
            extra = args[1]
        if x.isnumeric():
            x = int(x)
        if not x:
            await message.reply("I don't know who you're talking about, you're going to need to specify a user...!")
            return
        try:
            x = await message.client.get_entity(x)
        except (TypeError, ValueError):
            await message.reply("Looks like I don't have control over that user, or the ID isn't a valid one. If you reply to one of their messages, I'll be able to interact with them.")
            return
    else:
        await message.reply("I don't know who you're talking about, you're going to need to specify a user...!")
        return
    return user, extra
