install virtualenv

mkdir library

cd library

run: python3 -m venv venv

run: git clone

ls [should give 2 folders: backend, venv]

run: source venv/bin/activate

cd backend

run: pip install -r requirements.txt

cd library_management

run: python3 manage.py makemigrations lib

run: python3 manage.py migrate

run python3 manage.py create_grps

run: python3 manage.py runserver

http://locolhost:/ :: this gives a list of endpoints and their descriptions


For Docker