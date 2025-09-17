# Quiz Game Prototype  

This is a simple prototype that demonstrates how three Python scripts (`server.py`, `client.py`, and `game.py`) communicate with each other to simulate a quiz game setup.  

---

## 1. Connection Between `server.py`, `client.py`, and `game.py`

- **`server.py`**  
  - Acts as the data provider.  
  - Stores multiple sets of quiz data (questions, options, correct answer) mapped to different **game IDs**.  
  - Waits for clients (like `client.py`) to request data.  

- **`client.py`**  
  - Connects to `server.py`.  
  - Acts as a middleman between the game and the server.  
  - Forwards a **game ID** request from `game.py` to `server.py`, receives the quiz data, and then passes it back to `game.py`.  
  - Keeps its connection open to the server even when `game.py` ends, so it can be reused for another game session.  

- **`game.py`**  
  - Runs the actual quiz game for the user.  
  - Prompts the user to enter a **game ID**.  
  - Requests the corresponding quiz data from `client.py`.  
  - Shows the question and options to the player, takes the user’s answer, and then checks if it is correct.  

---

## 2. Local-Only Setup

- This project is designed to run on the **same system** for practice.  
- No external networking or internet connection is required.  
- The server, client, and game scripts all run locally and communicate using **localhost (`127.0.0.1`)** and a chosen port.  

---

## 3. Steps to Run  

```bash
# 1. Start the server
python server.py
# This will start listening for client connections.

# 2. Start the client
python client.py
# The client connects to the server and waits for game requests.

# 3. Run the game
python game.py
# You’ll first be asked to enter a game ID (e.g., 1 or 2).
# The client will fetch the quiz data for that ID from the server.
# The game will then prompt you with the question, options, and check your answer.
