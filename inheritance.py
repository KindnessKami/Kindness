class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.phone = phone_number
        self.balance = account_balance

    def send_money(self, amount, recipient):
        if self.balance >= amount:
            self.balance = -amount
            print(f"{amount} KES sent to {recipient} successful")
        else:
            print("insufficient balance")


class Personal_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buyairtime(self, amount):
        if self.balance >= amount:
            self.balance = amount
            print(f"{amount} KES airtime bought successfully")


class Business:
    def __init__(self, business_name, account_balance, phone_number):
        self.business_name = business_name

    def receive_money(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received successfully")


personal = Personal_Mpesa(500, 722271809, 41457690)
personal.send_money(450, 7333495653)
personal.buyairtime(25)

buss=Business("Kindo",5800, 789530211)
