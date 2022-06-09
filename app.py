from flask import Flask, request, render_template, redirect, session
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecretpassword"

boggle_game = Boggle()

@app.route('/board')
def board_init():

    board = boggle_game.make_board()
    session["INIT_BOARD"] = board

    return render_template('board.html', board=board)