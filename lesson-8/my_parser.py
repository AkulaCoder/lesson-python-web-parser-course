"""
🍰 ВЕСЁЛЫЙ ПАРСЕР — учимся доставать заголовок страницы с тортом
"""

import my_webdriver
import config
from bs4 import BeautifulSoup

class MyParser:
    """
    Класс для парсинга веб-страниц.
    Пока умеет только открывать сайт и читать заголовок.
    """

    def __init__(self, headless=False):
        print("🧠 Создаём парсер...")
        self.__driver = my_webdriver.MyWebdriver(headless=headless)
        self.url = ""
        self.html_page = ""
        print("✅ Парсер готов к работе!")

    def get_driver(self):
        """Возвращает драйвер (чтобы управлять браузером)"""
        return self.__driver

    def get_page(self, url):
        """
        Загружает страницу по ссылке и сохраняет её HTML-код
        """
        print(f"\n🌐 Загружаю страницу: {url}")
        try:
            self.get_driver().open_url(url=url)
            print("📄 Получаю HTML-код страницы...")
            self.html_page = BeautifulSoup(self.get_driver().get_page_source(), 'html.parser')
            self.url = url
            self.get_driver().quit()
            print("✅ Страница успешно загружена и закрыта!")
        except Exception as e:
            print(f"❌ Ошибка при загрузке страницы: {e}")
            self.url = ""
            self.html_page = None

    def get_page_title(self):
        """
        Извлекает заголовок страницы (тег <title>)
        """
        print("\n🔍 Ищу заголовок страницы...")
        try:
            title_tag = self.html_page.find('title')
            if title_tag:
                title = title_tag.get_text()
                print(f"🍰 Заголовок найден: {title}")
                return title
            else:
                print("⚠️ Заголовок не найден!")
                return "Без заголовка"
        except Exception as e:
            print(f"❌ Ошибка при извлечении заголовка: {e}")
            return "Ошибка при извлечении заголовка"


if __name__ == "__main__":
    print("\n🎉🎉🎉 ЗАПУСК ПАРСЕРА ДЛЯ ТОРТА 🎉🎉🎉\n")

    # Загружаем конфиг и получаем ссылку на торт
    conf = config.MyConfig()
    URL = conf.get_cake_url()
    print(f"🍰 Цель: торт по адресу {URL}\n")

    # Запускаем парсер в режиме без окон (headless=True)
    parser = MyParser(headless=True)

    # Загружаем страницу
    parser.get_page(URL)

    # Получаем и выводим заголовок
    title = parser.get_page_title()

    print("\n📢 РЕЗУЛЬТАТ РАБОТЫ:")
    print(f"🍰 Заголовок страницы: {title}")

    print("\n🎉 Готово! Парсер справился с задачей. Молодец!\n")
