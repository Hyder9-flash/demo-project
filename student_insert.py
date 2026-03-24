import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",            # your MySQL username
    password="Shyder@09#sa",# your MySQL password
    database="hyder_db"     # your database name
)
cursor = conn.cursor()

while True:
    # Ask user for input
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade (A/B/C): ")

    # Insert into database
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)",
        (name, age, grade)
    )
    conn.commit()
    print("✅ Student saved successfully!")

    # Ask if user wants to add more
    choice = input("Do you want to add another student? (yes/no): ").strip().lower()
    if choice != "yes":
        break

# Show all students after insertion
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\n📋 Current Students in Database:")
for row in rows:
    print(row)

cursor.close()
conn.close()