# Dictionaries:
# We use dictionaries in situations where we want to store attributes that come in key-value pairs\
# Name: John Smith
# Email: john@gmial.com
# Phone: 1234
customer = {
    "name":"John Smith",
    "age":30,
    "is_verified":True
}
# each key should be unique, you cant use age, name and all that twice,
# but the value can be anything
# here key is name and value is john smith and so on
print(customer["name"])
print(customer.get("name"))
print(customer.get("birthdate"))
print(customer.get("birthdate","Jan 1 1980"))
customer["name"] = "Jack Smith"
print(customer["name"])

#exercise:
# type phone number in digits and translate it into words
phone = input("Phone: ")
digits_mapping = {
    "1" : " 0ne ",
    "2" : " Two ",
    "3" : " Three ",
    "4" : " Four "
}
output = ""
for number in phone:
    output += digits_mapping.get(number, "!")
print(output)

message = input(">")
words = message.split(' ')
emojis = {
    ':)' : 'smiley',
    ':(' : 'sad'
}
print(words)
output = " "
for word in words:
    output += emojis.get(word, word) + " "
print(output)
