---For latest Update---
Link: https://github.com/ballsai/ExcelWriter

--- User ---
# Run Script #
1) Go to dist/GUI/ and click on GUI.exe 
2) Select source files folder
3) Select destination folder
4) Click on submit

--- Developer ---
# Prepare Step #
1) Install python
    Link = https://realpython.com/installing-python/
2) Install Dependencies
    pip install re
    pip install pandas
    pip intsall xlsxwriter

# Executable one folder creation #
1) Install pyinstaller
    pip install pyinstaller
2) Downgrade pandas module and numpy module
    pip install pandas==0.24.1
    pip install numpy==1.16.1
3) Create Executable 
    pyinstaller --onedir --hidden-import=FileReader --hidden-import=DataFrameBuilder --hidden-import==ExcelBuilder GUI.py
4) Then copy script
    copy FileReader.py to dist/GUI
    copy DataFrameBuilder to dist/GUI
    copy ExcelBuilder to dist/GUI
