class Account:
    def __init__(self):
        self.__account_no = None
        self.__account_bal = None
        self.__security_code = None

    def set_data(self, acc_no, acc_bal, sec_code):
        self.__account_no = acc_no
        self.__account_bal = acc_bal
        self.__security_code = sec_code

    def display(self):
        print(f"Account No: {self.__account_no}")
        print(f"Balance: {self.__account_bal}")
        print(f"Security Code: {self.__security_code}")


# Example usage
acc = Account()
acc.set_data("12345", 5000, "AB12")
acc.display()
