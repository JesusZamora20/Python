# ------------- file handling --------------- 

# .txt file
import os

txt_file= open("info.txt", "r+")

print(txt_file.read()) #read it all
print(txt_file.read(10)) #read X ammount of numbers
print(txt_file.readline())
print(txt_file.readlines()) #it creates an array of all the lines

txt_file.write("\n Even though I like Kotlin")

os.remove("info.txt")

#---------------- JSON file ----------------
import json

json_file = open("my_file.json", "w+")

json_test = {
  "name":"jesus",
  "last_name":"zamora",
  "age":35,
  "language":"python"
  "web":"https://python.org"
}


json_file.write(json_test)

#minuto 4:55




