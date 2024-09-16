# 🚭 Обнаружение курения в запрещенных зонах

## 📄 Обзор
Цель проекта — обучить модель **YOLOv8** для обнаружения факта курения в запрещенных зонах на основе скриншотов с камер видеонаблюдения. Это поможет контролировать соблюдение политики запрета курения и повысить эффективность ее исполнения.

### 🏆 Участие в хакатоне
Проект был создан в рамках **Nuclear-hack 2024**.  
**Кейс:** Детекция курильщиков в запрещенных зонах.

## 🔍 Ход работы
Для начала мы использовали доступные в интернете датасеты и обучили модель на их основе. В нашем наборе данных было около **3000 размеченных изображений**, к которым мы добавили еще **1000 изображений с собственной разметкой**. Однако, после обучения результаты оказались недостаточными — сигареты на предоставленных заказчиками изображениях обнаруживались слабо. Проблемы возникли из-за низкого качества некоторых изображений: из 3000 картинок **76 изображений** были замылены, что привело к снижению точности модели.

<p align="center">
  <img src="https://github.com/dmmmit/smoking_detection/blob/main/source/metrics/BigDataMetrica1.jpg" alt="Метрика-1" style="width: 30%;">
  <img src="https://github.com/dmmmit/smoking_detection/blob/main/source/metrics/BigDataMetrica2.jpg" alt="Метрика-2" style="width: 30%">
</p>
<p align="center">
  <img src="https://github.com/dmmmit/smoking_detection/blob/main/source/metrics/BigDataMetrica3.jpg" alt="Метрика-3" style="width: 30%;">
  <img src="https://github.com/dmmmit/smoking_detection/blob/main/source/metrics/BigDataMetrica4.jpg" alt="Метрика-4" style="width: 30%;">
</p>

- ![BigData NOTEBOOK](https://github.com/dmmmit/smoking_detection/blob/main/source/notebooks/BigData.ipynb)
- ![BigData Model](https://github.com/dmmmit/smoking_detection/blob/main/source/models/big_data_model.pt)

### 🧪 Исследование
Мы провели исследование для улучшения качества детекции в условиях низкой освещенности. В темное время суток, когда камеры наблюдения с трудом фиксируют силуэты людей и сигарет, можно использовать детекцию по горящему концу сигареты. В таких условиях его будет четко видно как ярко выраженный красный объект.

Для исследования мы создали собственный датасет: сфотографировали людей с подожженной сигаретой на плохо освещенной территории, размеченные изображения добавили в основной набор данных, а также дополнили его изображениями из открытых источников. Модель продемонстрировала хорошие результаты, но для полной оптимизации её необходимо дообучить. Объединение этой модели с основной поможет улучшить метрики обнаружения сигареты у человека.

<p align="center">
  <img src="https://github.com/dmmmit/smoking_detection/blob/main/source/metrics/RedLightMetrica1.jpg" alt="Метрика-1" style="width:30%;">
  <img src="https://github.com/dmmmit/smoking_detection/blob/main/source/metrics/RedLightMetrica2.jpg" alt="Метрика-2" style="width:30%;">
  <img src="https://github.com/dmmmit/smoking_detection/blob/main/source/metrics/RedLightMetrica3.jpg" alt="Метрика-3" style="width:30%;">
</p>

- ![RedLight NOTEBOOK](https://github.com/dmmmit/smoking_detection/blob/main/source/notebooks/RedLight.ipynb)
- ![RedLight Model](https://github.com/dmmmit/smoking_detection/blob/main/source/models/red_light_model.pt)

### 💨 Детекция дыма
Мы также решили попробовать детектировать дым от зажженной сигареты. Обучили модель на имеющемся датасете, и получили **хорошие метрики**. Данную модель можно использовать совместно с основной, что позволит повысить точность обнаружения факта курения.

<p align="center">
  <img src="https://github.com/dmmmit/smoking_detection/blob/main/source/metrics/SmokeDetectMetrica1.jpg" alt="Метрика-1" style="width:30%;">
  <img src="https://github.com/dmmmit/smoking_detection/blob/main/source/metrics/SmokeDetectMetrica2.jpg" alt="Метрика-2" style="width:30%;">
</p>

- ![SmokeDetect NOTEBOOK](https://github.com/dmmmit/smoking_detection/blob/main/source/notebooks/SmokeDetect.ipynb)
- ![SmokeDetect Model](https://github.com/dmmmit/smoking_detection/blob/main/source/models/smoke_model.pt)

### 🏁 Финальная модель
Окончательная модель была обучена на изображениях, размеченных заказчиком, а также на фотографиях с камер наблюдения, где присутствуют как курящие, так и не курящие люди.
- ![Final NOTEBOOK](https://github.com/dmmmit/smoking_detection/blob/main/source/notebooks/Final.ipynb)
## 🤖 Telegram-бот
Для удобной работы с основной моделью мы разработали **Telegram-бота**, который принимает изображение, обрабатывает его и отправляет пользователю результат в виде вероятности того, что человек на фото курит.

📲 Ссылка на Telegram-бота:  
[Telegram Bot](https://t.me/misis_coconut_bot)

## 🚀 Планы по улучшению
- Точная настройка модели для повышения производительности.
- Объединение всех моделей для достижения максимальной точности детекций.
- Добавление детекции позы человека для более точного определения факта курения.
- Интеграция с биометрическими базами данных (например, Сбер, mos.ru) для автоматического определения личности нарушителя и выписывания штрафов.
