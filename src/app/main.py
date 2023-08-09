from presenter.presenter import Presenter
from model.model import Model
from view.view import View

if __name__ == "__main__":
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    presenter.run()
