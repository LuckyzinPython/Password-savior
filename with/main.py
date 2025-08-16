import time

password = str(input("What password do you want to store inside the file?: "))
name = str(input("What name do you want to put in the file?: "))

print("=" * 120)
print("Generating file...")
time.sleep(5)
with open(name, "x") as archive:
  archive.write(password)
print("Your file has been successfully generated!")
print("=" * 120)
