from faker import Faker

adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_title = ' Advantage Shopping'
fake = Faker(locale='en_CA')
username = fake.user_name()
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phone = fake.phone_number()
email = fake.email()
city = fake.city()
street_address = fake.street_address()
province = fake.province_abbr()
postal_code = fake.postalcode()
