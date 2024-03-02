import datetime

def load(self):
    self.users = {}

    for line in self.file:
        email, password, name, created = line.strip().split(";")
        self.users[email] = (password, name, created)

class DataBase:

    def add_user(self, email, password, name):
        self.file = open("users.txt", "r")
        load(self)

        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email já existe")
            return -1

    def save(self):
        with open("users.txt", "w") as self.file:
            for user in self.users:
                self.file.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    def get_user(self, email):
        self.users = None
        self.file = open("users.txt", "r")
        load(self)
        self.file.close()
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            chave = 3
            n = 128
            cifrada = ""

            for letra in password:
              indice = ord(letra)
              nova_letra = chr((indice + chave)%n)
              cifrada = cifrada + nova_letra

            password = ""
            password = cifrada

            return self.users[email][0] == password
        else:
            return False

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]