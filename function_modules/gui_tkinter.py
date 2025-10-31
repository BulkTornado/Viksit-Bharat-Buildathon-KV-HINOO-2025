import tkinter as tk
from PIL import Image, ImageTk
import json
from tabulate import tabulate
if __name__ == '__main__':
    from connection_module import ConnectToMySQL
else:
    from function_modules import ConnectToMySQL


try:
    with open('configuration.json', 'r') as config_file:
        configuration = json.load(config_file)
except Exception as exc:
    with open('..configuration.json', 'r') as config_file:
        configuration = json.load(config_file)
#
#grid_viksit
ASSETS = configuration.get('assets')
GEOMETRY = configuration.get('geometry')
TITLE = configuration.get('title')
USER = configuration.get('user')
PASSWD = configuration.get('passwd')
DATABASES = configuration.get('databases')

def check_email_address_in_database(email: str):
    _: list[str]= []
    with ConnectToMySQL('localhost', USER, PASSWD) as conn_ob:
        for database in DATABASES:
            conn_ob.execute_sql_query(f'USE {database[0]};')

            conn_ob.execute_sql_query(f'SELECT * FROM customer_information WHERE customer_email_address = \'{email}\';')
            result_set = conn_ob.fetch_data()

            if result_set and len(result_set) == 1:
                cust_info_columns = [desc[0] for desc in conn_ob.get_column_name()] # type: ignore
                _.append(tabulate(result_set, headers=cust_info_columns, tablefmt='grid'))

                c_id = result_set[0][0] # type: ignore
                conn_ob.execute_sql_query(f'SELECT * FROM transactions_table WHERE customer_id = {c_id};')
                trans_table_columns = [desc[0] for desc in conn_ob.get_column_name()] # type: ignore
                _.append(tabulate(conn_ob.fetch_data(), headers=trans_table_columns, tablefmt='grid'))
            else:
                _.append('')
                _.append('')
    return _



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

        self.label = tk.Label(
                self._root,
                text='Cyber Security\n Viksit Bharat\nBuildathon 2025',
                font=('Arial', 40),
                padx=20, pady=10
            )
        self.label.grid(column=2, row=1, columnspan=2, rowspan=2)

        self._button1 = tk.Button(self._root,text='Check for leak', command=self.open_window_to_get_email).grid(column=2, row=4, columnspan=1, rowspan=1)
        self._button2 = tk.Button(self._root,text='Learn about Cyber Security').grid(column=3, row=4, columnspan=1, rowspan=1)
        for ASSET in ASSETS:
            self.add_asset(ASSET) # type: ignore

        for asset in self._assets[1:]:
            self.add_label(asset)

        for _ in range(26):
            self.add_label(self._assets[0])

        self._set_image_in_grid()

        self.configure_window(GEOMETRY, f'{TITLE}{"[DEV]" if dev else ""}')


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

    def open_window_to_get_email(self):
        self._email_window = tk.Toplevel(self._root)
        self._email_window.title('EMAIL WINDOW')
        self._email_window.geometry('1000x1000')

        self._label1 = tk.Label(self._email_window, text='Enter your e-mail')
        self._label1.config(font=('Consolas', 30))
        self._label1.grid(column=0, row=0, columnspan=2)

        self._submit_email = tk.Button(self._email_window, text='SUBMIT EMAIL', command=self._submit_email_button)
        self._submit_email.grid(column=2, row=1)

        self._entry = tk.Entry(self._email_window)
        self._entry.config(font=('Ink Free', 15))
        self._entry.grid(column=0, row=1, columnspan=2)


    def _submit_email_button(self):
        self._email_address = self._entry.get()
        _ = check_email_address_in_database(self._email_address)

        self._label2 = tk.Label(self._email_window, text=_[0])
        self._label3 = tk.Label(self._email_window, text=_[1])
        self._label4 = tk.Label(self._email_window, text=_[2])
        self._label5 = tk.Label(self._email_window, text=_[3])

        self._label2.grid(column=0, row=2)
        self._label3.grid(column=0, row=3)
        self._label4.grid(column=0, row=4)
        self._label5.grid(column=0, row=5)



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
