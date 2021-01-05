import json
import random
from prettytable import PrettyTable
from pprint import pprint
table=PrettyTable()

desk=random.randint(1,7)
token=random.randint(10,100)
time_remain=random.randint(10,50)
tm=str(time_remain)+str(' min')

def resturant_app():
    while True:
        user=input("""1.) Create Account \n2.) Login Account \n3.) Exite \n""")
        if user == '1':
            print("Now we are creating your account")
            create_name = input("Enter your name: ")
            create_gmail  = input("Enter gmail: ")
            create_username = input("Enter user name: ")
    
            # getting password for checking either its right or wrong
            while True:
                create_password1 = int(input("Enter password only numbers: "))
                create_password2 = int(input("Enter again password only numbers :"))
                if create_password1 == create_password2:
                    break
                else:
                    print("Password doesn't match pls! enter right password.")
        
            create_gender = input("Enter gender: ")
            create_mobile = int(input("Enter mobile number: "))
            create_region =input("Enter country name: ")
    
            create_account = {
                'Name':create_name,
                'Gmail':create_gmail,
                'Username':create_username,
                'Password':create_password1,
                'Gender':create_gender,
                'Mobile':create_mobile,
                'Country':create_region
            }
            with open('login_details.json','w') as file:
                json.dump(create_account,file)
            with open('login_details.json','r') as checking:
                check=json.load(checking)
            
    
        elif user == '2':
            with open('login_details.json','r') as checking:
                check=json.load(checking)
            login_username = input("Enter user name: ")
            login_password = int(input("Enter password only numbers: "))
            if login_username == check['Username'] and login_password == check['Password']:
                print("Wellcom to our shopping app")
                break
            else:
                print("Ops! Username & password was wrong!")
                break
        
        else:
            print("Ops! we can't find your identity")

            
    dish1 = {'Pakistani Food':[{'1.) Biryani':150},
                               {'2.) Chicken Karahi':750},
                               {'3.) Helleem':500},
                               {'4.) Mutton Karahi':1000},
                               {'5.) Kabuli Pulao':250},
                               {'6.) halwa Puri':50},
                               {'7.) Tikka':220},
                               {'8.) Chargha':1500},
                               {'9.) Seekh kabab':350},
                               {'10.) Nihari':190},
                               {'11.) Chapli Kabab':260},
                               {'12.) Paneer Handi':160},
                               {'13.) Broast':600},
                               {'14.) Muttor Pulao':160},
                               {'15.) Dahi bary':130}
                                ]
            }
    dish2 = {'Chineese Food': [{'1.) Noodles': 150},
                               {'2.) Chicken Manchorian': 750},
                               {'3.) Chiness Chicken Con Shoup': 150},
                               {'4.) Chineess Noodles Karahi': 400},
                               {'5.) Cheese Roll': 90},
                               {'6.) Corodile Soup': 250},
                               {'7.) Bat Wing Soup': 160},
                               {'8.) Chineese Chicken Shaslikh': 1500},
                               {'9.) Chineese Rice': 350},
                               {'10.) Shawarma': 190},
                               {'11.) Chicken Chineese Fried Rice': 260},
                               {'12.) Chineese Burger': 160},
                               {'13.) Chineese Chicken Pulao': 600},
                               {'14.) Chineese Paneer Burger': 160},
                               {'15.) Chicken Pizza': 1000},
                               {'16.) Chineese Wonton': 500},
                               {'17.) Chineese Cheese kabab': 260},
                               {'18.) Chineese Potli Kabab': 350},
                               {'19.) Mackoroni': 460},
                               {'20.) Chineese Chicken Pizza': 230}
                               ]
            }
    dish3 = {'Refreshment':[{'1.) Tea':50},
                            {'2.) Ice-Cream':200},
                            {'3.) Coffee':120},
                            {'4.) Mineral Water':80},
                           ]
            }
    while True:
        food = input("Pls select food \n1.) Pakistani Food \n2.) Chineese \n3.) Refreshment \n4.) Over oder")
        if food == '1':
            pprint(dish1)
            pak_food = input("Pls! select food item in this list: \t")
            if pak_food == '1':
                pak_food="Biryani"
                price=150
                print("You have select Biyani")
            elif pak_food == '2':
                price=750
                pak_food="Chicken Karahi"
                print("You have select Chicken Karahi")
            elif pak_food == '3':
                price=500
                pak_food="Haleem"
                print("You have select Haleem")
            elif pak_food == '4':
                price=1000
                pak_food="Mutton Karahi"
                print("You have select Mutton Karahi")
            elif pak_food == '5':
                price=250
                pak_food="Kabuli Pulao"
                print("You have select Kabuli Pulao")
            elif pak_food == '6':
                price=50
                pak_food="Halwa Puri"
                print("You have select Halwa Puri")
            elif pak_food == '7':
                price=220
                pak_food="Tikka"
                print("You have select Tikka")
            elif pak_food == '8':
                price=1500
                pak_food="Chargha"
                print("You have select Chargha")
            elif pak_food == '9':
                price=350
                pak_food="Seek Kabab"
                print("You have select Seek Kabab")
            elif pak_food == '10':
                price=190
                pak_food="Nihari"
                print("You have select Nihari")
            elif pak_food == '11':
                price=260
                pak_food="Chapli"
                print("You have select Chapli Kabab")
            elif pak_food == '12':
                price=160
                pak_food="Paneer Handi"
                print("You have select Paneer Handi")
            elif pak_food == '13':
                price=600
                pak_food="Broast"
                print("You have select Broast")
            elif pak_food == '14':
                price=160
                pak_food="Muttor Pulao"
                print("You have select Muttor Pulao")
            elif pak_food == '15':
                price=130
                pak_food="Dahi Bary"
                print("You have select Dahi Bary")
            elif pak_food > '15' or pak_food < '1':
                print('Invalid! Enter')
        elif food == '2':
            pprint(dish2)
            chin_food = input("Pls! select food in this list: \t")
            if chin_food == '1':
                price2=150
                chin_food="Noodles"
                print("You have select Noodles")
            elif chin_food == '2':
                price2=750
                chin_food="Chicken Manchorian"
                print("You have select Chicken Manchorian")
            elif chin_food == '3':
                price2=150
                chin_food="Chineese Chicken Con Soup"
                print("You have select Chineess Chicken Con Soup")
            elif chin_food == '4':
                price2=400
                chin_food="Chineess Noodles Karahi"
                print("You have select Chineess Noodles Karahi")
            elif chin_food == '5':
                price2=90
                chin_food="Cheese Roll"
                print("You have select Cheese Roll")
            elif chin_food == '6':
                price2=250
                chin_food="Corodile Soup"
                print("You have select Corodile Soup")
            elif chin_food == '7':
                price2=160
                chin_food="Bat Wing Soup"
                print("You have select Bat Wing Soup")
            elif chin_food == '8':
                price2=1500
                chin_food="Chineese Chicken Shaslikh"
                print("You have select Chineese Chicken Shaslikh")
            elif chin_food == '9':
                price2=350
                chin_food="Chineese Rice"
                print("You have select Chineese Rice")
            elif chin_food == '10':
                price2=190
                chin_food="Shawarma"
                print("You have select Shawarma")
            elif chin_food == '11':
                price2=260
                chin_food="Chineese Chicken Fried Rice"
                print("You have select Chineese Chicken Fried Rice")
            elif chin_food == '12':
                price2=160
                chin_food="Paneer Burger"
                print("You have select Chineese Paneer Burger")
            elif chin_food == '13':
                price2=600
                chin_food="Chineese Burger"
                print("You have select Chineese Burger")
            elif chin_food == '14':
                price2=160
                chin_food="Chineese Chicken Pulao"
                print("You have select Chineese Chicken Pulao")
            elif chin_food == '15':
                price2=1000
                chin_food="Pizza"
                print("You have select Pizza")
            elif chin_food == '16':
                price2=500
                chin_food="Chineese Wonton"
                print("You have select Chineese Wonton")
            elif chin_food == '17':
                price2=260
                chin_food="Chineese Cheese Kabab"
                print("You have select Chineese Cheese Kabab")
            elif chin_food == '18':
                price2=350
                chin_food="Chineese Potli Kabab"
                print("You have select Chineese Potli Kabab")
            elif chin_food == '19':
                price2=460
                chin_food="Mankroni"
                print("You have select Mackroni")
            elif chin_food == '20':
                price2=230
                chin_food="Chineese Chicken Pizza"
                print("You have select Chineese Chicken Pizza")
            elif chin_food < '1' or chin_food > '20':
                print('Invalid! Enter')
        elif food == '3':
            pprint(dish3)
            ref_food = input("Pls select refreshment item in this list: \t")
            if ref_food == '1':
                price3=50
                ref_food = "Tea"
                print('You have select Tea')
            elif ref_food == '2':
                price3=200
                ref_food = "Ice-Cream"
                print("You have select Ice-Cream")
            elif ref_food == '3':
                price3=120
                ref_food="Coffee"
                print('You have select Coffee')
            elif ref_food == '4':
                price3=80
                ref_food='Minera Water'
                print("You have select Mineral Water")
            elif ref_food < '1' or ref_food > '4':
                print("Invalid! Enter")
        elif food == '4':
            break
        elif food < '1' or food > '3':
            print("Invalid! Enter")
        else:
            print("Sorry! we can't understand")
    
    # for Module 1
    restu_module_1={
        '1.) Desk':desk,
        '2.) Pakistani Food':pak_food,
        '3.) Chineese Food':chin_food,
        '4.) Refreshment':ref_food
    }
    print(' '*35,"Module 1")
    pprint(restu_module_1)
    billing_module_2={
        '1.) Token No':token,
        '2.) Desk No':desk,
        '3.) Name':check['Name'],
        '4.) Total Items':3,
        '5.) Items Names':pak_food+', '+chin_food+', '+ref_food,
        '6.) Time Duration':tm
    }
    print(' '*35,"Module 1")
    pprint(billing_module_2)
    # using prettytable librayr for showing billinf reciept
    table.title="Reciept"
    table.field_names=['Overall','Amount']
    table.add_row(['Token',token])
    table.add_row(['Desk',desk])
    table.add_row(['Total Item',3])
    table.add_row(['amount',price+price2+price3])
    table.add_row(['Payment','Cash'])
    print(table)
    #using w & r function for storing data in json file
    with open('modules.json','w') as data:
        json.dump(restu_module_1,data)
    with open('modules.json','a') as data:
        json.dump(billing_module_2,data)

resturant_app()
