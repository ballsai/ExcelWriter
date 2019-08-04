import sys
import PySimpleGUI as sg

class GUI:

    def directoryBrowse(self):
        layout = [
            [ # ---- First row
                sg.Text('Will convert all plain-text files to xlsx files from the source to the destination')], [ # ---- New row
                sg.Text('Source folder', size=(15, 1)), 
                sg.InputText(key="source"), 
                sg.FolderBrowse(target="source") 
            ], [ # ---- New row
                sg.Text('Destination folder ', size=(15, 1)), 
                sg.InputText(key="destination"), 
                sg.FolderBrowse(target="destination") 
            ], [ # ---- New row
                sg.Submit(), sg.Cancel()
            ],
        ]

        window = sg.Window('ExcelWriter').Layout(layout)

        while True:
            event, values = window.Read() # Run the window until an "event" is triggered
            if event == "Submit":
                return values
            elif event is None or event == "Cancel":
                return None

if __name__ == "__main__":
    result = GUI()
    dir_dict = result.directoryBrowse()
    try:
        exec(open('ExcelWriter.py').read(), dir_dict)
    except TypeError:
        print('\'NoneType\'')