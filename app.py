from flask import Flask, abort 
current_user_id = 3

app = Flask(__name__)

users = {
    1: {"name": "Aras","email":"aras@ornek.com","secret_note": "Aras's secret note"},
    2: {"name": "Anil", "email": "anil@ornek.com", "secret_note": "Anil's secret note"},
    3: {"name": "Mehmet", "email": "mehmet@ornek.com", "secret_note": "Mehmet's secret note"},
}
@app.route('/')
def home():
    return "Welcome to profile systems. Try an address like /profile/1."

@app.route('/profile/<int:user_id>')#If someone visits an address like /profile/1 or /profile/2,store the number 1 or 2 in a variable named `user_id`.The `<int:user_id>` part automatically captures that number from the URL.
def profile(user_id):#You can use the user_id captured above here.this syntax is definition of function
    if user_id != current_user_id:
        abort(403)  #It terminates the operation and displays the standard 403 Forbidden page.
    user = users[user_id]#It retrieves the corresponding user from the previously defined users dictionary using that ID
    return f"Name: {user['name']}, Email: {user['email']}, Note: {user['secret_note']}"#It prints the information of the user who corresponds to that ID in the browser.

if __name__ == '__main__':
    app.run(debug=True)