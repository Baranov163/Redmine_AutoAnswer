from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://redmine.r77.center-inform.ru/projects")
search_box = driver.find_element(By.NAME, value="username")
search_box.send_keys("n.baranov")
search_box1 = driver.find_element(By.NAME, value="password")
search_box1.send_keys("BARash%123")
button = driver.find_element(By.NAME, value="login")
button.click()

driver.get("https://redmine.r77.center-inform.ru/issues/...../edit")
button_status = driver.find_element(By.XPATH, "//select[@name='issue[status_id]']/option[text()='Выполнено']")
button_status.click()
button_name = driver.find_element(By.XPATH, "//select[@name='issue[assigned_to_id]']/option[text()='Кольцова Анастасия ']")
button_name.click()
input_text = driver.find_element(By.NAME, value="issue[notes]")
input_text.send_keys("Добрый день!")
input_text.send_keys(Keys.RETURN)
input_text.send_keys("На текущий момент по указанной справке расхождения отсутствуют.")
input_text.send_keys(Keys.RETURN)
input_text.send_keys("Рекомендуем запросить остатки повторно и проверить актуальность проблемы.")
input_text.send_keys(Keys.RETURN)
input_text.send_keys("Если вопрос по остаткам не решён, необходимо предоставить ответ на запрос остатков, а также ответ на запрос штрихкодов по справке Б строго из системы ЕГАИС с указанием конкретных данных, по которым выявлены расхождения.")
input_text.send_keys(Keys.RETURN)
input_text.send_keys("Если после ответа по Вашему обращению у Вас не осталось вопросов и проблема неактуальна, Вы можете самостоятельно закрыть заявку.")
button_commit = driver.find_element(By.NAME, value="commit")
button_commit.click()

time.sleep(4)
driver.quit()





