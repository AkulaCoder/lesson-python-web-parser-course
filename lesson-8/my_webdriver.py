"""
my_webdriver.py — умный браузер с Selenium
Делает скриншоты, ждёт загрузку страницы и радуется жизни 🎉
"""

import time
import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyWebdriver:
    """
    Класс для управления браузером через Selenium WebDriver.
    Умеет открывать сайты, ждать загрузку, делать скриншоты и радоваться результату 🎈
    """

    def __init__(self, headless=False):
        """
        Инициализация драйвера.
        headless=True — браузер работает в фоне (без окон) 🤫
        headless=False — ты увидишь, как открывается браузер 👀
        """
        self.headless = headless
        print("🚀 Запускаю браузер...")
        self.__driver = self._start_driver()
        print("✅ Браузер готов к работе!")

    def _start_driver(self):
        """
        Настройка браузера: user-agent, headless-режим, отключение лишних фич.
        """
        conf = config.MyConfig()
        options = Options()

        if self.headless:
            options.add_argument("--headless")
            print("🕶️ Включён headless-режим (браузер работает в фоне)")

        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"user-agent={conf.get_user_agent()}")

        driver = webdriver.Chrome(options=options)
        return driver

    def get_driver(self):
        """Возвращает объект драйвера (чтобы делать с ним всякие штуки)"""
        return self.__driver

    def open_url(self, url):
        """
        Открывает указанный URL.
        Ждёт, пока страница полностью загрузится (хитрое ожидание до 15 секунд).
        """
        print(f"🌐 Открываю URL: {url}")
        self.get_driver().get(url)

        print("⏳ Жду полной загрузки страницы...")
        WebDriverWait(self.get_driver(), 15).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        print("✅ Страница загружена!")

    def get_page_source(self):
        """Возвращает HTML-код страницы"""
        return self.get_driver().page_source

    def close(self):
        """Закрывает текущую вкладку (но не весь браузер)"""
        self.get_driver().close()
        print("🚪 Вкладка закрыта")

    def quit(self):
        """Полностью завершает работу браузера"""
        self.get_driver().quit()
        print("👋 Браузер закрыт. Пока!")

    def take_screenshot(self, file_path):
        """
        Делает скриншот страницы.
        Сначала ждёт 1 секунду (для надёжности), потом сохраняет картинку.
        """
        print(f"📸 Делаю скриншот и сохраняю в '{file_path}'...")
        time.sleep(1)  # небольшая задержка для полной отрисовки
        self.get_driver().save_screenshot(file_path)
        print(f"✅ Скриншот сохранён! 🎉")

if __name__ == "__main__":
    import random

    print("\n✨✨✨ Добро пожаловать в Selenium-парсер ✨✨✨\n")

    # Загружаем конфиг и получаем URL торта
    conf = config.MyConfig()
    URL = conf.get_cake_url()
    print(f"🍰 Сегодня работаем с тортом: {URL}\n")

    # Запускаем браузер
    my_webdriver = MyWebdriver(False)

    # Открываем страницу с тортом
    my_webdriver.open_url(URL)

    # Генерируем имя файла: screen_ + 5 случайных цифр
    random_num = random.randint(10000, 99999)
    screenshot_name = f"screen_{random_num}.png"

    # Делаем скриншот
    my_webdriver.take_screenshot(screenshot_name)

    # Закрываем браузер
    my_webdriver.quit()

    print(f"\n🎉 Готово! Скриншот '{screenshot_name}' сохранён.\n")
