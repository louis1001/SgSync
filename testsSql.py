from dataAccess import dbConnection

my_name = 'thirduser'
my_email = '1234@ltt.com'
my_pass = 'realsecurepass'

me = dbConnection.User(my_name, my_pass, my_email)

success = dbConnection.signup(me.name, me.email, me.password)

if success:
    print("Logged in\nWelcome, %s" % usr_name)