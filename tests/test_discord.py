import time
import re
from appium.webdriver.common.appiumby import AppiumBy


def test_discord(app):
    app.dis.login_in()
    app.dis.press_permission_button('deny')
    app.dis.select_discord_group("HELLDIVERS™ Official Discord")
    app.dis.select_group_channel("troubleshooting")
    app.dis.go_to_last_message()

    templates = {
        "$dism": '../instructions/Information/Check and repair System Data.md',
        "$cache": '../instructions/Information/Clear Nvidia Shader.md',
        "$dx11": '../instructions/Information/DirectX11.md',
        "$performance": '../instructions/Information/Performance + Settings.md',
        "$support": '../instructions/Information/Help Template.md',
        "$ctd": '../instructions/Problems/Crashes/Crashes to Desktop.md',
        "$crashstart": '../instructions/Problems/Crashes/Crash on Startup.md',
        "24h2": '../instructions/Problems/Crashes/Windows 11 24H2 Gaming Fix.md'
    }

    last_used_tag = None  # хранит последний использованный тег
    while True:
        try:
            any_tags_found = False
            message_log = app.dis.get_message_list(start=-2)  # словарь сообщений
            for message in message_log:   # Анализируем каждое сообщение
                parts = message.split(':', maxsplit=1)
                name, text = parts[0], parts[1]
                for tag, file_path in templates.items():
                    # print(re.match(r'^KoHb \[418th] КСЗ Жеребец Истины', name))
                    # if tag in text.lower() and re.match(r'^KoHb \[418th] КСЗ Жеребец Истины', name):
                    if tag in text.lower():  # Проверяем известные теги в сообщениях
                        any_tags_found = True  # если у нас был хоть 1 тег, то историю не обнуляем
                        if tag != last_used_tag:  # Только если тэг отличается от последнего активного
                            app.dis.click_on_message_input()  # жмём на ввод, вводим сообщение которое привязано к тексту, жмём отправить
                            with open(file_path, 'r', encoding='utf-8') as md_file:
                                additional_text = f'response on tag from {name}: \n'
                                response = md_file.read()
                            app.dis.enter_message(additional_text+response)
                            app.dis.click_on_send_message()
                            last_used_tag = tag  # Запоминаем новый активный тег
                            # print(last_used_tag)
                            time.sleep(1)  #35 это 30 + запас, 30 это таймаут в канале
                            break
            if not any_tags_found:  # Если в последних сообщениях не обнаружено ни одного тега, очищаем текущий тег
                last_used_tag = None

            # print(message_log)
            # break
        except Exception as e:
            # print(e, flush=True)
            raise Exception from e

def test_get_last_message_data(app):
    app.dis.login_in()
    app.dis.press_permission_button('deny')
    app.dis.select_discord_group("HELLDIVERS™ Official Discord")
    app.dis.select_group_channel("troubleshooting")
    app.dis.go_to_last_message()
    from pprint import pprint
    pprint(app.dis.get_message_list())