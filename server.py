from flask import Flask, render_template, url_for, request, redirect
import csv 
app = Flask(__name__)
print(__name__)

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')
        
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database2.write('\n')
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, try again!'



# @app.route('/')
# def hello_world():
#     print(url_for('static', filename='pencil.ico'))
#     return render_template('index.html')

if __name__ == '__main__' :
   app.run(debug=True)
