import logging
from aiogram import Bot, Dispatcher, types

# تفعيل سجل الأخطاء في الكونسول
logging.basicConfig(level=logging.INFO)

# استبدال "TOKEN" بتوكن البوت الخاص بك
bot = Bot(token="6391905722:AAEiZbF2xyO6Xz0m_TKoWV2wWNaATcaooCw")
dispatcher = Dispatcher(bot)

@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    # إرسال الرسالة الأولى
    await message.reply("مرحبًا! التحقق من الزر التالي:", reply_markup=types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton("الزر الشفاف", callback_data='transparent_button')
    ))

@dispatcher.callback_query_handler(lambda c: c.data == 'transparent_button')
async def transparent_button_callback(callback_query: types.CallbackQuery):
    # إجراء عند الضغط على الزر الشفاف
    await bot.answer_callback_query(callback_query.id, text="لقد ضغطت على الزر الشفاف.")

# تشغيل البوت
async def main():
    await dispatcher.start_polling()

if __name__ == '__main__':
    # تشغيل الدالة الرئيسية
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
