import sys
from PyQt5.QtWidgets import QApplication
from interface import RecipeFinderUI  
from logic import RecipeLogic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = RecipeFinderUI()
    logic = RecipeLogic(ui)
    ui.show()
    sys.exit(app.exec_())
