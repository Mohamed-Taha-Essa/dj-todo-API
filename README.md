
# Django To-Do App  

A simple To-Do application built with Django and Django REST Framework (DRF) for managing tasks with status tracking. The app provides a RESTful API for creating, retrieving, updating, and deleting tasks.  

---

## Features  

- **Task Management**:  
  - Create, update, delete, and list tasks.  
  - Track task status with two states: `INPROGRESS` and `DONE`.  
- **RESTful API**:  
  - Built with Django REST Framework (DRF).  
  - Default routing for To-Do endpoints using `DefaultRouter`.  
- **Date Tracking**:  
  - Each task includes a creation timestamp.  

---

## Technologies Used  

- **Backend**: Django, Django REST Framework  
- **Database**: SQLite (default, configurable to other databases)  
- **API Testing**: Django's `manage.py test` and tools like Postman or Swagger  

---

## Project Structure  

```plaintext  
django-todo/  
│  
├── todo/  
│   ├── models.py         # Defines the ToDo model  
│   ├── serializers.py    # Serializes ToDo objects for the API  
│   ├── api.py            # API views using DRF viewsets  
│   ├── urls.py           # Routes for To-Do endpoints  
│   ├── admin.py          # Admin configurations for ToDo  
│   ├── tests.py          # Unit tests for the application  
│  
├── project_name/         # Django project settings and configurations  
├── manage.py             # Django management script  
└── requirements.txt      # Python dependencies  
```  

---

## Models  

### ToDo Model  

```python  
from django.db import models  
from django.utils import timezone  

STATUS = [  
    ('INPROGRESS', 'INPROGRESS'),  
    ('DONE', 'DONE')  
]  

class ToDo(models.Model):  
    title = models.CharField(max_length=50)  
    status = models.CharField(max_length=50, choices=STATUS)  
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):  
        return self.title  
```  

**Fields**:  
- `title`: The name of the task (string, max length 50).  
- `status`: The task's current status, either `INPROGRESS` or `DONE`.  
- `created_at`: The timestamp when the task was created.  

---

## API Endpoints  

The app uses Django REST Framework's `ModelViewSet` and a `DefaultRouter` to provide CRUD operations:  

### Available Endpoints  

| HTTP Method | Endpoint    | Description                |  
|-------------|-------------|----------------------------|  
| GET         | `/todo/`    | Retrieve a list of tasks.  |  
| POST        | `/todo/`    | Create a new task.         |  
| GET         | `/todo/{id}/` | Retrieve a specific task. |  
| PUT         | `/todo/{id}/` | Update a specific task.   |  
| DELETE      | `/todo/{id}/` | Delete a specific task.   |  

---

## How to Run  

### Prerequisites  

- Python >= 3.8  
- Django >= 4.x  
- Django REST Framework >= 3.14  

### Installation  

1. **Clone the repository**:  
   ```bash  
   git clone <repository-url>  
   cd django-todo  
   ```  

2. **Set up a virtual environment**:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Apply migrations**:  
   ```bash  
   python manage.py migrate  
   ```  

5. **Run the development server**:  
   ```bash  
   python manage.py runserver  
   ```  

6. **Access the app**:  
   - API Root: `http://127.0.0.1:8000/todo/`  

---

## Testing  

1. **Run unit tests**:  
   ```bash  
   python manage.py test  
   ```  

2. **Test the API**:  
   Use tools like Postman or Swagger to interact with the endpoints.  

---

## Contributing  

1. Fork the repository.  
2. Create a new branch for your feature:  
   ```bash  
   git checkout -b feature-name  
   ```  
3. Commit your changes:  
   ```bash  
   git commit -m "Add feature description"  
   ```  
4. Push to your branch:  
   ```bash  
   git push origin feature-name  
   ```  
5. Open a pull request.  


