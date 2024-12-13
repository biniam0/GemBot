## Tech Stacks
![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)  ![Django](https://img.shields.io/badge/Django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)  ![HTML](https://img.shields.io/badge/HTML5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)  ![CSS](https://img.shields.io/badge/CSS3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)  ![Bootstrap](https://img.shields.io/badge/Bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)  ![SQLite](https://img.shields.io/badge/SQLite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)  ![Gemini AI](https://img.shields.io/badge/Gemini--AI-%230255D6.svg?style=for-the-badge&logoColor=white)  ![Markdown](https://img.shields.io/badge/Markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)


# AI Chat Application
An interactive web application where users can chat with an AI model (powered by Gemini 1.5). The app stores chat history for logged-in users and provides an intuitive user interface for seamless communication.

## Features
- User authentication: Login and logout functionality.
- Chat functionality: Users can send messages and receive responses from the AI.
- Chat history: Stores and displays past chats for logged-in users.
- Markdown formatting: AI responses are formatted using Markdown for better readability.
- Environment variable management: API keys and sensitive data are securely stored and managed.

## Technologies Used
- Backend: Django
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (or your configured database)
- AI Integration: Gemini AI API
- Markdown Formatting: Python markdown module

## Setup Instructions

1. Clone the Repository:
- `git clone <repository-url>`
- `cd <repository-folder> `

2. Set Up Environment Variables:
- Create a .env file in the project root:
- `API_KEY=your-secret-api-key`
- Add `.env` to `.gitignore` to prevent accidental commits.

3. Install Dependencies:
- `pip install -r requirements.txt`

4. Run Migrations:
- `python manage.py migrate`

5. Start the Server:
- `python manage.py runserver`
- Access the Application: Open `http://127.0.0.1:8000/` in your browser.

## Usage
1. Authentication:
- Login to access chat history and save new chats.
- Logout to access the public chat functionality without saving history.

2. Chat with AI:
- Type a message in the chat box and click "Send."
- Receive a response formatted with Markdown.

## Chat History:

- Logged-in users can view their past conversations.
- Environment Variables
- Ensure the following environment variables are set:
 > `API_KEY: Your Gemini AI API key`

## Future Enhancements:
- Add support for multiple AI models.
- Improve user interface with additional styling.
- Enable exporting chat history as a file.
