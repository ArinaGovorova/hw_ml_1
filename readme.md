В результате домашней работы было создано пять линейных моделей разного уровня сложности, и с разным количеством параметров. Ожидаемо, лучшая модель -  последняя ридж регрессия, параметры позволяют лучше подстроиться под данные, а грид серч помогает выбрать лучшие гиперпараметры для модели.

Для запуска линейных моделей были проведены иследовательский анализ данных и очистка датасета, результаты анализа лежат в ноутбуке и в файле eda_report.html

Итоговая модель была обернута в классы пайтон для запуска на сервере с помощью fastapi и uvicorn.

К сожалению, у меня не получилось выполнить часть задания с загрузкой csv файла на сервер, зато получилось разобраться с пайплайнами и выгрузкой их в отдельный файл, чтобы применять без обучения, это долгое время у меня не получалось выполнить. 



Для запуска сервера:
uvicorn app:app --reload

Установка модулей и зависимостей:
pip install -r requirements.txt

Ссылка на данные 
'https://raw.githubusercontent.com/Murcha1990/MLDS_ML_2022/main/Hometasks/HT1/cars_test.csv'

Пример данных:
```
{
  "name": "Arina",
  "year": 2019,
  "selling_price": 1000,
  "km_driven": 35000,
  "fuel": "Petrol",
  "seller_type": "Individual",
  "transmission": "Manual",
  "owner": "First Owner",
  "mileage": "23.01",
  "engine": "999"	,
  "max_power": "671.0"	,
  "torque": "5",
  "seats": 5
}
```

 Он же но в формате скрипта :
 ``` curl -X 'POST' \
  'http://127.0.0.1:8000/predict_item' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Arina",
  "year": 2019,
  "selling_price": 1000,
  "km_driven": 35000,
  "fuel": "Petrol",
  "seller_type": "Individual",
  "transmission": "Manual",
  "owner": "First Owner",
  "mileage": "23.01",
  "engine": "999"	,
  "max_power": "671.0"	,
  "torque": "5",
  "seats": 5
}'
```