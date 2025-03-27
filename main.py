from bank import Bank
from customer import Customer


user1 = Customer("Tom", "Planks", "tplanks", "Luv4Cat!")
user2 = Customer("Sarah", "Sugarhill", "ssugarhill", "D1rtB$ke")

bank_users = {
    "Tom Planks": user1,
    "Sarah Sugarhill": user2
}

test = Bank()
test.opening_message()
