import os
import zipfile
from domain.university import University
from input import add_student, add_course, input_marks, save_data, load_data
from output import show_data

def main():
    system = None

    # --- 1. Decompression & Loading ---
    if os.path.exists("students.dat"):
        print("Found compressed data. Decompressing...")
        try:
            with zipfile.ZipFile("students.dat", 'r') as zip_ref:
                zip_ref.extractall()
            
            # Load the pickled object directly
            system = load_data()
        except Exception as e:
            print(f"Failed to load existing data: {e}")

    # If no data was loaded (or file didn't exist), create a new system
    if system is None:
        print("Initializing new University system...")
        system = University()

    # --- 2. Input Loop ---
    try:
        n = int(input("Enter number of NEW students (0 to skip): "))
        for _ in range(n):
            add_student(system)

        m = int(input("Enter number of NEW courses (0 to skip): "))
        for _ in range(m):
            add_course(system)
            
        # Only ask for marks if we have data
        if system.students and system.courses:
            choice = input("Do you want to input marks? (y/n): ").lower()
            if choice == 'y':
                input_marks(system)
            
    except ValueError:
        print("Invalid input entered. Skipping to output.")

    # --- 3. Output ---
    show_data(system)

    # --- 4. Serialization & Compression ---
    print("\nSaving data...")
    
    # Step A: Pickle the data to university.pkl
    save_data(system)

    # Step B: Compress university.pkl into students.dat
    if os.path.exists("university.pkl"):
        with zipfile.ZipFile("students.dat", 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write("university.pkl")
        
        # Cleanup: Remove the raw pickle file after zipping to keep directory clean
        os.remove("university.pkl") 
        print("Data compressed and saved to students.dat")

if __name__ == "__main__":
    main()