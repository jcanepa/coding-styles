# Codes
p_1, p_2, p_3 = "oof", "rab", "zab"

# Guests with assigned codes
guest_list = {"Ace": p_1, "Bear": p_2, "Joey": p_3, "Teddy": p_1, "Wes": p_3}
expired_codes = []

# Guest class
Guest = lambda name, code: type("Guest", (object,), {"name": name, "code": code, "__str__": lambda self: f"Guest(name='{self.name}', code='{self.code}')"})()

# Functions
bounce = lambda: print("get lost")
knock_on_door = lambda guest: (
    print(f"{guest.name} is attempting to get in with code {guest.code}"),
    expired_codes.append(guest.code) if guest.name in guest_list and guest.code == guest_list[guest.name] and guest.code not in expired_codes else bounce()
)[0]

# Guest queue
guests = [Guest(name, code) for name, code in guest_list.items()]
while guests:
    knock_on_door(guests.pop())
print("Guest queue is empty.")