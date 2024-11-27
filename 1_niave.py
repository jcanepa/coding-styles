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
    def __init__(self, name, code):
        """
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
    print(
        guest.name,
        'is attempting to get in with code',
        guest.code)

    # verify guest is on the list
    if not name in guest_list:
        return bounce()

    # verify code is assigned to guest
    if not guest.code == guest_list[guest.name]:
        return bounce()

    # code valid
    if guest.code in expired_codes:
        return bounce()

    # invalidate code
    expired_codes.append(guest.code)
    print('welcome in!')

def bounce():
    print('get lost')

guests = []
for name, code in guest_list.items():
    guests.append(Guest(name, code))

while guests:
    knock_on_door(guests.pop())
print('Guest queue is empty.')
