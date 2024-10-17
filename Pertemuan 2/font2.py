import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profil",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25))],
                           [sg.Text("NPM    :2210010065")],
                           [sg.Text("Nama   :Khairur Rizal")],
                           [sg.Text("Kelas  :5O REGULER PAGI")],
                           [sg.Text("Matkul :PEMROGRAMAN VISUAL 3")]],
                    size=(500,200),
                    font=("Times", 18))
window.read()
window.close()