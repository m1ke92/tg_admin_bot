import random

from aiogram.types.chat_permissions import ChatPermissions
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


question_text = 'Добро пожаловать! У вас есть 5 минут чтобы доказать, что вы не спамер!\n\n' \
                'Сколько плюсов в названии группы?'

right_button_text = '2'
answer_query_wrong_button = 'Неверно, осталась одна попытка.'
answer_query_right_user = 'Добро пожаловать!'

wrong_answers = [
    'Я бы на твоем месте застрелился.',
    'Ну нажал. Легче стало?',
    'Угадай, кто только что подтвердил что он дегенерат?',
    'Чтоб у тебя этот палец отсох!',
    'Тест на пидора успешно пройден. Поздравляем, ты пидор! ',
    'Ты не спамер, ты сильно хуже. Ты мудак с геном петросяна.',
    'За тобой уже выехали, шутист.',
    'Анус себе потыкай, пёс!',
    'Игорь, ты?',
    'Я смотрю, папа не старался, и ты теперь за него компенсируешь, постоянно тыкая все подряд?',
    'Таким как ты нужно гвоздь в голову вбивать при рождении.',
    'И ты видимо считаешь, что это афигенно смешно?',
    'Так и запишем: помогал ботам.',
    'Хочешь, всем расскажу, чем ты тут занимаешься?',
    'Не твоя, вот ты и бесишься.',
    'Ваш диагноз - патологическая гипоэнцефалокарния.',
    'Чтоб тебе всю жизнь на одну и ту же кнопку жать.',
    'Не думал о карьере фронтендера? Ты бы подошел.',
    'Дружище, это не лифт, здесь каждый сам за себя.',
    'У меня во дворе за такое убивают нахуй.',
    'Еще раз – и ты пидорас.',
    'Кролик с аватары этого чата гораздо умнее тебя. Гораздо умнее. Гораздо!',
    'Ты кажется можешь посоревноваться в интеллекте с хасой, которую кролик с аватары ест.',
    'Нет, ну вы посмотрите на этого поца. Тыкает куда ни попадя!',
    'А тот кто будет тыкать эту кнопку - тому фурункул вскочит на живот!',
    'Повар спрашивает повара: нахуя ты тыкаешь эту кнопку?'
    '',
]

RESTRICT_PERMISSIONS = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False
    )
ALLOW_PERMISSIONS = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True
    )


def get_keyboard(user_id: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.row_width = 5
    answers = list(range(5))

    random.shuffle(answers)

    buttons = []

    for answer in answers:
        buttons.append(InlineKeyboardButton(
            text=answer,
            callback_data=f'{user_id}:{answer}'
        ))
    kb.add(*buttons)

    return kb
