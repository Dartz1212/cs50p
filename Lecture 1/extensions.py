"""
In a file called extensions.py,
implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends,
case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""

f = input("File name: ").lower().strip()

if f.endswith(".gif"):
    print("image/gif")
elif f.endswith(".jpg") or f.endswith(".jpeg"):
    print("image/jpeg")
elif f.endswith(".png"):
    print("image/png")
elif f.endswith(".pdf"):
    print("application/pdf")
elif f.endswith(".txt"):
    print("text/plain")
elif f.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")