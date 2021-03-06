import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_home")
def get_home():
    home = mongo.db.tasks.find()
    return render_template("home.html", home=home)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Your message has been sent")
        return redirect(url_for("get_home"))
    return render_template("contact.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                     request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])  # PROFILE PAGE
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find())
    # if existing user display profile
    if session["user"]:
        return render_template("profile.html",
                               username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/get_recipes")  # RECIPES PAGE
def get_recipes():
    recipes = list(mongo.db.recipes.find())  # gets recipes from database
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])  # ADD RECIPE
def add_recipe():
    categories = mongo.db.categories.find().sort("category_name", 1)
    if request.method == "POST":
        recipe_vegetarian = "on" if request.form.get(
            "recipe_vegetarian") else "off"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_vegetarian": recipe_vegetarian,
            "recipe_addedby": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added!")
        return redirect(url_for("get_recipes"))

    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])  # EDIT RECIPE
def edit_recipe(recipe_id):
    categories = mongo.db.categories.find().sort("category_name", 1)
    if request.method == "POST":
        recipe_vegetarian = "on" if request.form.get(
            "recipe_vegetarian") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_vegetarian": recipe_vegetarian,
            "recipe_addedby": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe updated!")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")  # DELETE RECIPE
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted!")
    return redirect(url_for("get_recipes"))


@app.route("/search", methods=["GET", "POST"])  # SEARCH RECIPES
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipe_details/<recipe_id>")  # RECIPE DETAILS
def recipe_details(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_details.html", recipe=recipe)


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("add_category"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


@app.errorhandler(404)  # 404 ERROR
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)  # 500 ERROR
def something_wrong(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
