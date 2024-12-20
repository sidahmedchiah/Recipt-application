import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt  

class RecipeLogic:
    def __init__(self, ui):
        self.ui = ui
        self.api_key = 'd634c05b2444432d82739048d7730a78'
        self.ui.search_button_spoonacular.clicked.connect(self.find_recipes)

    def find_recipes(self):
        ingredients = self.ui.ingredients_input.text()
        if not ingredients.strip():
            QMessageBox.warning(self.ui, "Input Error", "Please enter at least one ingredient.")
            return

        url = 'https://api.spoonacular.com/recipes/findByIngredients'
        params = {
            'ingredients': ingredients,
            'number': 5,
            'apiKey': self.api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            recipes = response.json()

            if not recipes:
                QMessageBox.warning(self.ui, "No Recipes Found", "No recipes found for the given ingredients.")
                return

            self.ui.results_list.clear()
            for recipe in recipes:
                title = recipe['title']
                recipe_id = recipe['id']
                self.ui.results_list.addItem(f"{title} (ID: {recipe_id})")

            self.ui.results_list.itemClicked.connect(self.show_recipe_details)

        except requests.RequestException as e:
            QMessageBox.critical(self.ui, "Error", f"Failed to fetch recipes: {e}")

    def show_recipe_details(self, item):
        recipe_id = item.text().split(' (ID: ')[1].strip(')')

        url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
        params = {'apiKey': self.api_key}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            recipe_data = response.json()

            if recipe_data:
                title = recipe_data['title']
                instructions = recipe_data.get('instructions', 'No instructions available.')
                image_url = recipe_data.get('image', '')

                self.ui.recipe_details.clear()
                self.ui.recipe_details.append(f"Title: {title}")
                self.ui.recipe_details.append(f"Instructions: {instructions}")

                if image_url:
                    pixmap = QPixmap()
                    pixmap.loadFromData(requests.get(image_url).content)
                    self.ui.recipe_image.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))
                else:
                    self.ui.recipe_image.setText("No image available")

        except requests.RequestException as e:
            QMessageBox.critical(self.ui, "Error", f"Failed to fetch recipe details: {e}")
