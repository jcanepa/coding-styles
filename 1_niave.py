# scenario: a secret club's guest list
# select non-members are on a guest list
# they will arrive with a code, multiple people might have the same code
# guests arrive and tell us their name and a code
# check whether or not they are on the list
# if they are, we check whether the code is registered to them
# if it is, we "let them in" and check their name off and mark the code as expired
# if their name is not on the list, or the code they have is invalid, they are sent away

# codes
p_1 = "oof"
p_2 = "rab"
p_3 = "zab"

# guests with assigned codes
guest_list = {
    "Ace": p_1,
    "Bear": p_2,
    "Joey": p_3,
    "Teddy": p_1,
    "Wes": p_3
}

expired_codes = []

class Guest:
    name: str
    code: str

    def __init__(self, name, code):
        """
        Initialize a new Guest instance.

        :param name: The name of the guest.
        :param code: The code associated with the guest.
        """
        self.name = name
        self.code = code

    def __str__(self):
        """
        Return a string representation of the Guest instance.
        """
        return f"Guest(name='{self.name}', code='{self.code}')"

def knock_on_door(guest):
    print(guest.name, 'is attempting to get in with code', guest.code)

    if not is_on_list(guest.name): return

    # name is on list, check the promo code

def is_on_list(name):
    return name in guest_list

guests = []
for name, code in guest_list.items():
    guests.append(Guest(name, code))

while guests:
    knock_on_door(guests.pop())
print('Guest queue is empty.')
