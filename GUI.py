import sys
import time
import PySimpleGUI as sg

class GUI:

    def __init__(self):
        self.layout = [
            [ # ---- First row
                sg.Text('Convert all plain-text files to xlsx files from the source to the destination')], [ # ---- New row
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
        self.window = sg.Window('ExcelWriter').Layout(self.layout)
    
    def directoryBrowse(self):
        while True:
            event, values = self.window.Read() # Run the window until an "event" is triggered
            if event == "Submit":
                return values
            elif event is None or event == "Cancel":
                return None

if __name__ == "__main__":
    print('Excel Writer v1.0')
    gui = GUI() # create GUI class
    dir_dict = gui.directoryBrowse() # get directory dict
    try:
        gui.window.Close()  # close GUI after select Folder and click on Submit
        exec(open('ExcelWriter.py').read(), dir_dict) # execute Excelwriter.py and pass dict of argument to ExcelWriter class
        time.sleep(0.5)
    except TypeError:
        print('\'NoneType\'')
