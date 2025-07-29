``` markdown
# **Newsportal**

A modern Django web application for managing news publishers, journalists, articles, and subscriptions.

This project demonstrates professional Django practices, REST API implementation, Docker containerization, Sphinx documentation, and `.env`-driven configuration for security and portability.

---

## **Features**
- **Custom User Model**: Designed for publishers, journalists, subscribers.
- **Publisher & Journalist Management**: Streamlined tools for managing platform personnel.
- **Secure Authentication**: Built-in security practices.
- **RESTful API Endpoints**: Powered by Django REST Framework.
- **Easy Local Development**: Use of virtual environments (`venv`).
- **Complete Containerization**: Docker support for hassle-free deployment.
- **Developer Documentation**: Sphinx-generated guidance for developers.

---

## **🏗️ Quick Start (Local Development)**

1. **Clone this repo** and navigate to the project root:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Create and edit your `.env` file**:  
   Add all required configuration (see the sample below).

5. **Set up the database and superuser**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
   Visit the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## **🐳 Docker Build & Run**

1. **Build the Docker image**:
   ```bash
   docker build -t newsportal .
   ```

2. **Run your app in Docker** (ensure DB credentials in `.env` are set up):
   ```bash
   docker run --env-file .env -p 8000:8000 newsportal
   ```

   ### Notes:
    - For MariaDB on **Mac**: Set `DB_HOST=host.docker.internal` in `.env`.
    - For MariaDB in another **Docker container** (via Compose): Use `DB_HOST=db` (or the container's service name).

3. **Stop the app**:
   ```bash
   CTRL+C   # or
   docker stop <container_id>
   ```

---

## **📄 Sample `.env` File**

```text
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=newsappdb
DB_USER=admin
DB_PASSWORD=@Sapd71236147
DB_HOST=localhost              # local dev or host.docker.internal for Docker/Mac
DB_PORT=3306

# X/Twitter API integration (optional)
X_API_KEY=your-x-api-key
X_API_SECRET=your-x-api-secret
X_BEARER_TOKEN=your-x-bearer-token
```

> ⚠ **Never commit your `.env` file to GitHub!**  
> Check `.gitignore` to ensure it's excluded.

---

## **📝 Additional Project Info**

- **Documentation**:  
  Find auto-generated Sphinx developer and API docs in the `docs/` directory.

- **Requirements**:
    - Python 3.12+
    - MariaDB 10+ or MySQL 8+.

- **Containerization**:  
  Full Docker support (`Dockerfile` provided).

- **REST API**:  
  Accessible under `/api/` endpoints.

---

## **🙅 Security Notice**
- **Do not use this configuration for production** as `DEBUG` mode is enabled.
- Always use a **unique secret key** and production-level database credentials when deploying.

---

## **💻 Author**
**D. Botha**
```
