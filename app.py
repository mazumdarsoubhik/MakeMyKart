from flask import Flask, render_template, request
from model import LLM
import json

app=Flask(__name__)

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

@app.route("/", methods=["GET", "POST"])
def home_page():

    return render_template('index.html', url="https://via.placeholder.com/400", headline="User Preference")

@app.route("/dish", methods=["GET"])
def menu_page():
    if request.method == "GET":
        user_preference = request.args.get("user_preference")
        print("User Preference :: ", user_preference)
        dish_list = LLM.get_dish_suggestion(user_preference)
        data = {"status": 200, "description": "Correct specification", "data": json.dumps(dish_list) }
        return json.dumps(data)
    else:
        return {"status": 404, "description": "Please specify your preference correctly"}

@app.route("/ingredient", methods=["GET"])
def ingredients_page():
    # i/p : [{"dish_name": abd, "serves": 3}, {"dish_name":bsa, "serves":3}]
    selected_menu = request.form["selected_menu"]
    selected_menu = list(selected_menu)
    ingredient_list=[]
    for dish in selected_menu:
        ingredients_data = LLM.get_ingredients(dish)
        ingredient_list.extend(ingredients_data)
    data = {"status": 200, "description": "Correct specification", "data": json.dumps(ingredient_list) }
    return json.dumps(data)
    