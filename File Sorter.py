# File Sorter
import os
import shutil

def filetype(file):
    img = (".png", ".jpeg", ".jpg", ".gif", ".webp")
    doc = (".txt", ".docx", ".pdf")
    code = (".py", ".html")
    vid = (".mp4", ".mkv", ".mov", ".avi")

    if file.endswith(img):
        return "image"
    elif file.endswith(doc):
        return "document"
    elif file.endswith(code):
        return "code"
    elif file.endswith(vid):
        return "video"
    else:
        return "misc"

def file_dir(type):
    # ! Important !
    # REPLACE Username with your Username
    if type == "image":
        return "C:\\Users\\Username\\Pictures"
    elif type == "document":
        return "C:\\Users\\Username\\Documents\\Doc"
    elif type == "video":
        return "C:\\Users\\Username\\Videos"
    elif type == "code":
        return "C:\\Users\\Username\\Documents\\Code"
    else:
        return "C:\\Users\\Username\\Documents\\Misc"

def organizer(folder):

   # Organize all top-level files in a folder
    if not os.path.isdir(folder):
        print("Folder does not exist!")
        return


    for item in os.listdir(folder):
        full_path = os.path.join(folder, item)

        # Skip folders
        if os.path.isdir(full_path):
            print(f"Skipping folder: {item}")
            continue

        # Only handle files
        if os.path.isfile(full_path):
            type = filetype(item)
            destination_folder = file_dir(type)

            os.makedirs(destination_folder, exist_ok=True)
            destination_path = os.path.join(destination_folder, item)

            # Avoid overwriting
            if os.path.exists(destination_path):
                print(f"{item} already exists in {destination_folder}. Skipping!")
                continue

            shutil.move(full_path, destination_path)
            print(f"{item} moved to {destination_folder}")

def main():
    folder = input("Enter folder to be organized: ").strip()
    organizer(folder)

if __name__ == "__main__":
    main()