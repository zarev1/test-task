def auth(func):
    async def wrapper(message):
        access_allowed = []#<< Сюда над чтобы попадали auth из конфига
        if str(message['from']['id']) not in access_allowed:
            return await message.reply(f'Access Denied [401]', reply=False)
        return await func(message)
    return wrapper
