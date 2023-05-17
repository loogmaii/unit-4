from flask import Flask, render_template, request, redirect, make_response, send_from_directory, url_for
from my_lib import database_worker, encrypt_password, check_password
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)



def create_database():
    db = database_worker("social_net.db")
    query_user = """CREATE table if not exists petowners (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT,
        password TEXT
    )
    """
    query_pet = """CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            pet TEXT,
            petname TEXT,
            breed TEXT,
            description TEXT,
            petowner_id INTEGER,
            FOREIGN KEY (petowner_id) REFERENCES petowners(id) on delete cascade
            )
            """
    query_post = """CREATE table if not exists posts(
        id INTEGER PRIMARY KEY,
        pet TEXT,
        title VARCHAR(100),
        content TEXT,
        petowner_id INTEGER,
        image TEXT,
        FOREIGN KEY (petowner_id) REFERENCES petowners(id) on delete cascade
    )
    """


    db.run_save(query_user)
    db.run_save(query_pet)
    db.run_save(query_post)
    db.close()

@app.route('/file/<filename>')
def file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.cookies.get('username', 'pet'):
        print('hi')
        username = request.cookies.get('username')
        pet = request.cookies.get('pet')
        print(username,pet)
    UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'UPLOAD_FOLDER')
    print(os.path.isdir(UPLOAD_FOLDER))
    if request.method == 'POST':
        image = request.files['image']
        filename = secure_filename(image.filename)
        image.save(os.path.join(UPLOAD_FOLDER, filename))
    else:
        filename = None
    db = database_worker('social_net.db')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        print(f'{title},{content}')
        create_post = (
            f"INSERT INTO posts (pet, title, content, image, petowner_id) VALUES ('{pet}','{title}', '{content}', '{filename}', '{username}')")
        db.run_save(query=create_post)

        return redirect(url_for('profile', username=username))

    posts = db.run_query(f"SELECT * FROM posts WHERE petowner_id='{username}'")
    return render_template('create post.html', posts=posts)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    msg = ""
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        passwd = request.form['passwd']
        db = database_worker('social_net.db')
        new_user = f"""INSERT INTO petowners(username, email, password) 
                      VALUES ('{username}', '{email}', '{encrypt_password(passwd)}')"""
        db.run_save(new_user)
        db.close()

        # Create a response object
        response = make_response(redirect(url_for('build_pet', user_id=username)))

        # Set a cookie with the username
        response.set_cookie('username', username)

        return response
    return render_template("signup.html")


@app.route('/buildpet')
def build_pet():
    return render_template("buildurpet.html")


@app.route('/chameleon', methods=["GET", "POST"])
def chameleon():
    # Here you can read the cookie
    if request.cookies.get('username'):
        print("The cookie was found")
        username = request.cookies.get('username')
    if request.method == "POST":
        petname = request.form['petname']
        breed = request.form['breed']
        description = request.form['description']
        print(petname)
        db = database_worker('social_net.db')
        # Insert the pet details into the pets table
        new_pet = f"""INSERT INTO pets (pet, petname, breed, description, petowner_id) 
                              VALUES ('chameleon', '{petname}', '{breed}', '{description}', '{username}')"""
        db.run_save(new_pet)
        print('save')
        db.close()
        return redirect(url_for('profile', username=username))
    return render_template("cham.html")

@app.route('/dog', methods=["GET", "POST"])
def dog():
    # Here you can read the cookie
    if request.cookies.get('username'):
        print("The cookie was found")
        username = request.cookies.get('username')
    if request.method == "POST":
        petname = request.form['petname']
        breed = request.form['breed']
        description = request.form['description']
        print(petname)
        db = database_worker('social_net.db')
        # Insert the pet details into the pets table
        new_pet = f"""INSERT INTO pets (pet, petname, breed, description, petowner_id) 
                              VALUES ('dog', '{petname}', '{breed}', '{description}', '{username}')"""
        db.run_save(new_pet)
        print('save')
        db.close()
        return redirect(url_for('profile', username=username))
    return render_template("dog.html")

