# Competitor Analysis API

## Description
This is a basic API for an application that provides competitor analysis.

## Features
- **Creation of Competitor Profile**: Includes business name, type, location, and website traffic metrics.
- **Viewing Competitor Details**: Shows detailed metrics for each competitor, including top-performing pages.


## Special Build Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`
5. Open the link to the server.

## Dependencies
- Django: Web framework.
- Django REST Framework: For building the API.
- drf-yasg: For API documentation.

## API Documentation
The API documentation is available at `/swagger/` or `/redoc/` endpoints.


## Creating Dummy Data
To populate the database with dummy data for competitor profiles, follow these steps:

- Ensure the server is not running.
- Run the provided script `populate.py` to create dummy data:

```
python populate.py
```