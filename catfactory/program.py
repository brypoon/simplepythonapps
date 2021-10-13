import os
import cat_service
import subprocess
import platform

def main():
    # print the header
    show_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    # download cats
    download_cats(folder)
    # display cats
    display_cats(folder)


def show_header():
    print('-----------------------')
    print('     CAT FACTORY')
    print('-----------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f"Creating new directory at {full_path}")
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print("Contacting server to download cats...")
    cat_count = 4
    for i in range(1, cat_count+1):
        name = f'lolcat_{i}'
        print("Downloading cat " + name)
        cat_service.get_cat(folder, name)

    print("Done.")


def display_cats(folder):
    print("Displaying cats in OS folder")
    if platform.system() == "Darwin":
        subprocess.call(['open', folder])
    elif platform.system() == "Windows":
        subprocess.call(['explorer', folder])
    elif platform.system() == "Linux":
        subprocess.call(['xdg-open', folder])
    else:
        print("App does not support your OS: " + platform.system())

if __name__ == "__main__":
    main()
