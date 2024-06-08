import os


def write_file(uploaded_file, directory, file_name):
    """Generic Function to write file to a given directory

    Args:
        uploaded_file (_type_): File Object which is to be saved.
        directory (_type_): Directory where file is to be saved.
        file_name (_type_): Name of File to be saved.
    """
    if not os.path.exists(directory):  # Checking if the directory exists
        os.makedirs(directory)  # Creating the directory
    with open(os.path.join(directory, file_name), "wb+") as f:
        for chunk in uploaded_file.chunks():
            f.write(chunk)  # Writing File to given location