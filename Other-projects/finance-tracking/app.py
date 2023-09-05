from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forex_python.converter import CurrencyRates
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import pandas as pd
import io
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = '2678eoyudjfnmp3ieowngvdslaoijfeNS'

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

c = CurrencyRates()

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def main_page():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('register'))

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    # Fetch transactions from the database and pass them to the template
    with sqlite3.connect('finance.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM transactions')
        transactions = cursor.fetchall()
    return render_template('dashboard.html', transactions=transactions)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']
        
        with sqlite3.connect('finance.db') as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
            db.commit()
        
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with sqlite3.connect('finance.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()

        if user and check_password_hash(user[1], password):
            login_user(User(user[0]))
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/add_transaction', methods=['POST'])
@login_required
def add_transaction():
    description = request.form['description']
    amount = request.form['amount']
    date = request.form['date']
    category = request.form['category']
    with sqlite3.connect('finance.db') as db:
        cursor = db.cursor()
        cursor.execute('''
        INSERT INTO transactions (description, amount, date, category)
        VALUES (?, ?, ?, ?)
        ''', (description, amount, date, category))
        db.commit()
    flash('Transaction added successfully!')
    return redirect(url_for('dashboard'))

@app.route('/graphical_reports')
@login_required
def graphical_reports():
    with sqlite3.connect('finance.db') as db:
        cursor = db.cursor()

        # Fetch data for graphical reports
        cursor.execute('SELECT category, SUM(amount) FROM transactions GROUP BY category')
        data = cursor.fetchall()
        categories = [item[0] for item in data]
        amounts = [item[1] for item in data]

        # Create and save the spending by category pie chart
        plt.figure(figsize=(10, 7))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title('Spending by Category')
        plt.savefig('static/images/report_by_category.png')

        # Monthly Expenses
        cursor.execute('SELECT strftime("%Y-%m", date) as month, SUM(amount) FROM transactions GROUP BY month')
        monthly_data = cursor.fetchall()
        months = [item[0] for item in monthly_data]
        monthly_expenses = [item[1] for item in monthly_data]
        plt.figure(figsize=(12, 7))
        plt.bar(months, monthly_expenses, color='#58a4b0')
        plt.title('Monthly Expenses')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('static/images/monthly_expenses.png')
        
        # Trend of Expenses
        plt.figure(figsize=(12, 7))
        plt.plot(months, monthly_expenses, marker='o', linestyle='-', color='#58a4b0')
        plt.title('Trend of Expenses Over Time')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('static/images/expenses_trend.png')

    return render_template('report.html')

@app.route('/export_data', methods=['GET', 'POST'])
@login_required
def export_data():
    if request.method == 'POST':
        # Get the transaction data from the form
        transactions = request.form.getlist('transaction[]')

        # Convert the transaction data to a list of dictionaries
        data = [eval(transaction) for transaction in transactions]

        # Convert data to a pandas DataFrame
        df = pd.DataFrame(data)

        # Convert the DataFrame to an Excel file in memory
        output = io.BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        # Create a response with the Excel file
        return send_file(output, as_attachment=True, download_name="transactions.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        # Handle GET request (if needed)
        # You can provide a template or some information here
        return "This route supports only POST requests for exporting data."
    
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'xls', 'xlsx'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/import_data', methods=['POST'])
@login_required
def import_data():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        try:
            df = pd.read_excel(file)
            
            if validate_imported_data(df):
                with sqlite3.connect('finance.db') as db:
                    df.to_sql('transactions', db, if_exists='append', index=False)
                
                flash('Data imported successfully!')
                # Fetch the updated transactions and render the dashboard
                with sqlite3.connect('finance.db') as db:
                    cursor = db.cursor()
                    cursor.execute('SELECT * FROM transactions')
                    transactions = cursor.fetchall()
                return render_template('dashboard.html', transactions=transactions)
                
            else:
                flash('Imported data is not valid')
        
        except Exception as e:
            flash(f'An error occurred while importing data: {str(e)}')
        
    return redirect(url_for('dashboard'))


def validate_imported_data(df):
    required_columns = ['description', 'amount', 'date', 'category']
    
    # Check if all required columns are present in the DataFrame
    if not set(required_columns).issubset(df.columns):
        return False
    
    # Check for non-empty values in each required column
    if df[required_columns].isnull().any().any():
        return False
    
    # Check for valid numeric values in the 'amount' column
    if not df['amount'].apply(lambda x: isinstance(x, (int, float)) and x >= 0).all():
        return False
    
    # Check if the 'date' column is in a valid format (e.g., YYYY-MM-DD)
    try:
        pd.to_datetime(df['date'], format='%Y-%m-%d', errors='raise')
    except ValueError:
        return False
    
    # Check if categories are valid (customize this part based on your data)
    valid_categories = ['category1', 'category2', 'category3']  # Add valid category values here
    if not df['category'].isin(valid_categories).all():
        return False
    
    # Check for valid description length (e.g., not too long)
    if not df['description'].apply(lambda x: isinstance(x, str) and len(x) <= 100).all():
        return False
    
    # Check for valid date range (e.g., not too far in the past or future)
    today = pd.to_datetime('today').normalize()
    valid_date_range = (today - pd.DateOffset(years=5), today)  # Adjust as needed
    date_series = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
    if not date_series.between(*valid_date_range).all():
        return False
    
    # Check for valid category format (e.g., no leading/trailing spaces)
    if not df['category'].apply(lambda x: isinstance(x, str) and x.strip() == x).all():
        return False
    
    # Check for positive non-zero amounts
    if not df['amount'].apply(lambda x: isinstance(x, (int, float)) and x > 0).all():
        return False
    
    # You can add more checks here based on your specific data requirements
    
    return True

@app.route('/convert_currency', methods=['POST'])
@login_required
def convert_currency():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)

    return render_template('currency_conversion.html', converted_amount=converted_amount, from_currency=from_currency, to_currency=to_currency, amount=amount)

@app.route('/search_transactions', methods=['POST'])
@login_required
def search_transactions():
    query = request.form['query']
    with sqlite3.connect('finance.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM transactions WHERE description LIKE ? OR category LIKE ?", (f"%{query}%", f"%{query}%"))
        transactions = cursor.fetchall()
    return render_template('dashboard.html', transactions=transactions)

@app.route('/delete_transaction/<int:id>', methods=['POST'])
@login_required
def delete_transaction(id):
    with sqlite3.connect('finance.db') as db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM transactions WHERE id = ?', (id,))
        db.commit()
    flash('Transaction deleted successfully!')
    return redirect(url_for('dashboard'))

# Initialize database tables
def init_db():
    with sqlite3.connect('finance.db') as db:
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            category TEXT NOT NULL
        )
        ''')
        db.commit()

init_db()

if __name__ == '__main__':
    app.run(debug=True)
