# Quiz Game Prototype  

This is a simple prototype that demonstrates a frontend-backend setup for a quiz game using Python and a browser-based interface.  

---

## 1. Connection Between `server.py`, `client.py`, and `game.html`

- **`server.py`**  
  - Stores multiple sets of quiz data (questions, options, correct answers) mapped to different **game IDs**.  
  - Waits for connections from `client.py` via **TCP sockets**.  

- **`client.py`**  
  - Acts as a proxy between the frontend and `server.py`.  
  - Runs a **Flask server** that the frontend (`game.html`) can fetch from via HTTP.  
  - When a frontend request comes in for a game ID, `client.py` connects to `server.py` through sockets, fetches the corresponding quiz data, and returns it as JSON.  
  - Keeps running so multiple frontend sessions can request data.  

- **`game.html`**  
  - Browser-based frontend that interacts with `client.py` via **HTTP fetch requests**.  
  - Prompts the user to enter a **game ID**, requests quiz data from `client.py`, and displays the question and options.  
  - Handles user interaction and checks answers.  

---

## 2. Local-Only Setup

- All components run on the **same system** using `localhost (127.0.0.1)`.  
- No internet connection is required.  
- Ports used:  
  - `server.py` → TCP socket (default: 5001)  
  - `client.py` → Flask HTTP server (default: 5000)  
  - `game.html` → served via local HTTP server (e.g., `python -m http.server 8080`)  

---

## 3. Steps to Run  

```bash
# 1. Start the server (data provider)
cd backend
python server.py
# Server listens on TCP port 5001 for client connections.

# 2. Start the client (proxy)
cd backend
python client.py
# Client runs a Flask server on HTTP port 5000.

# 3. Serve the frontend
cd frontend
python -m http.server 8080
# Opens the HTML page via http://127.0.0.1:8080/game.html

# 4. Open the game in a browser
# Enter a game ID (e.g., 1 or 2) and click "Fetch Quiz".
# The frontend will fetch quiz data from client.py,
# which retrieves it from server.py, and then displays it.
