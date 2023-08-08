from presenter.presenter import Presenter
from model.model import *
from view.view import View

import customtkinter

if __name__ == "__main__":
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    presenter.run()
