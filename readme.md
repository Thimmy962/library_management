install virtualenv

mkdir library

cd library

run: python3 -m venv venv

run: git clone <this repo>

ls [should give 2 folders: backend, venv]

run: source venv/bin/activate

cd backend

run: pip install -r requirements.txt

cd library_management

<!-- You can change databaseconfigurations to what you like -->
run: python3 manage.py makemigrations lib

run: python3 manage.py migrate

<!-- create_grps is a custom command written by me to create groups in the database -->
run python3 manage.py create_grps
<!-- Now ths database is set -->

run: python3 manage.py runserver <!--  To start dev server -->

http://locolhost:<your port>/ :: this gives a list of endpoints and their descriptions