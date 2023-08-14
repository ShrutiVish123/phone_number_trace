import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number = input("enter your number with +_ _: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print(phone)#details of  phone
print(time) # time zone 
print(car) #company of sim
print(reg) #present in which country