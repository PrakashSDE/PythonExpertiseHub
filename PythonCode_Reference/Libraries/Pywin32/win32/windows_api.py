import win32api
import win32con
import win32file

# Get the version of the operating system
version = win32api.GetVersionEx()
print(version)

# Display a sample message box
win32api.MessageBox(0, 'Hello, Pywin32!', 'Pywin32', 0)

# Get the current directory
current_directory = win32api.GetFullPathName('.')
print(current_directory)

# File Operations
# Create a file
file_handle = win32file.CreateFile('test.txt', win32con.GENERIC_WRITE, 0, None, win32con.CREATE_ALWAYS, 0, None)
win32file.WriteFile(file_handle, b"Hello, Pywin32!")
win32file.CloseHandle(file_handle)

# Read the file
file_handle = win32file.CreateFile('test.txt', win32con.GENERIC_READ, 0, None, win32con.OPEN_EXISTING, 0, None)
data = win32file.ReadFile(file_handle, 1024)
print(data)
win32file.CloseHandle(file_handle)

# Delete the file
win32file.DeleteFile('test.txt')



