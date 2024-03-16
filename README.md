# Описание проекта

Основная идея проекта заключается в реализации сервиса, позволяющего любому, даже самому маленькому магазину выйти на доставку,
а так же любому желающему человеку, в любой момент стать курьером у ближайших магазинов. Магазину будет доступна массовая
выгрузка товаров и продвинутая система отчетов по продажам.

Реализуется система моментальной регистрации курьеров, всё что нужно - зайти в телеграм бота, отправить трансляцию местоположения,
и получить ближайший заказ. (Продумывается система защиты от недобросовестных курьеров)

Для клиентов доставки создаётся система трекинга заказов, которая позволяет рассчитывать время, через которое заказ прибудет
а так же отслеживать местоположение курьера.



## Функционал

На данный момент, в проекте реализован следующий функционал:
- CRUD-функционал для работы с основными сущностями
- Сервис валидации загружаемых данных
- Гибкая система permission-ов
- Поиск товаров
- Система скидок, заказов и отзывов
- Ведется разработка системы периодических отчетов по продажам для магазинов
- Реализована регистрация курьеров и система трекинга их действий

## Сущности

### Магазин

Для управления магазином реализована логика управления permission-ами. Владелец магазина может создавать сущности менеджеров, которых можно наделять различными правами.

### Продукт

Реализована логика валидации каждого продукта. Проверка на содержание запрещенных слов и другие аспекты.

### Заказ

Реализована mock система оплаты и многоступенчатая система валидации заказа перед оплатой.

### Доставка

### Курьер

На данный момент есть сырая реализация регистрации в боте, трекинга местоположения, выхода на линию, получения заказ, 
завершения заказа с получением награды, выхода с линии.

## Инфраструктура

Для разворачивания инфраструктуры приложения используется Docker Compose.
Для ускорение процесса разработки написан Makefile со скриптами часто используемых сценариев.

### Хранилища

- PostgreSQL - основная база данных
- Redis - для кеша и в качестве message брокера для Celery

### Фоновые задачи

- Celery - для обеспечения скорости работы приложения. Многие операции, которые потенциально могут нести высокие
нагрузки выведены в background задачи.

### Курьерское приложение

- Telegram Bot - обеспечивает очень удобную и быструю процедуру регистрации в качестве курьера для любого желающего заработать, а также
удобный инструмент для отслеживания действий курьеров.

## Стиль написания

При разработке придерживаюсь best-practise в разработке REST API, использую шаблоны проектирования и следую принципам SOLID, DRY, KISS.
Настроены pre-commit хуки, линтеры для поддержания единообразия стиля кода и обнаружения ошибок на ранних этапах разработки.

## Оптимизация

Проводится оптимизация SQL запросов. 
Исправлены n+1 ошибки, исправлено избытычное обращение к базе данных.

## Тестирование

Написание кода ведется с учетом TDD, каждая логическая строка кода сначала покрывается юнит тестами.

### Тестирование загрузки товаров для магазина
- На данный момент проведено тестирование в условиях загрузки таблицы со 100000 продуктов и 
валидацией каждого из продуктов - клиент не заметил никаких изменений в работе приложения. (В дальнейшем планируется автоматизация
повышения выделяемых ресурсов и количества worker-ов при увелечении нагрузок на сервис)


