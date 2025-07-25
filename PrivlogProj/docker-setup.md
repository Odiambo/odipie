# 🐳 Docker Setup for Flask-based AI Project

This guide walks through the Docker integration process for a Flask-based project. It includes a project folder overview, build and run instructions, and environment notes.
I do not tend to use python pre-releases, so this is geared for `python 3.13.5`.

> *Security note: Never import python packages using the `*` (meaning 'import all'). Use the modules reuired for the project and that you selected during the requirements phase. If you are using the `*`, first inspect the `_init_.py` file for any aberrations or unexpected attributes.
<br>Never run `*` inside of _init_py.*

---

## 📂 Project Tree (Post-Dockerization)

```
ai_project/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   ├── static/
│   └── models/
├── notebooks/
├── data/
├── scripts/
├── tests/
├── config.py
├── requirements.txt
├── app.py
├── docker/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── entrypoint.sh
│   └── README.md
├── docker-compose.yml
└── README.md
```

---

## Step 1: Create the Docker Build Folder

Create a `/docker` folder and add the following files:

- `Dockerfile` – Defines the Flask app build process.
- `.dockerignore` – Prevents unnecessary files from entering the image.
- `entrypoint.sh` – Launches the app.
- `README.md` – (Optional) Describes the Docker purpose and usage.

---

##  Step 2: Define the Dockerfile

```dockerfile
FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

COPY ../requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ../ /app/

RUN chmod +x docker/entrypoint.sh
ENTRYPOINT ["docker/entrypoint.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]
```

---

## Step 3: Ignore Build Clutter

`.dockerignore` contents:

```
__pycache__
*.pyc
*.pyo
*.pyd
.env
*.db
*.sqlite3
.git
.vscode
notebooks/
data/
tests/
docker/
```

---

## Step 4: Run with Docker Compose

`docker-compose.yml` at project root:

```yaml
version: "3.9"

services:
  flaskapp:
    build:
      context: .
      dockerfile: docker/Dockerfile
    volumes:
      - .:/app
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - FLASK_APP=app.py
    command: flask run --host=0.0.0.0 --port=5000
```

---

## Build & Launch

From the root project directory:

```bash
# Build the image
docker-compose build

# Run the container
docker-compose up
```

Visit your app at: [http://localhost:5000](http://localhost:5000)

---

## 📌 Notes

- `PYTHONDONTWRITEBYTECODE=1`: Prevents `.pyc` files for a cleaner container.
- `PYTHONUNBUFFERED=1`: Ensures real-time logging to stdout/stderr.
- You can later swap Flask’s development server with your choice for production.
- Entry points, security, and project buildouts are still under works.

---
