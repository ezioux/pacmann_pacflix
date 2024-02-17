from datetime import datetime
from dateutil.relativedelta import relativedelta

class pacflix():
    list_of_referral_code = []

    def __init__(self, user_name):
        self.user_name = user_name
        self.start_date = None
        self.end_date = None
        self.current_plan = None
        self.duration = 0

        pacflix.list_of_referral_code.append(self.user_name)
        print(f"Your account successfully created, share this code '{self.user_name}' with your friend")

    #---------------------------------------------------------------------------------------------------
    # Membuat paket plan untuk Pacflix (list_plan)
    #---------------------------------------------------------------------------------------------------

    def list_plan(self):
        print("List of Pacflix Plan")
        print("1. Basic Plan")
        print("SD, 1 device, Movie, Rp 120.000")
        print("2. Standard Plan")
        print("HD, 2 devices, Movie + Sports, Rp 160.000")
        print("3. Premium Plan")
        print("UHD, 4 devices, Movie + Sports + Pacflix Originals, Rp 200.000")

    #---------------------------------------------------------------------------------------------------
    # Mengecek current plan (check_plan)
    #---------------------------------------------------------------------------------------------------

    def check_plan(self):
        if self.current_plan == None:
            print("You are not subscribed yet")
        else:
            print(f"Your current plan is {self.current_plan}")
            print(f"Started subscribing since {self.start_date}")
            print(f"Subscription will end at {self.end_date}")

    #---------------------------------------------------------------------------------------------------
    # Membeli plan (purchase)
    #---------------------------------------------------------------------------------------------------

    def purchase(self, new_plan, ref_code, duration):
        total_price = 0

        if ref_code != None and ref_code in pacflix.list_of_referral_code:
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(months=duration)

            if new_plan == "Basic Plan":
                self.current_plan = "Basic Plan"
                total_price = (120_000 - (0.04 * 120_000))
                print(f"You've selected Basic Plan with referral code from {ref_code} for {total_price}")

            elif new_plan == "Standard Plan":
                self.current_plan = "Standard Plan"
                total_price = (160_000 - (0.04 * 160_000))
                print(f"You've selected Standard Plan with referral code from {ref_code} for {total_price}")

            elif new_plan == "Premium Plan":
                self.current_plan = "Premium Plan"
                total_price = (200_000 - (0.04 * 200_000))
                print(f"You've selected Premium Plan with referral code from {ref_code} for {total_price}")

            else:
                self.duration = 0
                self.start_date = None
                self.end_date = None
                print("Your selected plan is invalid")

        elif ref_code != None and ref_code not in pacflix.list_of_referral_code:
            print("Your referral code is invalid")

        elif ref_code == None:
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(months=duration)


            if new_plan == "Basic Plan":
                self.current_plan = "Basic Plan"
                total_price = 120_000
                print(f"You've selected Basic Plan for {total_price}")

            elif new_plan == "Standard Plan":
                self.current_plan = "Standard Plan"
                total_price = 160_000
                print(f"You've selected Standard Plan for {total_price}")

            elif new_plan == "Premium Plan":
                self.current_plan = "Premium Plan"
                total_price = 200_000
                print(f"You've selected Premium Plan for {total_price}")

            else:
                self.duration = 0
                print("Your selected plan is invalid")

        else:
            print("Something went wrong")

    #----------------------------------------------------------------------------------
    # Meng-upgrade plan (upgrade_plan)
    #----------------------------------------------------------------------------------        
            
    def upgrade_plan(self, new_plan):
        subs_time = self.end_date - datetime.now()
    
        if(subs_time.days > 360):
            if self.current_plan == "Basic Plan":
                if new_plan == "Standard Plan":
                    self.current_plan == "Standard Plan"
                    total_price = (160_000 - (160_000 * 0.05))
                    print(f"Upgrade to {self.current_plan} with discount for {total_price}")

                elif new_plan == "Premium Plan":
                    if new_plan == "Premium Plan":
                        self.current_plan == "Premium Plan"
                        total_price = (200_000 - (200_000 * 0.05))
                        print(f"Upgrade to {self.current_plan} with discount for {total_price}")
                    
                else:
                    print("Your selected new plan is invalid")

            elif self.current_plan == "Standard Plan":
                if new_plan == "Premium Plan":
                    if new_plan == "Premium Plan":
                        self.current_plan == "Premium Plan"
                        total_price = (200_000 - (200_000 * 0.05))
                        print(f"Upgrade to {self.current_plan} with discount for {total_price}")

                else:
                    print("Your selected new plan is invalid")

            else:
                print("You are in the highest tier plan.")

        
        elif(subs_time.days < 360):
            if self.current_plan == "Basic Plan":
                if new_plan == "Standard Plan":
                    self.current_plan == "Standard Plan"
                    total_price = 160_000 
                    print(f"Upgrade to {self.current_plan} for {total_price}")

                elif new_plan == "Premium Plan":
                    if new_plan == "Premium Plan":
                        self.current_plan == "Premium Plan"
                        total_price = 200_000 
                        print(f"Upgrade to {self.current_plan} for {total_price}")
                    
                else:
                    print("Your selected new plan is invalid")

            elif self.current_plan == "Standard Plan":
                if new_plan == "Premium Plan":
                    if new_plan == "Premium Plan":
                        self.current_plan == "Premium Plan"
                        total_price = 200_000 
                        print(f"Upgrade to {self.current_plan} for {total_price}")

            else:
                print("Your selected new plan is invalid")

        else:
            print("You are in the highest tier plan.")



            