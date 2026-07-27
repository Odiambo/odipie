FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md requirements.txt ./
COPY odipie ./odipie
COPY docker ./docker
COPY ROProj ./ROProj
COPY lazy_init_py.py app.py config.py ./

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY docs ./docs

ENTRYPOINT ["sh", "docker/entrypoint.sh"]
CMD ["python", "app.py"]
