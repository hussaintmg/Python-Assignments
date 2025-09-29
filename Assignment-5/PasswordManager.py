class PasswordManager:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def set_password(self, old, new):
        if old == self.__password:
            self.__password = new
            print("Password updated successfully!")
        else:
            print("Old password does not match. Update failed.")

    def check_username(self, name):
        return self.username == name

    def check_password(self, input_password):
        return self.__password == input_password


pm = PasswordManager("hussain", "1234")
print(pm.username)
pm.set_password("1234", "abcd")
pm.set_password("wrong", "xyz")
print(pm.check_password("abcd"))
