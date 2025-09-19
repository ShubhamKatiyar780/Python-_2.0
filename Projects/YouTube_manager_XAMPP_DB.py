import mysql.connector as mysql
from tabulate import tabulate
from datetime import datetime

connection = mysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    port = 3306
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS StudentsDetails")
print("\nDatabase Created Successfully!")

cursor.execute("USE StudentsDetails")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS youtube_videos(
        Id INT PRIMARY KEY AUTO_INCREMENT,
        Name VARCHAR(255) NOT NULL,
        Category VARCHAR(20) NOT NULL,
        Time TIME NOT NULL)
    ''')  # End of CREATE TABLE command
print("Table Created Successfully!")


# ---------------------- Helper Functions ----------------------

# Function to get all videos from the database
def get_all_videos():
    """Fetch all videos from the database and return them as a list of tuples."""
    cursor.execute(" SELECT * FROM youtube_videos")   # SQL query to select all rows
    return cursor.fetchall()   # Fetch all results as a list of tuples


# Function to display all videos in table format
def list_all_videos():
    """Display all videos in a formatted table with ID, Name, and Duration."""
    videos = get_all_videos()   # Call function to get all videos
    if videos:   # If there are videos in the list
        print(tabulate(videos, headers=["ID", "Name", "Category", "Duration"], tablefmt="fancy_grid"))
    else:   # If no videos are found
        print("No videos found!\n")


# Function to add a new video
def add_video(name, category,  time):
    """Add a new video record to the database."""
    cursor.execute("INSERT INTO youtube_videos (Name, Category, Time) VALUES (%s, %s, %s)", (name, category, time))
    connection.commit()   # Save changes
    print(f'{name} Video added successfully!\n')


def search_video():
    while True:
        print('\nSearch Options:')
        print('1. Search videos starting with text')
        print('2. Search videos ending with text')
        print('3. Search videos containing text (anywhere in between)')
        print('4. Exit from search menu')
        print('-' * 70)
        choice = input('Enter your search choice: ').strip()
        if choice == '4':
            confirmation = input('Are you sure you want to exit? (yes/no): ').strip().lower()
            if confirmation == 'yes':
                print("Exiting to the search menu and returning to main menu!\n")
                return
            elif confirmation =='no':
                print("Exit canceled. Returning to search menu.\n")
            else:
                print("Invalid confirmation! Please type 'yes' to confirm or 'no' to cancel.\n")
        elif choice in ['1', '2', '3']:
            keyword = input('Enter the search keyword: ').strip()
            if keyword:
                match choice:
                    case '1':
                        cursor.execute("SELECT * FROM youtube_videos WHERE Name LIKE %s", (keyword + '%',))
                    case '2':
                        cursor.execute("SELECT * FROM youtube_videos WHERE Name LIKE %s", ('%' + keyword,))
                    case '3':
                        cursor.execute("SELECT * FROM youtube_videos WHERE Name LIKE %s", ('%' + keyword + '%',))
                results = cursor.fetchall()
                if results:
                    print(tabulate(results, headers=["ID", "Name", "Category", "Duration"], tablefmt="fancy_grid"))
                else:   # If no videos are found
                    print("No matching video found!\n")   
            else:
                print('Keyword cannot be empty!\n')
        else:
            print('Invalid choice!\n')


# Function to update video details
def update_video(id, new_name, new_category, new_time):
    cursor.execute("UPDATE youtube_videos SET Name = %s, Time = %s, Category = %s WHERE Id = %s", (new_name, new_time,new_category, id))  # Update query
    connection.commit()   # Save changes
    if cursor.rowcount == 0:   # If no rows updated (ID not found)
        print("No video found with that ID!\n")
    else:   # If row was updated
        print('Video details updated successfully!\n')


# Function to delete a video by ID
def delete_video(id):
    confirmation = input('Are you sure you want to delete this video(yes/no): ').strip().lower()
    if confirmation == 'yes':
        cursor.execute("DELETE FROM youtube_videos WHERE Id = %s", (id, ))
        connection.commit()   # Save changes
        if cursor.rowcount == 0:   # If no rows deleted
            print("No video found with that ID!\n")
        else:   # If deletion successful
            print('Video deleted successfully!\n')
    elif confirmation == 'no':
        print('Deletion canceled. The video is safe in your list.\n')
    else:   # If user types invalid input
        print("Invalid confirmation! Please type 'yes' to confirm or 'no' to cancel.\n")


def validate_time(time):
    """Validate time in HH:MM:SS format. Return valid time string or None."""
    try:
        # Validate format
        valid_time = datetime.strptime(time, "%H:%M:%S")
        return valid_time.strftime("%H:%M:%S")  # Return in proper format
    except ValueError:
        return None


def print_menu():
    """Print the main menu with options in colorful text."""
    print('\nYoutube Manager App With DataBase| choose an option')   # Menu heading
    print('=' * 70)
    print('\033[1;32m1.\033[0m \033[1;31mList of all videos\033[0m')     # Green Red
    print('\033[1;34m2.\033[0m \033[1;35mAdd a video\033[0m')            # Blue Magenta
    print('\033[1;31m3.\033[0m \033[1;32mSearch video by name\033[0m')            # Blue Magenta
    print('\033[1;33m4.\033[0m \033[1;37mUpdate a video details\033[0m') # Yellow White
    print('\033[1;31m5.\033[0m \033[1;32mDelete a video\033[0m')         # Red Green
    print('\033[1;35m6.\033[0m \033[1;33mExit\033[0m')                   # Magenta Yellow
    print('=' * 70)
    # \033[1m = bold text start
    # \033[0m = formatting reset


# ---------------------- Main Program ----------------------
def main():
    """Main program loop to handle user choices."""
    while True:
        print_menu()
        choice = input('Enter your choice: ').strip()

        if choice == '1':
            list_all_videos()   # Show all videos

        elif choice == '2':
            name = input('Enter the video name: ').strip()
            category = input('Enter the video category: ').strip()
            time = validate_time(input('Enter the video duration (HH:MM:SS): ').strip())
            if not name or not category:
                print("Name and Category cannot be empty!\n")
            elif time is None:
                print("Invalid time format! Please use HH:MM:SS.\n")
            else:
                add_video(name, category, time)

        elif choice == '3':
            # name = input('Enter the video name: ').strip()
            search_video()
                
        elif choice == '4':
            videos = get_all_videos()   # Fetch all videos
            if videos:   # If videos exist
                try:
                    id = int(input('Enter the video ID for updation: '))
                    new_name = input('Enter the new video name: ').strip()
                    new_category = input('Enter the new category: ').strip()
                    new_time = validate_time(input('Enter the new video duration (HH:MM:SS): ').strip())
                    if not new_name or not new_category:   # If either is empty
                        print('Name and Category cannot be empty!\n')
                    elif new_time is None:
                        print("Invalid time format! Please use HH:MM:SS.\n")
                    else:   # If all fields are filled
                        update_video(id, new_name, new_category, new_time)
                except ValueError:   # If user enters non-numeric ID
                    print('Invalid ID! Please enter a number.\n')
            else:   # If no videos exist
                print('No videos found!\n')

        elif choice == '5':
            videos = get_all_videos()   # Fetch all videos
            if videos:   # If videos exist
                try:   # Try block to handle invalid input
                    id = int(input('Enter the video ID for deletion: '))
                    delete_video(id)
                except ValueError:   # If invalid ID entered
                    print('Invalid ID! Please enter a number.\n')
            else:   # If no videos exist
                print('No videos found!\n')

        elif choice == '6':
            confirmation = input('Are you sure you want to exit? (yes/no): ').strip().lower()
            if confirmation == 'yes':
                print("Exiting YouTube Manager. Goodbye!")
                return
            elif confirmation =='no':
                print("Exit canceled. stay on main menu.\n")
            else:
                print("Invalid confirmation! Please type 'yes' to confirm or 'no' to cancel.\n")
            
        else:   # If choice is invalid
            print('Invalid choice!')


# ---------------------- Entry Point ----------------------
if __name__ == '__main__':  # Ensure code runs only if executed directly
    try:
        main()  # Call the main function
    except Exception as e:  # Catch unexpected errors
        print("Unexpected error:", e)   # Print error message
    finally:    # Always execute this block
        if connection:  # If connection is open
            connection.close()  # Close database connection
            print("Database connection closed")    # Confirmation message