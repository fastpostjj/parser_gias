from selenium import webdriver as wd

# URL = "https://selectel.ru/blog/courses/"
URL = "https://gias.by/gias/#/"

browser = wd.Chrome("/usr/bin/chromedriver/")

# В большинстве случаев достаточно User-Agent и Accept.
# Первый заголовок поможет сымитировать, что мы реальный пользователь,
# который работает из браузера. Второй — укажет, что мы хотим получить
# от веб-сервера гипертекстовую разметку.

st_accept = "text/html" # говорим веб-серверу,
                        # что хотим получить html
# имитируем подключение через браузер Mozilla на macOS
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}


# отправляем запрос с заголовками по нужному адресу
req = requests.get(URL, headers)
# считываем текст HTML-документа
src = req.text
print(src)