@app.route('/hamster', methods=["GET", "POST"])
def hamster():
    # Here you can read the cookie
    if request.cookies.get('username'):
        print("The cookie was found")
        username = request.cookies.get('username')
    if request.method == "POST":
        petname = request.form['petname']
        breed = request.form['breed']
        description = request.form['description']
        print(petname)
        db = database_worker('social_net.db')
        # Insert the pet details into the pets table
        new_pet = f"""INSERT INTO pets (pet, petname, breed, description, petowner_id) 
                              VALUES ('hamster', '{petname}', '{breed}', '{description}', '{username}')"""
        db.run_save(new_pet)
        print('save')
        db.close()
        return redirect(url_for('profile', username=username))
    return render_template("hamster.html")



@app.route('/bird', methods=["GET", "POST"])
def bird():
    # Here you can read the cookie
    if request.cookies.get('username'):
        print("The cookie was found")
        username = request.cookies.get('username')
    if request.method == "POST":
        petname = request.form['petname']
        breed = request.form['breed']
        description = request.form['description']
        print(petname)
        db = database_worker('social_net.db')
        # Insert the pet details into the pets table
        new_pet = f"""INSERT INTO pets (pet, petname, breed, description, petowner_id) 
                              VALUES ('bird', '{petname}', '{breed}', '{description}', '{username}')"""
        db.run_save(new_pet)
        print('save')
        db.close()
        return redirect(url_for('profile', username=username))
    return render_template("bird.html")

@app.route('/cat', methods=["GET", "POST"])
def cat():
    # Here you can read the cookie
    if request.cookies.get('username'):
        print("The cookie was found")
        username = request.cookies.get('username')
    if request.method == "POST":
        petname = request.form['petname']
        breed = request.form['breed']
        description = request.form['description']
        print(petname)
        db = database_worker('social_net.db')
        # Insert the pet details into the pets table
        new_pet = f"""INSERT INTO pets (pet, petname, breed, description, petowner_id) 
                              VALUES ('cat', '{petname}', '{breed}', '{description}', '{username}')"""
        db.run_save(new_pet)
        print('save')
        db.close()
        return redirect(url_for('profile', username=username))
    return render_template("cat.html")

@app.route('/profile/<username>')
def profile(username):
    if request.cookies.get('username'):
        print("The cookie was found")
        username = request.cookies.get('username')
        db = database_worker('social_net.db')
        createpf = f"""SELECT * FROM pets WHERE petowner_id ='{username}'"""
        row = db.run_query(createpf)
        get_posts_query = f"""SELECT * FROM posts WHERE petowner_id='{username}'"""
        posts = db.run_query(get_posts_query)
        db.close()
        if len(row) > 0:
            return render_template('profile.html', pet=row[0][1], petname=row[0][2], breed=row[0][3], description=row[0][4],
            username=row[0][5], posts=posts)
    return render_template('profile.html')


@app.route('/allposts')
@app.route('/allposts', methods=['GET', 'POST'])
def allposts():
    if request.cookies.get('username'):
        print("The cookie was found")
        username = request.cookies.get('username')
        db = database_worker('social_net.db')

        # Get the pet filter from the request form or set it to an empty string
        pet_filter = request.form.get('pet-filter', '')

        # Build the query string based on the pet filter
        if pet_filter:
            get_posts_query = f"SELECT * FROM posts WHERE pet='{pet_filter}'"
        else:
            get_posts_query = "SELECT * FROM posts"

        posts = db.run_query(get_posts_query)
        db.close()
        return render_template('all posts.html', posts=posts, pet_filter=pet_filter)

    return render_template('all posts.html')


@app.route('/',methods=['GET', 'POST'])
def hi():
    return render_template("start.html")

@app.route('/login',methods=['GET', 'POST'])
def login():
    msg = ""
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['passwd']
        if len(username)>0 and len(passwd)>0:
            db = database_worker('social_net.db')
            user = db.search(f"SELECT * from petowners where username='{username}'")
            if user:
                user = user[0] # search returns a list, so here I select one
                id, username, email, hash = user
                if check_password(hashed_password=hash, user_password=passwd):
                    resp = make_response(redirect(url_for('profile', username=username)))
                    resp.set_cookie('username', f"{username}")
                    return resp
                else:
                    msg='Incorrect username or password'
            else:
                return redirect(url_for('profile', username=username))
    return render_template("login.html", message = msg)



create_database()


if __name__ == "__main__":
    app.debug = True  # setting the debugging option for the application instance
    app.run()
