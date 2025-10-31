import tkinter as tk
from PIL import Image, ImageTk
#
#grid_viksit
ASSETS = [
    ["assets/transparent.png",[100,100]],
    ["assets/cyber_security_lock1.png",[100,100]],
    ["assets/cyber_security_lock2.png",[100,100]],
    ["assets/cyber_security_vector_images.jpeg",[100,100]],
    ["assets/viksit-bharat-buildathon.jpeg",[100,100]]
]

class MainWindow:
    def __init__(self, dev: bool = False):
        self._root = tk.Tk()

        self._assets: list[ImageTk.PhotoImage] = []
        self._labels: list[tk.Label] = []

        self.label = tk.Label(
            self._root,
            text='Cyber Security\n Viksit Bharat\nBuildathon 2025',
            font=('Arial', 40),
            padx=20, pady=10
        )
        self.label.grid(column=2, row=1, columnspan=2, rowspan=2)

        self.button1 = tk.Button(
            self._root,
            text='Check for leaks'
        )
        self.button1.grid(column=2, row=4, columnspan=1, rowspan=1)

        self.button2 = tk.Button(
            self._root,
            text='Learn about Cyber Security'
        )
        self.button2.grid(column=3, row=4, columnspan=1, rowspan=1)

        self._create_and_set_label('Cyber Security\n Viksit Bharat\nBuildathon 2025')

        self._button1 = self._create_and_set_button('Check for leaks').grid(column=2, row=4, columnspan=1, rowspan=1)
        self._button2 = self._create_and_set_button('Learn about Cyber Security').grid(column=3, row=4, columnspan=1, rowspan=1)

        if dev:
            self.configure_window([840,613], 'Cyber Security[DEV]')

            for ASSET in ASSETS:
                self.add_asset(ASSET) # type: ignore

            for asset in self._assets[1:]:
                self.add_label(asset)

            for _ in range(26):
                self.add_label(self._assets[0])

            self._set_image_in_grid()


    def __enter__(self):
        return self


    def _create_image(self, file_path: str, size: tuple[int, int] | list[int]):
        # ImageTk.PhotoImage(Image.open(fp='').resize((100,100)))
        return ImageTk.PhotoImage(Image.open(fp=file_path).resize(size))


    def _set_image_in_grid(self):#, tk_object: tk.Label | tk.Button, column_pos: int, row_pos: int
        # Main 4 images
        self._labels[0].grid(column=1,row=1)
        self._labels[1].grid(column=1,row=2)
        self._labels[2].grid(column=4,row=1)
        self._labels[3].grid(column=4,row=2)

        # Padding with the transparent image
        self._labels[4].grid(column=0,row=0)
        self._labels[5].grid(column=1,row=0)
        self._labels[6].grid(column=2,row=0)
        self._labels[7].grid(column=3,row=0)
        self._labels[8].grid(column=4,row=0)
        self._labels[9].grid(column=5,row=0)

        self._labels[10].grid(column=0,row=5)
        self._labels[11].grid(column=1,row=5)
        self._labels[12].grid(column=2,row=5)
        self._labels[13].grid(column=3,row=5)
        self._labels[14].grid(column=4,row=5)
        self._labels[15].grid(column=5,row=5)

        self._labels[16].grid(column=0,row=1)
        self._labels[17].grid(column=0,row=2)
        self._labels[18].grid(column=0,row=3)
        self._labels[19].grid(column=0,row=4)

        self._labels[20].grid(column=5,row=1)
        self._labels[21].grid(column=5,row=2)
        self._labels[22].grid(column=5,row=3)
        self._labels[23].grid(column=5,row=4)

        self._labels[24].grid(column=1,row=3)
        self._labels[25].grid(column=2,row=3)
        self._labels[26].grid(column=3,row=3)
        self._labels[27].grid(column=4,row=3)

        self._labels[28].grid(column=1,row=4)
        self._labels[29].grid(column=4,row=4)


    def _create_and_set_label(self, label_text: str):
        self.label = tk.Label(
                self._root,
                text=label_text,
                font=('Arial', 40),
                padx=20, pady=10
            )
        self.label.grid(column=2, row=1, columnspan=2, rowspan=2)


    def _create_and_set_button(self, button_text):
        return tk.Button(self._root,text=button_text)


    def configure_window(self, geometry: tuple[int,int] | list[int], title: str):
        self._root.geometry('x'.join(map(str, geometry)))
        self._root.title(title)


    def add_asset(self, asset: tuple[str, list[int]]):
        self._assets.append(
            self._create_image(asset[0], asset[1])
        )


    def add_label(self, photo_image: tk.PhotoImage | ImageTk.PhotoImage):
        self._labels.append(
            tk.Label(self._root, image=photo_image)
        )


    def start(self):
        for asset in self._assets[1:]:
            self.add_label(asset)
        for _ in range(26):
            self.add_label(self._assets[0])
        self._set_image_in_grid()

        self._root.mainloop()


    def _start(self):
        self._root.mainloop()

    def __str__(self) -> str:
        return "Window of geometry 700x400"

    def __repr__(self) -> str:
        return "MainWindow"

    def __exit__(self, exc_type, exc_value, tb_value):

        print('Windows closed')


def main() -> None:
    with MainWindow(True) as root:
        root._start()

if __name__ == "__main__":
    print(f"Currently running {__file__} script.")  #
    main()
