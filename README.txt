# Customer Insight Tracker

A simple, full-stack web application built with Python (Flask) and vanilla JavaScript to demonstrate the process of taking a concept from idea to a functional prototype.

## Purpose

This app was built as a practical demonstration of using AI to generate the core components of a business tool. It allows users to submit customer feedback, which is then stored and displayed in a clean, organized interface. This is a foundational piece for a more complex system that could include sentiment analysis, keyword extraction, and trend reporting.

## Features

- Submit customer name and feedback text via a web form.
- View all submitted feedback in reverse chronological order.
- Feedback is stored persistently in a SQLite database.
- Clean, responsive, and professional user interface.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Database:** SQLite

## How to Run This Project

1.  **Prerequisites:** Make sure you have Python 3 installed on your system.
2.  **Clone/Download:** Save all the files (`app.py`, `templates/index.html`, `README.md`) into a single directory.
3.  **Install Flask:** Open your terminal or command prompt, navigate to the project directory, and run:
    ```bash
    pip install Flask
    ```
4.  **Run the Application:** In the same terminal, run the following command:
    ```bash
    python app.py
    ```
5.  **Access the App:** Open your web browser and go to `http://127.0.0.1:5000`.

## Future Enhancements

- Integrate a large language model (like the one from Venice.ai) to perform automated sentiment analysis on submitted feedback.
- Create a dashboard to visualize feedback trends over time.
- Add user authentication to allow multiple users to manage their own feedback streams.
- Containerize the application using Docker for easy deployment.

## Author

A prototype generated with strategic assistance from an AI language model to illustrate the principle of implementation over discussion.
