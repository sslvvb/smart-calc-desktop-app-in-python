"""
This is the main module of the application.
It coordinates the interaction between the model, view, and presenter components.
"""

from src.app.presenter.presenter import Presenter
from src.app.model.model import Model
from src.app.view.view import View

if __name__ == "__main__":
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    presenter.run()
