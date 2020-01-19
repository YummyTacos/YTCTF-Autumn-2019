from websockets import serve as ws_serve, ConnectionClosed  # pip install websockets
from datetime import datetime, timedelta
from time import gmtime
import asyncio
import logging

users = {}
flood_limit = {}
FLOOD_TIME = timedelta(seconds=1)
FLAG = 'ytctf{This_should_not_happen_but_I_can_do_XSS_via_w3bs0ket_haha}'
FLAG_USER = 'flag'
FLAG_PASSWORD = 'FlagIsNotEzToGet...TooHard4ME'

logging.Formatter.converter = gmtime
logging.basicConfig(level=logging.INFO, style='{', datefmt='%Y-%m-%d %H:%M:%S UTC',
                    format='[{levelname:<8}] [{asctime}] ({name}): {message}')
msg_log = logging.getLogger(__name__).getChild('message')
logging.getLogger('websockets').setLevel(logging.INFO)


def escape_html(html):
    return html.replace('<', '&lt;').replace('>', '&gt;')


async def login(ws):
    while True:
        name = await hello(ws)
        if len(name) > 32:
            await ws.send('Нельзя использовать имя длиннее 32 символов.')
            await ws.close()
        if name == '':
            await ws.send('Нельзя установить пустое имя.')
            await ws.close()
        if name in users or name == FLAG_PASSWORD:
            await ws.send('Имя пользователя занято.')
            await ws.close()
        if name == FLAG_USER:
            await ws.send('Введи пароль: ')
            password = await ws.recv()
            if password != FLAG_PASSWORD:
                msg_log.info(f'Введён неверный пароль от {FLAG_USER}')
                await ws.send('Неверный пароль.')
                await ws.close()
        if name in users:
            await ws.send('Имя пользователя занято.')
            await ws.close()
        new_name = escape_html(name)
        if new_name != name:
            await ws.send('Форматирование имён запрещено на сервере.')
            await ws.close()
        name = new_name
        break
    await ws.send(f'Привет и добро пожаловать в наш чат, {name}! Напиши /help для справки.')
    await send_all(f'{name} присоединился к чату.')
    return name


async def logout(name):
    if name not in users:
        return
    users.pop(name)
    await send_all(f'{name} покинул чат.')


async def hello(ws):
    await ws.send('Введи имя пользователя:')
    name = await ws.recv()
    return name


async def send_all(msg, name=None):
    text_log = msg
    text = msg
    if name is not None:
        text_log = f'{name} ({name.encode()}): {text_log}'
        text = f'{name}: {text}'
    msg_log.info(text_log)
    msg = f'[{datetime.utcnow().replace(microsecond=0)}] {text}'
    fut = [ws for name, ws in users.items()]
    if not fut:
        return
    await asyncio.wait([ws.send(msg) for ws in fut])


async def process_message(text, name):
    if not text.startswith('/'):
        return False
    command, *args = text[1:].split(' ')
    ws = users[name]
    msg_log.info(f'{name} ({name.encode()}) использовал команду {text}.')
    if command == 'help':
        return await ws.send(
            f'Доступные команды:\n'
            f'- /help — эта справка\n'
            f'- /pm [user] [message] — отправить личное сообщение [message] пользователю [user]\n'
            f'- /flag — получить флаг (доступно только пользователю {FLAG_USER})\n'
            f'- /users — получить список подключенных к серверу')
    if command == 'pm':
        if len(args) < 1:
            return await ws.send('Недостаточно аргументов! Использование: /pm [user] [message]')
        target_user = args[0]
        if users.get(target_user) is None:
            return await ws.send(f'"{target_user}" — такого пользователя нет в чате!')
        target_ws = users[target_user]
        if len(args) == 1:
            text = f'{name} что-то прошептал тебе, но ты ничего не услышал'
            self_text = f'Ты что-то прошептал {target_user}, но он ничего не услышал'
        else:
            msg = ' '.join(args[1:])
            text = f'{name} шепчет тебе: {msg}'
            self_text = f'Ты шепчешь {target_user}: {msg}'
        await ws.send(self_text)
        return await target_ws.send(text)
    if command == 'flag':
        if name == FLAG_USER:
            msg_log.warning(f'{name} ({name.encode()}) получил флаг!')
            return await ws.send(FLAG)
        return await ws.send(f'Доступ к этой команде имеет только {FLAG_USER}')
    if command == 'users':
        return await ws.send('Пользователи в чате:\n- ' + '\n- '.join(users.keys()))
    if command == 'ban':
        if name == FLAG_USER:
            if len(args) < 1:
                return await ws.send('Недостаточно аргументов! Использование: /ban [user]')
            target_user = args[0]
            if users.get(target_user) is None:
                return await ws.send(f'"{target_user}" — нет такого пользователя в чате!')
            target_ws = users[target_user]
            await target_ws.send('Не, ну это бан.')
            msg_log.info(f'{name} ({name.encode()}) был забанен.')
            await target_ws.close()
            return await ws.send(f'Пользователь {target_user} кикнут!')
    return await ws.send(f'"/{command}" — команда не найдена. Напиши /help для справки.')


async def chat(ws, room):
    try:
        name = await login(ws)
    except ConnectionClosed:
        return
    try:
        users[name] = ws
        async for msg in ws:
            if msg == '':
                continue
            if datetime.utcnow() - flood_limit.get(name, datetime(1970, 1, 1)) < FLOOD_TIME:
                await ws.send('Флуд в чате запрещён.')
                msg_log.info(f'{name} ({name.encode()}) кикнут за флуд.')
                await ws.close()
                break
            flood_limit[name] = datetime.utcnow()
            if name == FLAG_USER:
                flood_limit.pop(name)
            if await process_message(msg, name) is not False:
                continue
            if len(msg) >= 512:
                if len(msg) <= 4096:
                    await ws.send('Сообщение не может быть длиннее 512 символов.')
                continue
            if 'ytctf' in msg.lower():
                msg_log.info(f'{name} ({name.encode()}) пытался отправить флаг.')
                await ws.send('Я сервер простой: вижу флаг — удаляю.')
                continue
            new_msg = escape_html(msg)
            if new_msg != msg:
                await ws.send('Для предотвращения флуда, форматирование текста в общем чате'
                              ' запрещено.')
                continue
            msg = new_msg
            await send_all(msg, name)
    except ConnectionClosed:
        pass
    except Exception as e:
        await ws.send(f'На сервере произошла ошибка: {e.__class__}: {e}')
        raise
    finally:
        await logout(name)


srv = ws_serve(chat, '0.0.0.0', 8080)
asyncio.get_event_loop().run_until_complete(srv)

if __name__ == '__main__':
    asyncio.get_event_loop().run_forever()
