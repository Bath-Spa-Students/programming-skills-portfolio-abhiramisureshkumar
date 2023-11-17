#speed id abnormal or normal

speed =int(input("Enter the speed: "))

if speed > 24 and speed < 80:
    print("speed is normal.")
else:
    print("speed is abnormal.")