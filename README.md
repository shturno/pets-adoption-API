# Pet Adoption API

This project is an API for managing pets and the people associated with them. The API is built with Flask and uses an SQLite database to store information. The project includes functionality for listing, creating, and deleting pets and people.

## Project Structure

- **src/controllers**: Contains controllers that handle requests and interact with repositories.
- **src/main/composer**: Contains composers that create instances of controllers.
- **src/models/sqlite**: Contains interfaces and entities for interacting with the SQLite database.
- **src/views/http_types**: Contains the `HttpRequest` class representing the HTTP request.
- **src/errors**: Contains error handlers and custom error types.

## Features

### Pets

- **List Pets**: `GET /pets`
  - Lists all pets stored in the database.

- **Delete Pet**: `DELETE /pets/<pet_name>`
  - Removes a pet based on the provided name.

### People

- **Create Person**: `POST /people`
  - Adds a new person to the database. Data should be provided in the request body.

- **Find Person**: `GET /people/<person_id>`
  - Retrieves the information of a person based on the provided ID.

## Installation

To set up the development environment, follow these steps:

1. **Clone the repository:**
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
2. **Create a virtual environment:**
   python -m venv venv
3. **Activate the virtual environment:**
   - Linux/Mac:
       source venv/bin/activate
   - Windows:
       .\venv\Scripts\activate
4. **Install the dependencies:**
     pip install -r requirements.txt
## Usage

To start the Flask server, run: python3 run.py

## Testing

To run the tests, use the following command: pytest -s -v

## Web Service

To run the project without installing it, access https://pets-adoption-5o9i.onrender.com/ and use the routes on src/main/routes 

## Contributing

If you would like to contribute to the project, please fork the repository, make your changes, and submit a pull request. Ensure that your commits are well-documented and that tests pass.

## Author
@shturno

## Contact

You can contact me at [email](mailto:gabriel.dsalvarenga@gmail.com)
