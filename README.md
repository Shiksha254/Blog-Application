# Blog-Application
# Django Blog Application with Posts and Comments

Django Blog Application with Posts and Comments is a blog platform built with Django, featuring the ability to create, read, update, and delete blog posts, as well as leave comments on posts.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- **Post Management:**
  - Users can create, read, update, and delete blog posts.
  - Posts support rich text content and can include images.
  - Posts display creation and last update timestamps.

- **Comment System:**
  - Users can leave comments on blog posts.
  - Comments display the author's name and the creation timestamp.

- **User Authentication:**
  - Users can sign up, log in, and log out.
  - Authentication is required for creating, updating, or deleting posts and comments.

- **Responsive Design:**
  - The application is designed to be mobile-friendly.

## Installation

1. **Clone the repository**

    ```
    git clone https://github.com/your-username/Blog-Application.git
    ```

2. **Navigate to the project directory**

    ```
    cd task
    ```

3. **Create a virtual environment**

    ```
    python -m venv venv
    ```

4. **Activate the virtual environment**

    - On Windows:

        ```
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```
        source venv/bin/activate
        ```

5. **Install dependencies**

    ```
    pip install -r requirements.txt
    ```

6. **Apply database migrations**

    ```
    python manage.py migrate
    ```

7. **Create a superuser**

    ```
    python manage.py createsuperuser
    ```

8. **Start the development server**

    ```
    python manage.py runserver
    ```

9. **Open your web browser and navigate to**

    ```
    http://localhost:8000
    ```

## Usage

1. **Log in or sign up**

    - Navigate to `http://localhost:8000/accounts/login` to log in if you already have an account.
    - Navigate to `http://localhost:8000/accounts/signup` to create a new account if you don't have one.

2. **Create a new blog post**

    - Once logged in, navigate to `http://localhost:8000/posts/create` to create a new blog post.

3. **Read, update, or delete a blog post**

    - Navigate to `http://localhost:8000/posts` to view all blog posts.
    - Click on a post to view its details, update it, or delete it.

4. **Leave a comment**

    - Scroll to the bottom of a blog post's detail page and use the comment form to leave a comment.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature`)
6. Create a new Pull Request
