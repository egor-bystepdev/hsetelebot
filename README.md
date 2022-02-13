# hsetelebot

## Выполнил Бочаров Егор Николаевич, группа 203
Настроил CI/CD через github actions.
В данный момент бот отключён.
Бот распознаёт текст с картинки с помощью библиотеки pytesserac, не всегда успешно, но выдаёт.
Пример:

<img src="https://i.ibb.co/s2p7b0V/2021-12-14-00-14-54.jpg" width="400" height="400" />

Оказывается телеграм недавно тоже добавил такую возможность, можно сравнить результаты:

<img src="https://i.ibb.co/qdS0M6J/2021-12-14-00-18-33.jpg" width="250" height="400" /> <img src="https://i.ibb.co/SQgDL0B/2021-12-14-00-18-38.jpg" width="250" height="400" />

Бот запущен на aws, использовал watchtower, [ссылка на docker-compose](https://github.com/egor-bystepdev/hsetelebot/blob/main/utils/docker-compose.yaml)
