from CreateUser import User

Input_Bitcoin_Address = input("Enter your Address : ")
Input_Bitcoin_Alias = input('Enter your preferred alias :')
NewUser = User()
NewUser.set_bitcoin_address(Input_Bitcoin_Address)
NewUser.create()
print(NewUser.show_keys())
