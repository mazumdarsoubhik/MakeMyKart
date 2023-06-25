from usellm import Message, Options, UseLLM
import json 
# Initialize the service
service = UseLLM(service_url="https://usellm.org/api/llm")

def get_dish_suggestion(user_input):
    sys_property='''You're a bot that will help user by suggesting dishes of their preference. 
    The user will give you their preference as text and according to that you have to suggest them dishes with details. You're a bot which gives output in specified format, do not give conversational output.
    Ouput format (List of JSONs): [{ "dish_name": {{ dish_name }}, "dish_description": {{ dish_description }}, "dish_cooking_time": {{ dish_cooking_time }}, "dish_calories": {{ dish_calories }} }]
    If user is not specific to a single dish then only suggest more than 3 and less than 5 dishes.
    You are in no condition going to give paragraph output you must return output as LIST of JSONs format specified above.
    Do not put any extra words other than LIST of JSON.
    '''
    user_example_ip = '''I'm bengali and I've family of size 3. We prefer our native food majorly but we also prefer north indian sometimes'''
    assistant_example_op='''[{ "dish_name": "Aloo Poshto", "dish_description": "A vegetarian dish made with potatoes and poppy seeds. The poppy seed paste gives it a unique flavor and a slight nuttiness.", "dish_cooking_time": "40 mins", "dish_calories": "200" },{ "dish_name": "Kosha Mangsho", "dish_description": "A Bengali dish made with tender mutton pieces cooked in a rich and spicy gravy.", "dish_cooking_time": "90 mins", "dish_calories": "450" },{ "dish_name": "Chole Bhature", "dish_description": "A classic North Indian dish consisting of spicy chickpeas (chole) served with deep-fried bread (bhature).", "dish_cooking_time": "60 mins", "dish_calories": "500" }]'''

    # Prepare the conversation
    messages = [
    Message(role="system", content=sys_property),
    Message(role="user", content=user_example_ip),
    Message(role="assistant", content=assistant_example_op),
    Message(role="user", content=user_input),
    ]

    options = Options(messages=messages)

    # Interact with the service
    response = service.chat(options)

    # print(response.content)
    # data = json.loads(response.content)
    data=response.content

    return data

def get_ingredients(dish_details):
    sys_property='''You'll be given a list of JSON object which will contain a food dish name as "dish_name" and number of people that are going to consume it as "serves". You're bot which gives output in specified format, do not give conversational output.
    You need to provide ingredients needed to cook the dish at home. Only suggest those ingredients that the person needs to buy.
    Input format will be like: { "dish_name": {{ dish_name }}}, "serves": {{ serves }} }
    Output format should be a list of JSONs containing item details like: [{"item": {{ item }}, "category": {{ category }}, "quantity": {{ quantity }}, "unit": {{ unit }} }]
    The unit if each item must be mathematical unit i.e gm, Kg, mL, L, pieces'''

    user_example_ip = '''{ "dish_name: "Aloo Poshto", "serves": 3}'''
    assistant_example_op='''[{"item": "Potatoes", "category": "Vegetables", "quantity": 600, "unit": "g"}, {"item": "Poppy Seeds", "category": "Spices or Seeds", "quantity": 45, "unit": "g"}, {"item": "Mustard Oil", "category": "Oil", "quantity": 30, "unit": "ml"}, {"item": "Green Chilies", "category": "Spices or Seeds", "quantity": 6, "unit": "g"}, {"item": "Turmeric Powder", "category": "Spices or Seeds", "quantity": 2.5, "unit": "g"}, {"item": "Salt", "category": "Pantry", "quantity": 5, "unit": "g"}, {"item": "Sugar", "category": "Pantry", "quantity": 1, "unit": "g"}, {"item": "Dry Red Chili", "category": "Spices", "quantity": 1, "unit": "whole"}, {"item": "Fresh Coriander", "category": "Herbs", "quantity": 15, "unit": "g"}]'''

    # Prepare the conversation
    messages = [
    Message(role="system", content=sys_property),
    Message(role="user", content=user_example_ip),
    Message(role="assistant", content=assistant_example_op),
    Message(role="user", content=dish_details),
    ]

    options = Options(messages=messages)

    # Interact with the service
    response = service.chat(options)

    # print(response.content)
    # data = json.loads(response.content)
    data=response.content

    return data

if __name__ == '__main__':
	# I_want = 'I prefer south indian and north indian food'
	# values = get_dish_suggestion(I_want)
	# print(values)

    dish_detail = '{ "dish_name": "Butter Chicken", "serves": 3 }'
    ingredients_values = get_ingredients(dish_detail)
    print(ingredients_values)