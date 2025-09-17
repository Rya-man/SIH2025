import socket
import json

HOST = "127.0.0.1"  # Connect to client.py
PORT = 6000

# Ask user for gameID
game_id = input("Enter gameID (1 or 2): ").strip()

# Connect to client.py
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Send gameID to client.py
s.sendall(game_id.encode())

# Receive quiz data
data = s.recv(1024).decode()
quiz_data = json.loads(data)
s.close()

# If invalid gameID
if "error" in quiz_data:
    print("\n❌", quiz_data["error"])
else:
    # Run quiz
    print("\nWelcome to the Quiz Game!")
    print(quiz_data["question"])
    for option in quiz_data["options"]:
        print(option)

    user_input = input("\nEnter your choice (1 or 2): ")

    if user_input == quiz_data["answer"]:
        print("\n✅ Correct! Well done.")
    else:
        print(f"\n❌ Wrong! The correct answer is option {quiz_data['answer']}.")
