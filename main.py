import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import MainWindow
from triggers import implement_triggers
from Game import Game
from Player import Player


def main():
    # Initialize MainWindow, app, and Game
    app = QtWidgets.QApplication(sys.argv)
    player_one = Player(1)
    player_two = Player(2)
    window = MainWindow([player_one, player_two])
    new_game = Game(window, [player_one, player_two])

    # Initialize menu items
    implement_triggers(window)

    # Initialize roll button
    window.roll_button.clicked.connect(lambda: new_game.roll())

    # Open window
    window.show()
    app.exec()


if __name__ == '__main__':
    main()