# Тестовое задание для Luxoft

<details>
  <summary>Текст задания</summary>

    1. Реализовать автоматическое тестирование Blender 3.X.
    Blender 3.3 - https://www.blender.org/download/releases/3-3/
    Необходимо разработать программу, которая будет проверять работу Blender, исполняя
    несколько сценариев. Примеры:
        1. Создание произвольных фигур без материала.
        2. Создание произвольных фигур с материалом с различными параметрами.
        3. Использование различного освещение со сценариями из Пункта 2.
    На вход ожидаются аргументы:
    - blender_path – путь до исполняемого файла blender.exe
    - output_path – папка в которую будут сохраняться результаты тестирования.
    - x_resolution – ширина отрендеренного изображения.
    - y_resolution – высота отрендеренного изображения.
    На выходе ожидаются:
    - Отрендеренное изображение для каждого сценария
    - Лог рендера для каждого сценария.
    - JSON файл для каждого сценария, в котором будет:
        - Название теста (произвольное). o Дата и время запуска теста.
        - Дата и время окончания теста. o Длительность теста.
        - Информация о системе (CPU, RAM, название операционной системы).
    Необходимо самостоятельно продумать структуру проекта, реализацию тестов, а также быть готовым продемонстрировать и объяснить решение. Результаты работы необходимо опубликовать в публичном репозитории на GitHub и прислать ссылку.
    Полезные ссылки:
    https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html
    https://docs.blender.org/api/current/info_quickstart.html
</details>

## Установка и запуск

Этот этап предполагает, что на компьютере установлен Blender. Если нет, скачать программу можно [по ссылке] (https://www.blender.org/download/releases/3-3/).

Виртуальное окружение в проекте задано с помощью poetry. Установка poetry описана [здесь](https://python-poetry.org/docs/).

Клонируйте репозиторий
```
git clone git@github.com:mark-rom/luxoft-test-assignment.git
```
Перейдите в папку проекта
```
cd luxoft-test-assignment
```
Установите зависимости
```
poerty install
```

Команда для запуска
```
python run_tests.py --blender_path '<path/to/executable>' --output_path '<dirname>s' --x_resolution <resolution in pxls> --y_resolution <resolution in pxls>
```
Папка с результатами тестов будет создана в головной директории репозитория

Пример для MacOS
```
python run_tests.py --blender_path '/Applications/blender.app/Contents/MacOS/blender' --output_path 'test_results' --x_resolution 1000 --y_resolution 1000
```

## Технологии
- Python 3.10
- Blender API