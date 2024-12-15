# ReactJS & Python (Flask) Project

This project is built using **ReactJS** as the frontend framework and **Python** (Flask) as the backend framework.

## Project Overview
- **Frontend**: ReactJS
  - Libraries: Material UI, Axios, Typed.js
- **Backend**: Python with Flask
  - Libraries: CORS, SQLite3, Flask
- The backend is currently running in Flask debug mode.

---

## Prerequisites
To run this project, ensure the following are installed on your system:

- **Node.js** (for running the frontend)
- **Python 3.7+** (for running the backend)

---

## Setup Instructions

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install required libraries:
   ```bash
   npm install @mui/material @emotion/react @emotion/styled axios typed.js
   ```
3. Start the React development server:
   ```bash
   npm start
   ```

### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. Install required libraries:
   ```bash
   pip install flask flask-cors sqlite3
   ```
4. Start the Flask server in debug mode:
   ```bash
   flask run --debug
   ```

---

## Features
- **Frontend**: A React-based user interface styled with Material UI, capable of interacting with the backend through Axios.
- **Backend**: A Flask-based server with SQLite3 as the database, handling API requests and data processing.

---

## Notes
- Ensure the frontend and backend servers are running simultaneously to test the application.
- For production, Flask debug mode should be disabled.

---

## Future Enhancements
- Implement a production-ready Flask server.
- Add state management (e.g., Redux) on the frontend.
- Integrate a more robust database solution for scaling beyond SQLite3.

---

Feel free to contribute to this project or report any issues you encounter. 🚀
