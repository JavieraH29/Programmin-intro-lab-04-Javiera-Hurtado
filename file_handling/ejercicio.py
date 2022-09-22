print("Bienvenidos")
user_input = ""

def write_file():
    file = open("file_handling/boolean.txt", "a")
    user_content = input("Ingresa el contenido\n")
    file.write(user_content +"\n")
    file.close()

def read_file():
    
    file = open(file_handling/boolean.txt, "r")
    for line in file:
        print(line)


read_file("boolean")
read_file("microsystem")
read_file("google")