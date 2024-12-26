from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

bot_start_menu = [
    [
        InlineKeyboardButton(text='Добавить меня', url='https://t.me/scleep_bot?startgroup=iris&admin=change_info+restrict_members+delete_messages+pin_messages+invite_users'),
        InlineKeyboardButton(text='Разработчик', url='https://t.me/exfador'),
    ],
    [
        InlineKeyboardButton(text='ТГК', url='https://t.me/coxerhub'),
        InlineKeyboardButton(text='Пожертвовать', callback_data='help_me_please'),
    ],
    [
        InlineKeyboardButton(text="FAQ", url='https://teletype.in/@exfador/8_cRBeMJFiP')
    ]
]
menu = InlineKeyboardMarkup(inline_keyboard=bot_start_menu)


back = [
    [
        InlineKeyboardButton(text='Домой', callback_data='back'),
    ]
]
back_menu = InlineKeyboardMarkup(inline_keyboard=back)


info_chat = [
    [
        InlineKeyboardButton(text='Разработчик', url='https://t.me/exfador'),
        InlineKeyboardButton(text='ТГК', url='https://t.me/coxerhub'),
    ],
    [
        InlineKeyboardButton(text="FAQ", url='https://teletype.in/@exfador/8_cRBeMJFiP')
    ]
]
info_menu = InlineKeyboardMarkup(inline_keyboard=info_chat)
