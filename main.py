import Config
import logging

from aiogram import Bot, Dispatcher, executor,types


logging.basicConfig(level=logging.INFO)


bot = Bot(token=Config.TOKEN)
dp = Dispatcher(bot)

db = Sqligther('db.db')

@dp.message_handler(commands=['subscribe'])
async  def subscribe(message: types.Message):
    if(not db.subscriber(message.from_user.id)):
        db.add_subscriber(message.from_user.id)
    else:
        db.update_subscription(message.from_user.id,True)
    await message.answer("Вы успешно подписались на рассылку!\nЖдите, скоро выйдут новые обзоры и вы узнаете о них!")

@dp.message_handler(commands=['unsubscibe'])
async def unsubscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id,False)
        await message.answer("Вы итак не подписаны")
    else:
        db.update_subscriptions(message.from_user.id,False)
        await message.answer("Вы успешно отписаны от рассылки")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)