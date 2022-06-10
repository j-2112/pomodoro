import PySimpleGUI as sg
from win10toast import ToastNotifier


FONT = ("Courier", 12)
SIZE_1 = (20, 1)
SIZE_2 = (4, 1)
SIZE_3 = (10, 1)


sg.theme('DarkBlue')

layout = [[sg.Txt("Task", SIZE_2, font=FONT), sg.InputText("Your Task Here", SIZE_1, font=FONT)],
          [sg.Txt("Please Select Time: ", SIZE_1, font=FONT), sg.Spin([i for i in range(5, 121, 5)], initial_value=20,
           size=SIZE_2, font=FONT, key="-INI_TIME-")],
          [sg.Txt("00:00:00", size=(20, 2), justification='center', font=(FONT[0], 28), key="-TIMER-")],
          [sg.Button('Play', SIZE_2,), sg.Cancel(font=FONT)]]

window = sg.Window('Pomodoro Timer', layout)

while True:
    event, values = window.read(1000)
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break


window.close()