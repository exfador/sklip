import os
import json
import random
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
import logging
import asyncio
from aiogram.types import ChatMemberUpdated
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter
from datetime import datetime
from keyboards import menu, back_menu, info_menu  


TOKEN = ''
ADMIN = 8029299947

CHAT_DATA_DIR = "chat_data"
if not os.path.exists(CHAT_DATA_DIR):
    os.makedirs(CHAT_DATA_DIR)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

bot = Bot(token=TOKEN)
dp = Dispatcher()

message_counters = {}

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    chat_id = message.chat.id
    json_file_path = os.path.join(CHAT_DATA_DIR, f"{chat_id}.json")

    logging.info(f"Команда /start от пользователя {message.from_user.id} в чате {chat_id}")

    if os.path.exists(json_file_path):
        if message.chat.type in {"group", "supergroup"}:
            await message.answer("Я уже есть в этом чате.")
        else:
            await message.answer("Жмякни хуесос, я только в чате работаю", reply_markup=menu)
    else:
        chat_data = {
            "chat_id": chat_id,
            "chat_type": message.chat.type,
            "title": message.chat.title or "Личный чат",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "text_channel": []
        }
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(chat_data, json_file, ensure_ascii=False, indent=4)

        await message.answer("Парацетамол не помог, это разочаровывает, что я теперь с Вами", reply_markup=info_menu)

