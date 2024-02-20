from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
import random
from API.api import get_random_duck
from filter.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

should_repeat = False

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Hello my dear friend {message.from_user.full_name}. I'm your personal telegram-bot!")

@user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    if not should_repeat:
        await message.answer("Menu : \n1. /menu \n2. /help \n3. /echo \n4. /start \n5. /duck")
    else:
        await message.answer("You can't do this in echo mode")

@user_private_router.message(Command("help"))
async def help_cmd(message: types.Message):
    if not should_repeat:
        await message.answer("\n1. /menu - Send menu \n2. /help - Send this message \n3. /echo - Activate echo \n4. /start - Activate ChatBot \n5. /duck - Summon duck")
    else:
        await message.answer("You can't do this in echo mode")

@user_private_router.message(Command("echo"))
async def echo_start(message: types.Message):
    global should_repeat
    if not should_repeat:
        should_repeat = True
        await message.answer("Input /stop for stop")
    else:
        await message.answer("You are already in echo mode")

@user_private_router.message(Command("stop"))
async def echo_stop(message: types.Message):
    global should_repeat
    if should_repeat:
        should_repeat = False
        await message.answer("Echo stopped.")
    else:
        await message.answer("Echo is not active.")

@user_private_router.message(Command("duck"))
async def duck_cmd(message: types.Message):
    if not should_repeat:
        url = get_random_duck()
        await message.answer_photo(url)
    else:
        await message.answer("You can't do this in echo mode")

@user_private_router.message(F.text.lower().contains("pay"))
async def pay_method(message: types.Message):
    if not should_repeat:
        await message.answer("You can pay for this in such method")
    else:
        await message.answer("You can't do this in echo mode")

@user_private_router.message()
async def echo_handle(message: types.Message):
    global should_repeat
    if should_repeat:
        await message.answer(message.text)

# @user_private_router.message()
# async def echo(message: types.Message):
#     text = message.text
#     if text in ["Hi", "Hello", "Привіт", "Здоровенькі були"]:
#         await message.answer(f"Hello {message.from_user.full_name}")
#         await message.answer(random.choice(["Hi", "Hello", "Привіт", "Здоровенькі були"]))
#     elif text in ["Goodbye", "Bye", "Бувай", "Пака"]:
#         await message.answer(f"Goodbye {message.from_user.full_name}")
#         await message.answer(random.choice(["Goodbye", "Bye", "Бувай", "Пака"]))
#     else:
#         await message.reply("I don`t understand you")
