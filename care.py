from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    try:
        name = request.form['name']
        dob = request.form['dob']
        age = request.form['age']
        phone_no = request.form['phone_no']
        p_lefteye = request.form['p_lefteye']
        r_righteye = request.form['r_righteye']
        cost = float(request.form['cost'])  # Convert to float
        type_spectacles = request.form['type_spectacles']
        spectacles_cost = {"tommy": 1450, "frameless": 1500, "frame": 1400}[type_spectacles]
        total_cost = cost + spectacles_cost

        with open("b1.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, dob, age, phone_no, p_lefteye, r_righteye, type_spectacles, cost])

        # Redirect to the receipt route with details as query parameters
        return redirect(url_for('receipt', name=name, dob=dob, age=age, phone_no=phone_no,
                                p_lefteye=p_lefteye, r_righteye=r_righteye, cost=cost,
                                type_spectacles=type_spectacles, spectacles_cost=spectacles_cost,
                                total_cost=total_cost))
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/receipt')
def receipt():
    try:
        # Retrieve details from query parameters
        name = request.args.get('name')
        dob = request.args.get('dob')
        age = request.args.get('age')
        phone_no = request.args.get('phone_no')
        p_lefteye = request.args.get('p_lefteye')
        r_righteye = request.args.get('r_righteye')
        cost = request.args.get('cost')
        type_spectacles = request.args.get('type_spectacles')
        spectacles_cost = request.args.get('spectacles_cost')
        total_cost = request.args.get('total_cost')

        return render_template('receipt.html', name=name, dob=dob, age=age, phone_no=phone_no,
                               p_lefteye=p_lefteye, r_righteye=r_righteye, cost=cost,
                               type_spectacles=type_spectacles, spectacles_cost=spectacles_cost,
                               total_cost=total_cost)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
