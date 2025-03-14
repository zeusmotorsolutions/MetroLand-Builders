from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listings')
def listings():
    return render_template('listings.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Received Inquiry from {name} ({email}): {message}")  # Debugging
        return render_template('contact.html', success=True)  # Pass success message
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)