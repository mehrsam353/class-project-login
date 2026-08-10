class User:
    def __init__(self, username, password , email):
        self.username = username
        self.password = password
        self.email = email

    def buyCoruse(self):
        print(f"{self.username} can buy coruse at {self.email}")

    def sellCoruse(self):
        print(f"{self.username} can sell coruse at {self.email}")

    def readCoruse(self):
        print(f"{self.username} can read coruse at {self.email}")


myUser = User("myUser", "2345", "myUser@gamil.com")
mehrsam = User("mehrsam", "2345", "mehrsam31@gmail.com")

myUser.buyCoruse()
mehrsam.sellCoruse()
mehrsam.readCoruse()
myUser.sellCoruse()