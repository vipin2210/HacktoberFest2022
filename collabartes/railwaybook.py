print("\n\nTicket Booking System\n")
restart = ('Y')

#menu for ticket booking
while restart != ('N','NO','n','no'):
	print("1.Check PNR status")
	print("2.Ticket Reservation")
	option = int(input("\nEnter your option : "))

    #check PNR status
	if option == 1:
		print("Your PNR status is 2310034343")
		restart = input("\nWould you like to go back? y/n : ")
		if restart in ('n','NO','no'):
			print("Thank you")
			break        
    #ticket reservation
	elif option == 2:
		people = int(input("\nEnter no. of Ticket you want : "))
		name_l = []
		age_l = []
		sex_l = []
		for p in range(people):
			name = str(input("\nName : "))
			name_l.append(name)
			age  = int(input("\nAge  : "))
			age_l.append(age)
			sex  = str(input("\nMale or Female : "))
			sex_l.append(sex)

		restart = str(input("\nDid you forgot someone? y/n: "))
		if restart in ('y','YES','yes','Yes'):
			restart = ('Y')
		else :
			x = 0  #counter for printing name and age of passenger
			print("\nTotal Ticket : ",people)
			for p in range(1,people+1):
				print("Ticket : ",p)
				print("***************")
				print("Name : ", name_l[x])
				print("Age  : ", age_l[x])
				print("Sex : ",sex_l[x])
				print("***************")
				x += 1
#end of program


	
