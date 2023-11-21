from random import randint


class Game:

    def __init__(self, options=['Rock', 'Paper', 'Scissors']):
        self.options = options
        self.wins = 0
        self.rounds = 0

    def play(self):
        while True:
            self.rounds += 1
            print('Rock 🪨, Paper 📜, Scissors ✂️!')
            player = input('What\'s your choice? ').capitalize()
            if player not in self.options:
                print('Invalid input!')
                continue
            computer = self.options[randint(0, 2)]
            print(f'Computer: {computer}')
            if player == computer:
                print('It\'s a draw!')
            elif player == 'Rock' and computer == 'Scissors':
                self.wins += 1
                print('You win!')
            elif player == 'Paper' and computer == 'Rock':
                self.wins += 1
                print('You win!')
            elif player == 'Scissors' and computer == 'Paper':
                self.wins += 1
                print('You win!')
            else:
                print('You lose!')
            play_again = input('Play again? (y/n) ').lower()
            if play_again == 'n':
                break
        print(f'You won {self.wins} out of {self.rounds} rounds!')


if __name__ == '__main__':
    game = Game()
    game.play()
