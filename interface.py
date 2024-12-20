from PyQt5.QtWidgets import (QMainWindow, QLabel, QVBoxLayout,
                             QWidget, QLineEdit, QPushButton, QListWidget, QHBoxLayout, QTextEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class RecipeFinderUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recipe Finder")
        self.setGeometry(200, 200, 1000, 700)
        self.initUI()

    def initUI(self):
        
        self.setWindowIcon(QIcon('recipe_icon.ico'))

        self.setStyleSheet("background-color: #8e44ad; color: white;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title_label = QLabel("\ud83c\udf74 Recipe Finder \ud83c\udf74")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #ff6f61;")
        layout.addWidget(title_label)

        input_layout = QHBoxLayout()

        self.instructions_label = QLabel("Enter ingredients (comma-separated):")
        self.instructions_label.setFont(QFont("Arial", 14))
        self.instructions_label.setStyleSheet("color: #f1c40f;")
        input_layout.addWidget(self.instructions_label)

        self.ingredients_input = QLineEdit()
        self.ingredients_input.setFont(QFont("Arial", 14))
        self.ingredients_input.setStyleSheet("background-color: white; color: black; padding: 5px; border: 2px solid #ff6f61;")
        input_layout.addWidget(self.ingredients_input)

        self.search_button_spoonacular = QPushButton("Find Recipes on Spoonacular")
        self.search_button_spoonacular.setFont(QFont("Arial", 14, QFont.Bold))
        self.search_button_spoonacular.setStyleSheet("background-color: #ff6f61; color: white; padding: 10px; border-radius: 5px;")
        input_layout.addWidget(self.search_button_spoonacular)

        layout.addLayout(input_layout)

        self.results_list = QListWidget()
        self.results_list.setFont(QFont("Arial", 14))
        self.results_list.setStyleSheet("background-color: white; color: black; padding: 10px; border: 2px solid #8e44ad;")
        layout.addWidget(self.results_list)

        self.recipe_details = QTextEdit()
        self.recipe_details.setFont(QFont("Arial", 12))
        self.recipe_details.setStyleSheet("background-color: white; color: black; padding: 10px; border: 2px solid #8e44ad;")
        self.recipe_details.setReadOnly(True)
        layout.addWidget(self.recipe_details)

        self.recipe_image_label = QLabel("Recipe Image:")
        self.recipe_image_label.setFont(QFont("Arial", 12))
        self.recipe_image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.recipe_image_label)

        self.recipe_image = QLabel()
        self.recipe_image.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.recipe_image)
