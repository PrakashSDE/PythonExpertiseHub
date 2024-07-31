import win32com.client

# Create a new instance of Word
word = win32com.client.Dispatch("Word.Application")

# Make Word visible
word.Visible = True

# Add a new document
document = word.Documents.Add()

# Write text to the document
document.Content.Text = "Hello, PyWin32 and COM!"

# Close Word
word.Quit()
