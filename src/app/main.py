"""
This is the main module of the application.
It coordinates the interaction between the model, view, and presenter components.
"""

from presenter import presenter
from model import model
from view import view

if __name__ == "__main__":
    model = model.Model()
    view = view.View()
    presenter = presenter.Presenter(model, view)
    presenter.run()
