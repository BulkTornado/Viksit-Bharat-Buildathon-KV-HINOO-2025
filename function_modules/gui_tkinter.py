import tkinter as tk


class MainWindow:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Cyber Security")
        self.root.geometry("800x600")
        self.photo1 = tk.PhotoImage(file='images/cyber_security_lock.png') #height=100, width=100
        print(self.photo1.height(), self.photo1.width())
        self.photo2 = ...
        self.label = tk.Label(
            self.root,
            text='Cyber Security',
            font=('Arial', 40),
            padx=20, pady=10)
        self.label.pack()


    def __enter__(self):
        return self.root

    def set_image_somewhere(self, image_object: tk.PhotoImage, place: str):
        ... #self.root.pack(image_object)

    def __str__(self) -> str:
        return "Window of geometry 700x400"

    def __repr__(self) -> str:
        return ""

    def __exit__(self, exc_type, exc_value, tb_value):
        print('Windows closed')


def main() -> None:
    """root = tk.Tk()
    MainWindow(root)
    root.mainloop()"""
    with MainWindow(tk.Tk()) as root:
        root.mainloop()


if __name__ == "__main__":
    print(f"Currently running {__file__} script.")  # .split('\\')[-1]
    main()
