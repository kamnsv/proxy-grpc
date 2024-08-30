# Сборка образа

```
docker build -t grpc-server .
```
# Запуск контейнера

```
docker run -d -p 50051:50051 grpc-server
```