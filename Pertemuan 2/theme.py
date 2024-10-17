import PySimpleGUI as sg
sg.theme("DarGreen4")
window = sg.Window(title="Profil",
                   layout=[[sg.Text("NPM    :2210010065")],
                           [sg.Text("Nama   :Khairur Rizal")],
                           [sg.Text("Kelas  :5O REGULER PAGI")],
                           [sg.Text("Matkul :PEMROGRAMAN VISUAL 3")]],
                    size=(400,200))
window.read()
window.close()