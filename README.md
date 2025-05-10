# 🚀 Flask + PostgreSQL + Prometheus — Мини-DevOps проект

Этот проект — демонстрация микросервиса на Flask с базой данных PostgreSQL, сбором метрик через Prometheus и полной контейнеризацией с помощью Docker и CI/CD через GitHub Actions.

---

## 📦 Стек технологий

- 🐍 **Flask** — легковесный Python web-фреймворк  
- 🐘 **PostgreSQL** — надёжная реляционная база данных  
- 📊 **Prometheus** — система мониторинга  
- 🐳 **Docker + Compose** — управление сервисами  
- ⚙️ **GitHub Actions** — CI/CD пайплайн

---

## 📁 Структура проекта

```bash
.
├── app/                      # Flask-приложение
│   ├── app.py                # Основной файл приложения
│   ├── models.py             # Модель Task
│   ├── ext.py                # Инициализация SQLAlchemy
│   └── requirements.txt      # Python-зависимости
├── prometheus/
│   └── prometheus.yml        # Конфиг Prometheus
├── docker-compose.yml        # Описание сервисов
├── Dockerfile                # Docker-сборка Flask-приложения
├── .github/workflows/ci.yml  # GitHub Actions pipeline
└── README.md                 # Описание проекта
🚀 Быстрый старт
🔧 Запуск с помощью Docker
bash
Копировать
Редактировать
docker-compose up --build
После запуска:

API будет доступен на http://localhost:5000

Метрики Prometheus: http://localhost:9090/metrics

📡 API
🔹 Добавить задачу
bash
Копировать
Редактировать
curl -X POST http://localhost:5000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title": "Сделать проект"}'
🔹 Получить все задачи
bash
Копировать
Редактировать
curl http://localhost:5000/tasks
📈 Метрики
Система автоматически экспортирует метрики Prometheus через prometheus_flask_exporter.
Можно отслеживать запросы, время ответа и другие показатели.

🧪 CI/CD
Каждый push в main:

🔨 Сборка через docker-compose

✅ Тест curl-запроса к приложению

📥 Прогон в CI с ожиданием запуска и curl-тестом
