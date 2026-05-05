from aiogram import Router, types
from aiogram.filters import Command
from bot import db, farmgen

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user = await db.get_user(message.from_user.id)
    if user is None:
        img_url = farmgen.get_farm_img_url()
        await db.create_user(message.from_user.id, message.from_user.username, img_url)
        await message.answer_photo(photo=img_url, caption="Добро пожаловать на вашу ферму!")
    else:
        await message.answer("Вы уже зарегистрированы! Используйте /farm чтобы увидеть ферму.")

@router.message(Command("farm"))
async def cmd_farm(message: types.Message):
    user = await db.get_user(message.from_user.id)
    if user and user[3]:
        await message.answer_photo(photo=user[3], caption="Ваша ферма")
    else:
        await message.answer("Сначала зарегистрируйтесь: /start")

@router.message(Command("balance"))
async def cmd_balance(message: types.Message):
    user = await db.get_user(message.from_user.id)
    if user:
        await message.answer(f"Ваш баланс: {user[2]} монет")
    else:
        await message.answer("Сначала зарегистрируйтесь: /start")
