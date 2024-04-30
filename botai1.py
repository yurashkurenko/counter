from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode                  
#from aiogram import Bot, Dispatcher, executor, types#from aiogram.contrib.middlewares.logging import LoggingMiddleware
import shelve
from vedis import Vedis
from config import TOKEN
# Конфигурация бота
#API_TOKEN = 'YOUR_API_TOKEN_HERE'
API_TOKEN =TOKEN
DATABASE = 'devices.vdb'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
#dp.middleware.setup(LoggingMiddleware())

# Вспомогательные функции для работы с Vedis
def db_get_device_list(user_id):
    with Vedis(DATABASE) as db:
        try:
            devices = db[f"devices_{user_id}"].decode().split(';')
            return devices
        except KeyError:
            return []

def db_add_device(user_id, device_info):
    with Vedis(DATABASE) as db:
        devices = db_get_device_list(user_id)
        devices.append(device_info)
        db[f"devices_{user_id}"] = ';'.join(devices)

def db_remove_device(user_id, device_id):
    with Vedis(DATABASE) as db:
        devices = db_get_device_list(user_id)
        devices = [d for d in devices if d.split(',')[0] != device_id]
        db[f"devices_{user_id}"] = ';'.join(devices)

def db_get_device(user_id, device_id):
    with Vedis(DATABASE) as db:
        devices = db_get_device_list(user_id)
        for device in devices:
            if device.split(',')[0] == device_id:
                return device
        return None

# Обработчики команд

# Если не указать фильтр F.text,
# то хэндлер сработает даже на картинку с подписью /test
@dp.message(F.text, Command("test"))
async def any_message(message: Message):
    await message.answer(
        "Hello, <b>world</b>!",
        parse_mode=ParseMode.HTML
    )
    await message.answer(
        "Hello, *world*\!",
        parse_mode=ParseMode.MARKDOWN_V2
    )





@dp.message(Command(commands=['start', 'help']))
async def send_welcome(message: Message):
    await message.reply("Привет! Я бот для управления устройствами снятия показаний.\n Используйте команды:\n"
                        "/add_device <id>,<wifi>,<polling> - Добавить устройство\n"
                        "/delete_device <id> - Удалить устройство\n"
                        "/list_devices - Показать список устройств\n"
                        "/get_device <id> - Получить информацию об устройстве")


#@dp.message(Command(commands=['add_device']))
#async def add_device(message: Message):
#async def add_device(message: types.Message,
#                        command: CommandObject):
#    args = command.args
#    await message.answer(args)


#    print('Добавление устройства')
#    await message.reply('Добавление устройства')
#    print(message)
#    args = message.get_args().split(',')
 #   if len(args) != 3:
 #       await message.reply("Неверные аргументы. Используйте формат <id>,<wifi>,<polling>")
 #       return
#    db_add_device(message.from_user.id, ','.join(args))
#    await message.reply("Устройство добавлено!")


#@admin_router.message(Command('info'))
#async def get_user_info(message: type.Message,
#                        command: CommandObject):
#    args = command.args
#    await message.answer(args)

@dp.message(Command(commands=['add_device']))
async def add_device(message: Message):
    #args = command.args
    #print(message.chat.id)
#    print(message.text)
    args=message.text.split(' ')[1]
    args=args+','+str(message.from_user.id)+','+str(message.chat.username)
    db_add_device(message.from_user.id, args)
    await message.reply("Устройство добавлено!")
#    print(str(message))
#    id=args.split(',')[0]
#    print(id)
#    wifi=id=args.split(',')[1]
#    print(wifi)
#    polling=args.split(',')[2]
#    print(polling)
#/add_device <id>,<wifi>,<polling> - Добавить устройство
#db_add_device(user_id, device_info)
#    await message.answer(args)
#    db_add_device(message.from_user.id, ','.join(args))
#args=str(massage.user_id)+','+str(massage.chat_id)+','+args
#    db_add_device(message.from_user.id, args)
#    await message.reply("Устройство добавлено!")
#    print(message.text)

#@dp.message(Command(commands=['add_device']))
#async def get_device(message: Message):
#    print(message.text)
#    device_id = message.get_args()
#    print(message.text)
#    device_info = db_add_device(message.from_user.id, device_id)
#    if device_info:
#        await message.reply(f"Информация об устройстве: {device_info}")
#    else:
#        await message.reply("Устройство не найдено.")

@dp.message(Command(commands=['delete_device']))
async def delete_device(message: Message):
    args=message.text.split(' ')[1]
    device_id = args
    if not device_id:
        await message.reply("Укажите ID устройства.")
        return
    db_remove_device(message.from_user.id, device_id)
    await message.reply("Устройство удалено!")

@dp.message(Command(commands=['list_devices']))

async def list_devices(message: Message):
    devices = db_get_device_list(message.from_user.id)
    if not devices:
        await message.reply("Список устройств пуст.")
        return
    response = "\n".join(devices)
    await message.reply(f"Ваши устройства:\n{response}")

@dp.message(Command(commands=['get_device']))
async def get_device(message: Message):
    args=message.text.split(' ')[1]
    device_id = args
    device_info = db_get_device(message.from_user.id, device_id)
    if device_info:
        await message.reply(f"Информация об устройстве: {device_info}")
    else:
        await message.reply("Устройство не найдено.")

#if name == 'main':
#    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    dp.run_polling(bot)