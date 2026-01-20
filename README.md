# DRF Library API

A Django REST Framework (DRF) based API for managing a library book collection. This project provides a RESTful API to perform CRUD operations on books, along with filtering and summary features.

## Features

- **Book Management**: Create, read, update, and delete books
- **Filtering**: Filter books by author name and published year
- **Book Summary**: Get a short summary (first 100 characters) of any book
- **RESTful API**: Clean and intuitive REST endpoints
- **Admin Interface**: Django admin interface for managing books

## Project Structure

```
drf_library/
├── drf_library/          # Main project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py          # Root URL configuration
│   ├── asgi.py          # ASGI configuration
│   └── wsgi.py          # WSGI configuration
├── library/             # Main application
│   ├── models.py        # Book model definition
│   ├── views.py         # API views
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # Application URL routing
│   ├── admin.py         # Django admin configuration
│   └── migrations/      # Database migrations
├── manage.py            # Django management script
└── db.sqlite3           # SQLite database (created after migrations)
```

## Technology Stack

- **Python**: Python 3.12
- **Django**: 6.0
- **Django REST Framework**: 3.16.1
- **Database**: SQLite3

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or navigate to the project directory**
   ```bash
   cd drf_library
   ```

2. **Create and activate a virtual environment** (if not already created)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Base URL
All API endpoints are prefixed with `/api/`

### Endpoints

#### 1. List/Create Books
- **URL**: `/api/books/`
- **Methods**: `GET`, `POST`
- **Description**: 
  - `GET`: Retrieve a list of all books (supports filtering)
  - `POST`: Create a new book

**Query Parameters (for GET):**
- `author` (optional): Filter books by author name (case-insensitive partial match)
- `year` (optional): Filter books by published year

**Example GET Request:**
```
GET /api/books/?author=tolkien&year=1954
```

**Example POST Request:**
```json
POST /api/books/
Content-Type: application/json

{
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "published_year": 1954,
    "summary": "An epic fantasy novel about the quest to destroy the One Ring."
}
```

#### 2. Book Detail
- **URL**: `/api/books/<id>/`
- **Methods**: `GET`, `PUT`, `PATCH`, `DELETE`
- **Description**: 
  - `GET`: Retrieve a specific book
  - `PUT`: Update entire book object
  - `PATCH`: Partially update a book
  - `DELETE`: Delete a book

**Example:**
```
GET /api/books/1/
PUT /api/books/1/
DELETE /api/books/1/
```

#### 3. Book Summary
- **URL**: `/api/books/<id>/summary/`
- **Method**: `GET`
- **Description**: Get a short summary (first 100 characters) of a book

**Response Example:**
```json
{
    "id": 1,
    "title": "The Lord of the Rings",
    "short_summary": "An epic fantasy novel about the quest to destroy the One Ring..."
}
```

## Data Model

### Book Model

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Primary key (auto-generated) |
| `title` | CharField(200) | Book title |
| `author` | CharField(100) | Author name |
| `published_year` | Integer | Year of publication |
| `summary` | TextField | Book summary (optional) |

## Usage Examples

### Using cURL

**Create a new book:**
```bash
curl -X POST http://127.0.0.1:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "1984",
    "author": "George Orwell",
    "published_year": 1949,
    "summary": "A dystopian social science fiction novel and cautionary tale."
  }'
```

**List all books:**
```bash
curl http://127.0.0.1:8000/api/books/
```

**Filter books by author:**
```bash
curl http://127.0.0.1:8000/api/books/?author=Orwell
```

**Get a specific book:**
```bash
curl http://127.0.0.1:8000/api/books/1/
```

**Update a book:**
```bash
curl -X PUT http://127.0.0.1:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "1984",
    "author": "George Orwell",
    "published_year": 1949,
    "summary": "Updated summary here."
  }'
```

**Delete a book:**
```bash
curl -X DELETE http://127.0.0.1:8000/api/books/1/
```

**Get book summary:**
```bash
curl http://127.0.0.1:8000/api/books/1/summary/
```

### Using Python requests

```python
import requests

# Create a book
response = requests.post('http://127.0.0.1:8000/api/books/', json={
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'published_year': 1960,
    'summary': 'A gripping tale of racial injustice and loss of innocence.'
})
print(response.json())

# List all books
response = requests.get('http://127.0.0.1:8000/api/books/')
print(response.json())

# Filter by author
response = requests.get('http://127.0.0.1:8000/api/books/?author=Lee')
print(response.json())
```

## Admin Interface

Access the Django admin interface at `http://127.0.0.1:8000/admin/` to manage books through a web interface. You'll need to create a superuser account first:

```bash
python manage.py createsuperuser
```

## Development

### Running Tests

The project includes a test file structure. To run tests:

```bash
python manage.py test
```

### Creating Migrations

If you modify the models, create new migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Project Configuration

- **Debug Mode**: Enabled (for development only)
- **Database**: SQLite3 (default)
- **Time Zone**: UTC

