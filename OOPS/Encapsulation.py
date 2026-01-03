class Account:
    def __init__(self, account_number, password):
        self.account_number = account_number
        self.__password = password  # Private attribute
    
    def reset_password(self):
        print(f"Current password: {self.__password}")  # Accessible internally
        self.__password = "newpass"


acc1 = Account("12345", "abcde")
print(acc1.account_number)  
# print(acc1.__password)   # Error: not accessible
acc1.reset_password()  # Works: prints current password
