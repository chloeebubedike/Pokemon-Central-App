# Aim: Build a webserver to send/present data to people visiting site
from flask import Flask, render_template, redirect
import helpers


# Flask is a class. A class is a template for an object
app = Flask(__name__)


# When someone visits the / in our app run home function and return the message
@app.route('/pokemon')
def pokemon_list():
    return render_template('pokemon_list.html', pokemon_list=helpers.get_random_pokemon_list())


@app.route('/pokemon/<int:pokemon_id>')
def pokemon_info(pokemon_id):
    if pokemon_id not in helpers.FIRST_GEN_IDS:
        return redirect('/pokemon')
    pokemon = helpers.get_pokemon(pokemon_id)
    return render_template('pokemon_info.html', pokemon=pokemon)


app.run(debug=True, port=5001)
