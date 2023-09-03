from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys

from dotenv import load_dotenv

from api.helper_service import HelperService
from api.language_helper import LanguageHelper
from models.helper_response import HelperResponse
from ui.main_window import Ui_MainWindow


class EnglishHelperWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.helper_response = None

        self.pushButton.clicked.connect(self.generate_response)

    def generate_response(self):
        helper_service = HelperService(self.plainTextEditQuestion.toPlainText())

        try:
            response = helper_service.generate_response()
            self.textBrowserAnswer.setText(response)
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Error", str(e))


if __name__ == '__main__':
    load_dotenv()
    app = QApplication(sys.argv)
    window = EnglishHelperWindow()
    window.show()
    sys.exit(app.exec())