@dp.callback_query(F.data == "help_me_please")
async def help_me_please_handler(callback_query: CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer(
"""Не жадничай, подкинь на чай со шпротами, а то без них он как-то скучноват!

монета USDT сеть TON -> <code>UQBPOrLLkGdhQq0nZ-lHCo_HCVgyYH_iMIrd2BNscKZKxAbS</code>
монета TON сеть TON -> <code>UQBPOrLLkGdhQq0nZ-lHCo_HCVgyYH_iMIrd2BNscKZKxAbS</code>""",
        reply_markup=back_menu, parse_mode='HTML'
    )

@dp.callback_query(F.data == "back")
async def help_me_please_handler(callback_query: CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer(
        "ахуеть, оказывается ты умный, что даже нажал на кнопку",
        reply_markup=menu,
    )
    
@dp.message()
async def save_message_handler(message: Message):
    chat_id = message.chat.id
    json_file_path = os.path.join(CHAT_DATA_DIR, f"{chat_id}.json")
    logging.info(f"Получено сообщение в чате {chat_id}: {message.text}")

    if chat_id not in message_counters:
        message_counters[chat_id] = 0
    message_counters[chat_id] += 1

    if os.path.exists(json_file_path):
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            chat_data = json.load(json_file)

        chat_data["text_channel"].append({
            "user_id": message.from_user.id,
            "username": message.from_user.username,
            "text": message.text,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(chat_data, json_file, ensure_ascii=False, indent=4)

        if message.text.lower().strip() == "склип":
            phrases = [
                "че тебе надо, урод?",
                "пошел ты нахер",
                "ты вообще кто такой, чтобы со мной разговаривать?",
                "позабавил, конечно",
                "блин, достал уже!",
                "не трогай меня, понял?",
                "чё тебе, блять?",
                "проваливай отсюда",
                "тебе не кажется, что ты надоел?",
                "иди к черту",
                "заткнись и уходи",
                "что-то ты слишком наглый",
                "нахера ты мне пишешь?",
                "чё, совсем оборзел?",
                "пошел в жопу",
                "иди в баню, не мешай",
                "ты че за тупой?",
                "слушай, иди на хрен",
                "пошел ты, я тебе не собеседник",
                "нахер ты мне нужен?",
                "все, мне надоело, проваливай",
                "не трогай меня, дебил",
                "блять, ты надоел",
                "что тебе, реально не понять?",
                "не лезь ко мне",
                "позабавил, иди к черту",
                "чего ты пристал, да?",
                "что за дебилизм, блять?",
                "зачем ты здесь вообще?",
                "на хрен ты мне вообще нужен?",
                "ну что тебе, придурок?",
                "пошел на хер, понял?",
                "что за херню ты несешь?",
                "ты че себе позволяешь?",
                "отвали, пошел нахер!",
                "почему ты мне вообще пишешь?",
                "не мешай, блять!",
                "ты с ума сошел?",
                "ну реально, иди нахуй",
                "чё ты на меня орешь, дебил?",
                "проваливай отсюда, понял?",
                "ты че, совсем охренел?",
                "заткнись, тупой кусок",
                "пойди, попрыгай где-нибудь еще",
                "иди лесом, идиот",
                "заткнись, урод",
                "пошел в жопу со своими вопросами",
                "ты кто такой вообще?",
                "еще раз напишешь – забаню, понял?",
                "че тебе не имется?",
                "нахрен тебе эти вопросы?",
                "смотри, как бы я не вырубил тебя",
                "пошел на хрен, петух",
                "прекрати доставать меня",
                "с кем ты разговариваешь вообще?",
                "не общайся со мной, понял?",
                "иди отсюда, дебил",
                "заткнись, надоел",
                "ты че мне тут мозги паришь?",
                "скажи, у тебя проблема с головой?",
                "пошел ты нахер со своими вопросами",
                "не трогай меня больше",
                "что тебе, придурок?",
                "смотри, как бы ты не огрёб",
                "на хрен иди отсюда",
                "отстань, блин",
                "еще раз — уйдешь в бан",
                "что тебе надо, а?",
                "ты не понял, да?",
                "давай, валяй отсюда",
                "скажи мне, кто тебе вообще дал право сюда лезть?",
                "на кой хрен ты мне пишешь?",
                "все, не разговариваю с тобой больше",
                "не нравишься ты мне, понял?",
                "с кем ты там разговариваешь вообще?",
                "че тебе, блять?",
                "ты кто такой вообще, чтобы так со мной общаться?",
                "иди отсюда, урод",
                "пошел ты, тупой",
                "хватит меня доставать, понял?",
                "мне плевать на твою ерунду",
                "заткнись и не задавай тупых вопросов",
                "кто ты такой, чтобы мне что-то тут писать?",
                "ты реально с ума сошел?",
                "иди к черту, надоел",
                "пошел на хрен со своими разговорами",
                "я тебя сейчас забаню, понял?",
                "не надо мне тут рассказывать, понял?",
                "скажи, ты тупой или специально?",
                "иди нахер, хватит меня трогать",
                "ты заебал со своими вопросами",
                "почему я должен тебе отвечать?",
                "блин, ты че, вообще охренел?",
                "отвали, не трогай меня",
                "не пиши мне больше",
                "пошел в жопу с этим вопросом",
                "че тебе от меня нужно, да?",
                "пошел нахер, я не с тобой разговариваю",
                "иди уже отсюда, что ты приперся?",
                "забей, не общаюсь с тобой",
                "заткнись, не до тебя",
                "мне плевать на твои проблемы",
                "пошел на хрен со своими вопросами",
                "иди к черту со своим бредом",
                "что ты от меня хочешь, тупой?"
            ]

            response = random.choice(phrases)
            await message.reply(response)
            return
        if "склип, пл" in message.text.lower() and "?" in message.text:
            response = random.choice(["пиздят как дышат", "факт нахуй"])
            await message.reply(response)
            return
        if "склип" in message.text.lower():
            if chat_data["text_channel"]:
                random_message = random.choice(chat_data["text_channel"])
                await message.reply(f"{random_message['text']}")
            return
        if message_counters[chat_id] >= random.randint(2, 10):
            message_counters[chat_id] = 0
            if chat_data["text_channel"]:
                random_message = random.choice(chat_data["text_channel"])
                await message.reply(f"{random_message['text']}")



async def main():
    logging.info("Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
