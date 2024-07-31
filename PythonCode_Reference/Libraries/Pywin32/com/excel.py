import win32com.client

# Create a new instance of Excel
excel = win32com.client.Dispatch("Excel.Application")

# Make Excel visible
excel.Visible = True

# Add a new workbook
workbook = excel.Workbooks.Add()

# Access the active sheet
sheet = workbook.ActiveSheet

# Write data to cells
sheet.Cells(1, 1).Value = "Hello"
sheet.Cells(1, 2).Value = "PyWin32"
