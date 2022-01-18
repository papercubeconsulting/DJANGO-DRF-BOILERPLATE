import os
# Generating App migrations
print("1. Make migrations of the app...")
try:
    print("1.1 Make migrations of the main app...")
    os.system('python manage.py makemigrations')
except:
    print("1.1 ERROR: Make migrations of the main app it is not possible")
try:
    print("1.2 Make migrations of the app pethospital ...")
    os.system('python manage.py makemigrations pethospital ')
except:
    print("1.2 ERROR: Make migrations of the app pethospital it is not possible")
# Migrating DB
try:
    print("2. Migrate DB of the app...")
    os.system('python manage.py migrate')
except:
    print("2. ERROR: Migrate DB of the app it is not possible")
# DB feed
print("3. Feeding DB of the app with default data...")
try:
    print("3.1. Saving staff roles in BD...")
    os.system('python manage.py loaddata ./startup/DBfoods/staff_roles.json')
except:
    print("3.1. ERROR: Save staff roles it is not possible")