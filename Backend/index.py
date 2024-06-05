import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

def run_selenium_chrome() -> WebDriver:
	return webdriver.Chrome(
		service = Service(ChromeDriverManager().install()),
		keep_alive = True,
		options = webdriver.ChromeOptions().add_experimental_option(
			name = 'detach',
			value = True,
		)
	)

if __name__ == '__main__':
	logging.basicConfig(
		level = logging.INFO,
		format = '[{levelname}]: {message}',
		style = '{'
	)

	browser: WebDriver = run_selenium_chrome()
	browser.get(url = 'https://www.google.co.jp')

	browser.quit()
	logging.info(msg = '処理が正常に終了しました。')