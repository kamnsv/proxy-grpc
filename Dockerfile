# Используем официальный образ Python на базе Alpine
FROM python:3.11-alpine

# Устанавливаем необходимые зависимости
RUN apk add --no-cache gcc musl-dev

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения
COPY . .

# Генерируем gRPC файлы из .proto
RUN python -m grpc_tools.protoc -I./protos --python_out=./server --grpc_python_out=./server ./protos/*.proto

# Указываем команду для запуска сервера
CMD ["python", "server"]

# Открываем порт
EXPOSE 50051