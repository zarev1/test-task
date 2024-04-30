from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

import Auth
from keyboard.kb_all_course import get_all_course
from keyboard.kb_all_test import get_all_test
from keyboard.only_kb_start import only_start
from db.read import get_test_id, answers
from states.answer_states import Answers
from log import logger


"""=================================="""
"""              Ответ               """
"""=================================="""

@Auth
async def course(message: types.Message):
    await message.answer(
        "Введите названия предмета:\n\n"
        "P.S. Ниже кнопки со всеми предметами",
        reply=False,
        reply_markup=await get_all_course()
    )

    await Answers.Course.set()


@Auth
async def test(message: types.Message, state: FSMContext):
    tg_course = message.text
    await state.update_data(course=tg_course)

    await message.answer(
        "Введите названия теста:\n\n",
        reply=False,
        reply_markup=await get_all_test(tg_course)
    )
    
    await Answers.Test.set()

@Auth
async def answer(message: types.Message, state: FSMContext):
    data = await state.get_data()
    course = data.get('course')
    tg_test = message.text

    test_id = await get_test_id(tg_test)
    get_answer = await answers(test_id)

    await message.answer(
        f"{course}\n\n"
        f"{tg_test}\n\n"
        f"{get_answer}\n",
        reply=False,
        reply_markup=only_start
    )

    await state.finish()


"""=================================="""
"""         Register 'Ответ'         """
"""=================================="""


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(course, commands=['Ответ'])
    dp.register_message_handler(test, state=Answers.Course)
    dp.register_message_handler(answer, state=Answers.Test)

