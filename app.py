import os
import datetime
import tkinter as tk
from tkinter import filedialog, simpledialog

def upload_file():
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename()
    return file_path


def index_file(file_path):
    
    auto_index = datetime.datetime.now().strftime("%Y-%m-%d")
    
    
    manual_index = simpledialog.askstring("Indexation", "Entrez les métadonnées:")
    
    return auto_index, manual_index


def classify_file(file_path, auto_index, manual_index):
    directory = f"./ClassifiedFiles/{manual_index}/{auto_index}/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    new_path = os.path.join(directory, os.path.basename(file_path))
    os.rename(file_path, new_path)


def evaluate_classification(file_path, manual_index):
    evaluation_result = {
        "correct_classification": False,
        "metadata_integrity": False,
        "file_accessibility": False,
        "naming_convention": False
    }

    
    expected_directory = f"./ClassifiedFiles/{manual_index}/"
    if os.path.dirname(file_path) == expected_directory:
        evaluation_result["correct_classification"] = True

    
    metadata_file = expected_directory + "metadata.txt"
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r') as file:
            metadata = file.read()
            if manual_index in metadata:
                evaluation_result["metadata_integrity"] = True

    
    if os.path.exists(file_path):
        evaluation_result["file_accessibility"] = True

   
    if os.path.basename(file_path).startswith("2023-"):
        evaluation_result["naming_convention"] = True

    return evaluation_result


file_path = upload_file()
auto_index, manual_index = index_file(file_path)
classify_file(file_path, auto_index, manual_index)
evaluation_result = evaluate_classification(file_path, manual_index)
print(evaluation_result)
