import os
import zipfile
import time
from domain.university import University
from input import add_student, add_course, input_marks, save_data, load_data
from output import show_data

def main():
    system = None

    # --- 1. Decompression & Loading (Synchronous) ---
    # We keep loading synchronous because the program cannot run without data.
    if os.path.exists("students.dat"):
        print("Found compressed data. Decompressing...")
        try:
            with zipfile.ZipFile("students.dat", 'r') as zip_ref:
                zip_ref.extractall()
            
            # Load the extracted pickle
            system = load_data()
            print("Data loaded successfully.")
            
            # Cleanup extracted file immediately to keep folder clean
            if os.path.exists("university.pkl"):
                os.remove("university.pkl")
                
        except Exception as e:
            print(f"Failed to load existing data: {e}")

    if system is None:
        print("Initializing new University system...")
        system = University()

    # --- 2. Input Loop ---
    try:
        # Check if user wants to add students
        if input("Add new students? (y/n): ").lower() == 'y':
            n = int(input("Enter number of NEW students: "))
            for _ in range(n):
                add_student(system)

        # Check if user wants to add courses
        if input("Add new courses? (y/n): ").lower() == 'y':
            m = int(input("Enter number of NEW courses: "))
            for _ in range(m):
                add_course(system)
        
        # Check if user wants to input marks
        if system.students and system.courses:
            choice = input("Do you want to input marks? (y/n): ").lower()
            if choice == 'y':
                input_marks(system)
            
    except ValueError:
        print("Invalid input entered. Skipping remaining inputs.")

    # --- 3. Output ---
    show_data(system)

    # --- 4. Background Serialization ---
    print("\n--- Exit Sequence ---")
    
    # This call is now non-blocking. 
    # The main thread continues immediately to the print statement below.
    save_thread = save_data(system)
    
    print("Main program has finished execution.")
    print("Waiting for background save to complete...")
    
    # Explicitly join to ensure the script doesn't close strictly before save is done
    # (Though Python waits for non-daemon threads automatically, explicit join is safer)
    save_thread.join()
    print("Goodbye!")

if __name__ == "__main__":
    main()