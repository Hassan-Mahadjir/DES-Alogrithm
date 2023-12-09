from server import receiver, sender

choose = input("Do you want to send(s) or receive(r) massage: ")

if choose == "s":
    sender()

elif choose == "r":
    receiver()
