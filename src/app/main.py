from presenter.presenter import Presenter
from model.model import Model
from view.view import View

import customtkinter

if __name__ == "__main__":
    root = customtkinter.CTk()

    model = Model()
    view = View(root)
    presenter = Presenter(model, view)

    root.mainloop()


# https://www.google.com/search?q=mvp+python+example&tbm=vid&source=lnms&sa=X&ved=2ahUKEwjBxIb_kciAAxUESfEDHaFmAawQ0pQJegQICxAB&biw=1503&bih=966&dpr=2#fpstate=ive&vld=cid:2b3e89d3,vid:eHhXoCNCI1c