import os
import shutil
import sys

def Search():
    # Prompt the user to input the directory path
    documents_path = input("Enter the directory path you want to check: ")

    # Set the default directory path if the user enters "default"
    if documents_path.lower() == "default":
        documents_path = "/users/Jorge/Desktop"

    # Check if the directory path exists and raise error if not
    if not os.path.exists(documents_path):
        print("The directory path does not exist")
        while True:
            documents_path = input("Enter a valid directory path: ")
            if documents_path.lower() == "default":
                documents_path = "/users/Jorge/Desktop"
            if os.path.exists(documents_path):
                break
        
    # Create an empty list to store the names of the files that contain the specified words
    files_found = []
    file_names = []
    # Prompt the user to input the words to search for
    while True:
        file_name = input("Enter a file name, or 'ok' to stop: ")
        if file_name == None: 
            break
        if file_name.lower() == "ok":
            break
        else:
            file_names.append(file_name)


    # Traverse the directory and search for the specified words in each file name
    for root, dirs, files in os.walk(documents_path):
        for file in files:
            for file_name in file_names:
                if file_name in file:
                    files_found.append(file)




    # Print the list of files that contain the specified words in their file name
    print(f"Here are the files in the '{documents_path}' directory and its subdirectories that contain the words selected:")
    if len(files_found) == 0:
        print("No files found.")
        # Exit the program if no files were found
        try:
            import sys
            # Raise the SystemExit exception instead of calling sys.exit()
            raise SystemExit
        except SystemExit:
            # Handle the SystemExit exception gracefully
            print("The program won't be able to move any files as none has been found")
            return files, documents_path
    else:
        for file in files_found:
            print(file)


            
    return (files_found, documents_path)

def MoveFiles(files_found, documents_path, destination_dir):
    # Check if the destination directory exists and create it if necessary
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Traverse the documents_path directory and its subdirectories
    for root, dirs, files in os.walk(documents_path):
        for file in files:
            # Check if the file matches the specified criteria
            if file in files_found:
                # Skip hidden files like .DS_Store
                if file.startswith('.'):
                    continue
                # Check if the source file exists
                if os.path.exists(os.path.join(root, file)):
                    # Check if the destination file already exists
                    if not os.path.exists(os.path.join(destination_dir, file)):
                        # Move the file to the destination directory if it does not exist
                        shutil.move(os.path.join(root, file), destination_dir)



    print(f"\n\nThe following files have been moved to '{destination_dir}':")
    if files_found:
        for file in files_found:
            print(file)
    else:
        print("No files have been moved")


        
def main():
    files, documents_path = Search()
    Question = input("Do you want to move the files? Write Yes or No: ")
    if Question.lower() == "yes":
        destination_dir = input("Enter the directory where you want to move the files: ")
        if destination_dir.lower() == "default":
            destination_dir = "/users/Jorge/Desktop/test"
        MoveFiles(files, documents_path, destination_dir)
    else:
        print("Okay, No files have been moved")

main()


