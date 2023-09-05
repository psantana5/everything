import os
import sys
import hashlib
import ctypes
from collections import defaultdict
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget, QProgressBar, QLabel, QLineEdit, QCheckBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QMovie
from tqdm import tqdm

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

class DuplicateFinderWorker(QThread):
    progress_updated = pyqtSignal(int)
    duplicates_found = pyqtSignal(list)
    no_duplicates_found = pyqtSignal()
    current_directory = pyqtSignal(str)
    
    def __init__(self, directory, extensions, delete_duplicates, move_duplicates):
        super().__init__()
        self.directory = directory
        self.extensions = extensions
        self.delete_duplicates = delete_duplicates
        self.move_duplicates = move_duplicates

    def run(self):
        self.find_and_display_duplicates(self.directory)

    def calculate_hash(self, filename, block_size=65536):
        hasher = hashlib.md5()
        with open(filename, 'rb') as f:
            for block in iter(lambda: f.read(block_size), b''):
                hasher.update(block)
        return hasher.hexdigest()

    def find_and_display_duplicates(self, directory):
        file_hashes = defaultdict(list)
        duplicates = []

        files = self.find_files(directory, self.extensions)
        total_files = len(files)
        
        for i, file in enumerate(files):
            hash_value = self.calculate_hash(file)
            file_hashes[hash_value].append(file)
            progress = (i + 1) * 100 // total_files
            self.progress_updated.emit(progress)
            self.current_directory.emit(file)
        
        for hash_value, files in file_hashes.items():
            if len(files) > 1:
                duplicates.append(files)
        
        if duplicates:
            self.progress_updated.emit(100)
            self.duplicates_found.emit(duplicates)
        else:
            self.emit_no_duplicates()

    def find_files(self, directory, extensions):
        file_list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.lower().endswith(ext.strip()) for ext in extensions):
                    file_path = os.path.join(root, file)
                    file_list.append(file_path)
        return file_list

    def emit_no_duplicates(self):
        self.no_duplicates_found.emit()
        

class DuplicateFinderUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Duplicate File Finder")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.file_extension_label = QLabel("File Extensions (comma-separated):")
        self.layout.addWidget(self.file_extension_label)

        self.file_extension_input = QLineEdit()
        self.layout.addWidget(self.file_extension_input)

        self.delete_duplicates_checkbox = QCheckBox("Delete Duplicates")
        self.layout.addWidget(self.delete_duplicates_checkbox)

        self.move_duplicates_checkbox = QCheckBox("Move Duplicates")
        self.layout.addWidget(self.move_duplicates_checkbox)

        self.current_directory_label = QLabel()
        self.layout.addWidget(self.current_directory_label)

        self.progress_animation = QLabel(self)
        self.progress_animation.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.progress_animation)
        self.movie = QMovie("progress_animation.gif")  
        self.progress_animation.setMovie(self.movie)
        self.movie.start()

        self.scan_button = QPushButton("Scan Directory")
        self.scan_button.clicked.connect(self.scan_directory)
        self.layout.addWidget(self.scan_button)

        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

        self.set_ui_style()

        self.worker = None


        self.set_ui_style()

    def set_ui_style(self):
        self.setStyleSheet(
            "QWidget {"
            "background-color: #333;"
            "border-radius: 10px;"
            "}"
            "QTextEdit, QLineEdit, QCheckBox, QProgressBar {"
            "background-color: #555;"
            "border-radius: 5px;"
            "color: white;"
            "}"
            "QLabel {"
            "color: white;"
            "}"
            "QPushButton {"
            "background-color: #6ea9e8;"
            "color: white;"
            "border: none;"
            "border-radius: 5px;"
            "}"
            "QPushButton:hover {"
            "background-color: #5290c2;"
            "QMainWindow { background-color: #f7f7f7; }"
            "QTextEdit, QLineEdit, QCheckBox { background-color: #ffffff; border: 1px solid #ccc; border-radius: 5px; padding: 5px; }"
            "QPushButton { background-color: #6ea9e8; color: white; border: none; border-radius: 5px; padding: 8px 12px; font-weight: bold; }"
            "QPushButton:hover { background-color: #5290c2; }"
            "QProgressBar { background-color: #ffffff; border: 1px solid #ccc; border-radius: 5px; height: 20px; text-align: center; color: #555; font-weight: bold; }"
            "QProgressBar::chunk { background-color: #6ea9e8; }"
            "QLabel { color: #555; font-size: 12px; margin-top: 5px; }"
            "}"
        )

        font = QFont("Segoe UI", 10)
        self.setFont(font)

    def scan_directory(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Select Directory", options=options)
        
        if directory:
            self.text_edit.clear()
            self.progress_bar.setValue(0)
            extensions = self.file_extension_input.text().split(',')
            delete_duplicates = self.delete_duplicates_checkbox.isChecked()
            move_duplicates = self.move_duplicates_checkbox.isChecked()
            self.worker = DuplicateFinderWorker(directory, extensions, delete_duplicates, move_duplicates)
            self.worker.progress_updated.connect(self.update_progress)
            self.worker.duplicates_found.connect(self.display_duplicates)
            self.worker.no_duplicates_found.connect(self.display_no_duplicates)
            self.worker.current_directory.connect(self.update_current_directory)
            self.worker.start()

    def update_progress(self, progress):
        self.progress_bar.setValue(progress)

    def display_duplicates(self, duplicates):
        self.text_edit.append("Duplicate files found:")
        for group in duplicates:
            self.text_edit.append("Group:")
            for file in group:
                self.text_edit.append(file)
            self.text_edit.append("=" * 20)

    def display_no_duplicates(self):
        self.text_edit.append("No duplicate files found.")

    def update_current_directory(self, directory):
        self.current_directory_label.setText("Scanning: " + directory)

if __name__ == "__main__":
    run_as_admin()
    
    app = QApplication(sys.argv)
    window = DuplicateFinderUI()
    window.show()
    sys.exit(app.exec_())
