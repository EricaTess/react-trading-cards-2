import shelve
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def show_homepage():
    """Show the application's homepage."""

    return render_template('homepage.html')


@app.route('/cards-jquery')
def show_cards_jquery():
    """Show a jQuery implementation of this app."""

    return render_template('cards-jquery.html')


@app.route('/cards')
def show_cards():
    """Show all trading cards."""

    return render_template('cards.html')


@app.route('/api/cards')
def get_cards_json():
    """Return a JSON response with all cards in the 'database'."""

    with shelve.open('cards.shelve') as db:
        cards_list = db['cards']

    return jsonify({'cards': cards_list})


@app.route('/api/cards', methods=['POST'])
def add_card():
    """Add a new card to the 'database'."""

    name = request.form.get('name')
    skill = request.form.get('skill')

    try:
        with shelve.open('cards.shelve', writeback=True) as db:
            db['cards'].append({'name': name,
                                'skill': skill})

        return jsonify({'success': True})

    except Exception as err:
        return jsonify({'success': False,
                        'error': str(err)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
