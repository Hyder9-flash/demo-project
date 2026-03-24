
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",            # your MySQL username
    password="Shyder@09#",# your MySQL password
    database="hyder_db"     # your database name
)
cursor = conn.cursor()

# Function to register a new user
def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    print("✅ User registered successfully!")

# Function to login
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()

    if result:
        print("🎉 Login successful! Welcome,", username)
    else:
        print("❌ Invalid username or password.")

# Function to delete an account
def delete_account():
    username = input("Enter username to delete: ")
    password = input("Enter password: ")

    cursor.execute("DELETE FROM users WHERE username=%s AND password=%s", (username, password))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"🗑️ Account '{username}' deleted successfully!")
    else:
        print("❌ No account found with those credentials.")

# Main menu
while True:
    choice = input("\nDo you want to (register/login/delete/exit)? ").strip().lower()
    if choice == "register":
        register()
    elif choice == "login":
        login()
    elif choice == "delete":
        delete_account()
    elif choice == "exit":
        break
    else:
        print("Invalid choice. Please type register, login, delete, or exit.")

cursor.close()
conn.close()