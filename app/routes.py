from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pablo'}
    
    # Organize problems into sessions
    sessions = [
        {
            'date': 'Today',
            'problems': [
                {'title': 'Endgame #1', 'time_spent': 120, 'accuracy': 85},
                {'title': 'Tactics #42', 'time_spent': 90, 'accuracy': 92},
                {'title': 'Opening Theory #15', 'time_spent': 180, 'accuracy': 78},
            ]
        },
        {
            'date': 'Yesterday',
            'problems': [
                {'title': 'Checkmate Pattern #7', 'time_spent': 45, 
                 'accuracy': 95},
                {'title': 'Pin & Skewer #23', 'time_spent': 75, 
                 'accuracy': 88},
                {'title': 'Endgame #12', 'time_spent': 150, 
                 'accuracy': 82},
            ]
        },
        {
            'date': 'Dec 29',
            'problems': [
                {'title': 'Fork Tactics #31', 'time_spent': 60, 
                 'accuracy': 91},
                {'title': 'Rook Endgame #5', 'time_spent': 200, 
                 'accuracy': 73},
                {'title': 'Discovered Attack #18', 'time_spent': 55, 
                 'accuracy': 89},
                {'title': 'Queen Sacrifice #9', 'time_spent': 110, 
                 'accuracy': 86},
            ]
        }
    ]
    
    # Calculate stats for each session
    for session in sessions:
        problems = session['problems']
        total_problems = len(problems)
        total_time = sum(p['time_spent'] for p in problems)
        avg_accuracy = sum(p['accuracy'] for p in problems) / total_problems
        
        session['stats'] = {
            'total_problems': total_problems,
            'total_minutes': round(total_time / 60),
            'avg_accuracy': round(avg_accuracy)
        }
    return render_template('index.html', title='Home', user=user, 
                           sessions=sessions)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


    
