"""
This is the main module of the application.
It coordinates the interaction between the model, view, and presenter components.
"""

from presenter.presenter import Presenter
from model.model import Model
from view.view import View

if __name__ == "__main__":
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    presenter.run()
