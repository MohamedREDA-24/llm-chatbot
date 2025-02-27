# LLM Chatbot

This project is a multi-container chatbot application that uses FastAPI as the backend and Streamlit as the frontend to provide an interactive chatbot powered by Google's Gemini API. The project is fully containerized using Docker Compose but can also be run locally for development.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
  - [Local Development](#local-development)
  - [Docker Deployment](#docker-deployment)
- [Configuration](#configuration)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```plaintext
llm-chatbot/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── .env
└── docker-compose.yml
```

## Prerequisites
Docker and Docker Compose installed.

Python 3.12 (for local development if needed).

A valid Gemini API key.

# Setup and Installation
## Local Development

**1. Clone the Repository**

```bash
git clone https://github.com/MohamedREDA-24/llm-chatbot.git
cd llm-chatbot
```
**2. Set Up a Virtual Environment**

For the backend:

```bash
cd backend
python -m venv venv
source venv\Scripts\activate  # On linux: venv\bin\activate
pip install --upgrade pip
pip install -r requirements.txt
```

 For the frontend:

 ```bash
cd frontend
python -m venv venv
source venv/Scripts/activate  # On linux: venv\bin\activate
pip install --upgrade pip
pip install -r requirements.txt
```

**3. Configure Environment Variables**

Create a .env file in the project root with the following content:

     GEMINI_API_KEY=your_actual_gemini_api_key_here

Important: Add the .env file to your .gitignore to prevent accidental commits:
   
    .env

**4. Running the Backend and Frontend Locally**

-**Backend:**

 Navigate to the backend folder and run:

    uvicorn main:app --reload
The backend will run on http://localhost:8000.

-**Frontend:**

Navigate to the frontend folder and run:

    streamlit run app.py
The frontend will run on http://localhost:8501.



# Docker Deployment
1. Ensure your .env file is in the project root (this file contains your GEMINI_API_KEY).
2. Build and Run the Containers

Run the following command in the project root:

    docker-compose up --build
This will build and start both the backend (FastAPI) and frontend (Streamlit) containers.


# Configuration

## Backend (FastAPI)

  - **Location:** backend/main.py

  - **Functionality:** 
       - Loads environment variables using dotenv.
       - Configures the Gemini API client using the API key from GEMINI_API_KEY.
       - Exposes a /chat/ endpoint that processes incoming chat messages and returns generated responses.

## Frontend (Streamlit)

  - **Location:**  frontend/app.py

  - **Functionality:**  
       - Provides a chat interface where users can send messages.
       - Maintains chat history with st.session_state.
       - Reads the backend URL from an environment variable (BACKEND_URL) with a default value of http://localhost:8000/chat/ for local development.
       - When running in Docker, the BACKEND_URL is set to http://backend:8000/chat/ via Docker Compose.

## Docker Compose
The docker-compose.yml file defines two services:

```yaml
version: '3.9'
services:
  backend:
    build: ./backend
    container_name: backend
    ports:
      - "8000:8000"
    environment:
      GEMINI_API_KEY: ${GEMINI_API_KEY}

  frontend:
    build: ./frontend
    container_name: frontend
    ports:
      - "8501:8501"
    depends_on:
      - backend
    environment:
      BACKEND_URL: http://backend:8000/chat/
```
# Usage      
- **Access the Frontend:**

    Once the containers are running, open your browser and navigate to http://localhost:8501 to access the chatbot interface.
- **Chat Flow:**  
  - Type your message into the Streamlit chat input.
  - The frontend sends your message to the backend via the /chat/ endpoint.
  - The backend processes the request using the Gemini API and returns a response.
  - The response is displayed in the chat interface.
 
# Troubleshooting
### Missing GEMINI_API_KEY Error:
- Verify that the `.env` file exists in the project root.
- Ensure that the `.env` file contains a valid `GEMINI_API_KEY`.

### 500 Internal Server Error in Backend:
- Check the backend logs for details.
- Ensure that the Gemini API is accessible.
- Verify that your API key is correct.

### Docker Networking Issues:
- Make sure both the backend and frontend services are defined in the same `docker-compose.yml` file.
- Confirm that the frontend can resolve the backend using the service name `backend`.

## Contributing
Contributions are welcome! Please open issues or submit pull requests with improvements or bug fixes.

## License
This project is licensed under the MIT License.














