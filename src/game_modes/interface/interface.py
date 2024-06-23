from tkinter import Button, Frame, Label, Tk
from game_modes.game import Game


class InterfaceGame(Game):
    def start_game(self) -> None:
        root = Tk()
        root.title("FIUBLE")
        root.resizable(0, 0)

        container = Frame(root, bg="black", padx=15, pady=15)
        container.grid()
        Label(container,
                text="Welcome!",
                bg="black",
                fg="white",
                pady="20",
            ).grid(column=0, row=0)
        Button(container, text="Close", command=root.destroy).grid(column=0, row=1)

        root.mainloop()