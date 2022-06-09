from flask import Flask, render_template, url_for, request, redirect, send_file
import csv
import yagmail

app = Flask(__name__)

DOWNLOAD_FOLDER = 'downloads/'


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:route>')
def router(route=None):
    try:
        if '.html' in route:
            return render_template(route)
        else:
            return render_template(route + '.html')
    except Exception as e:
        return render_template('404.html', title = '404'), 404


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            print("got inside try catch")
            email = yagmail.SMTP(user="auto.email.tj@gmail.com", password="vfmvpukkglkgioaj")
            data = request.form.to_dict()
            user_email = data['email']
            user_subject = data['subject']
            message = data['message']
            print("data looks good so far")
            email.send(to="jankowski_tj@outlook.com",
            subject=f"PORTFOLIO WEBSITE: {user_subject}",
            contents=f"""<h2>{user_subject}</h2>
                        <h3>You have received the following message from <b>{user_email}</b></h4>
                        <h4>Message:</h4>
                        <p>{message}</p>""")
            print("problem on send")
            return redirect('thankyou.html')
        except Exception as e:
            print(e)
            return 'something went wrong....'
    else:
        return 'something went wrong'


# return downloadable file 
@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = DOWNLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')

