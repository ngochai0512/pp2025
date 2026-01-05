import os
import zipfile
from domain.university import University
from input import add_student, add_course, input_marks, load_data
from output import show_data

def main():
    system = University()

    # --- Startup Check ---
    # Check if students.dat exists
    if os.path.exists("students.dat"):
        print("Found existing data. Decompressing...")
        # Decompress files
        with zipfile.ZipFile("students.dat", 'r') as zip_ref:
            zip_ref.extractall()
        
        # Load data from the extracted text files
        load_data(system)
    
    # --- Input Loop ---
    # We ask if the user wants to add new data. 
    # If data was loaded, they might just want to view it.
    try:
        n = int(input("Enter number of NEW students (0 to skip): "))
        for _ in range(n):
            add_student(system)

        m = int(input("Enter number of NEW courses (0 to skip): "))
        for _ in range(m):
            add_course(system)
            
        if n > 0 or m > 0:
            input_marks(system)
            
    except ValueError:
        print("Invalid input entered. Skipping to output.")

    # --- Output ---
    show_data(system)

    # --- Shutdown Compression ---
    # Compress files to students.dat before closing
    print("\nCompressing data...")
    files_to_compress = ["students.txt", "courses.txt", "marks.txt"]
    
    with zipfile.ZipFile("students.dat", 'w') as zipf:
        for file in files_to_compress:
            if os.path.exists(file):
                zipf.write(file)
                # Optional: Remove txt files after zipping to keep folder clean
                # os.remove(file) 
    
    print("Data saved to students.dat")

if __name__ == "__main__":
    main()