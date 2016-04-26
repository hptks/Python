def profanity_check(text):
    connection=urllib.urlopen("http://www.wdyl.com/profanity?q="+content)
    response=connection.read()
    if "true" in response:
        print("Profanity alert!!!")
    else:
        print("No swear words in the file.")
    connection.close()
    
def read_file():
    file=open("PATH TO THE FILE")
    content=file.read()
    profanity_check(content)
    file.close()

read_file()
