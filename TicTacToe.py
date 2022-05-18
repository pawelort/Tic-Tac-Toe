class tic_tac_toe:
    def __init__(self):
        self.players_moves = [[" ", " ",  " "], [" ", " ",  " "], [" ", " ",  " "]]
        self.sum_of_x = 0
        self.sum_of_o = 0
        self.sum_empty = 0
        self.state = "Xmoves"

    def screen_printout(self):
        return input("Enter the coordinates:")



    def user_input(self, user_moves):
        self.user_input_conversion(user_moves)
        self.playground()
        self.result()



    def moves(self, user_input):
        self.players_moves = [[user_input[j] for j in range(i, i + 3)] for i in range(0, len(user_input), 3)]


    def playground(self):
        print("---------")
        print(f"| {self.players_moves[0][0]} {self.players_moves[0][1]} {self.players_moves[0][2]} |")
        print(f"| {self.players_moves[1][0]} {self.players_moves[1][1]} {self.players_moves[1][2]} |")
        print(f"| {self.players_moves[2][0]} {self.players_moves[2][1]} {self.players_moves[2][2]} |")
        print("---------")

    def user_input_conversion(self, coordinates):
        user_move = coordinates.split()
        freespace = [" ", "_"]
        symbol = "X" if self.state == "Xmoves" else "O"
        # if len(user_move) > 2:
        #     print("Please type coordinates - only two digits separated by space")

        for x in user_move:
            if not x.isnumeric():
                print("You should enter numbers!")
                return
            if int(x) > 3 or int(x) < 1:
                print("Coordinates should be from 1 to 3!")
                return

        if self.players_moves[int(user_move[1]) - 1][int(user_move[0]) - 1] not in freespace:
            print("This cell is occupied! Choose another one!")
        else:
            self.players_moves[int(user_move[1]) - 1][int(user_move[0]) - 1] = symbol
            self.state = "Xmoves" if self.state == "Omoves" else "Omoves"



    def result(self):
        self.sum_of_o, self.sum_of_x, self.sum_empty = [0,  0, 0]
        for i in self.players_moves:
            for j in i:
                if j == "X":
                    self.sum_of_x += 1

        for i in self.players_moves:
            for j in i:
                if j == "O":
                    self.sum_of_o += 1

        for i in self.players_moves:
            for j in i:
                if j == "_" or j == " ":
                    self.sum_empty += 1

        xo_diff = abs(self.sum_of_x - self.sum_of_o)

        x_wins = self.x_wins()
        o_wins = self.o_wins()

        if x_wins and o_wins or xo_diff >= 2:
            print("Impossible")
            self.state = "end_game"
        elif x_wins:
            print("X wins")
            self.state = "end_game"
        elif o_wins:
            print("O wins")
            self.state = "end_game"
        elif self.sum_empty == 0:
            print("Draw")
            self.state = "end_game"


    def x_wins(self):

        if self.players_moves[0] == ["X", "X", "X"]:
            return True
        if self.players_moves[1] == ["X", "X", "X"]:
            return True
        if self.players_moves[2] == ["X", "X", "X"]:
            return True
        if ["X", "X", "X"] == [x[0] for x in self.players_moves]:
            return True
        if ["X", "X", "X"] == [x[1] for x in self.players_moves]:
            return True
        if ["X", "X", "X"] == [x[2] for x in self.players_moves]:
            return True
        if ["X", "X", "X"] == [self.players_moves[0][0], self.players_moves[1][1], self.players_moves[2][2]]:
            return True
        if ["X", "X", "X"] == [self.players_moves[0][2], self.players_moves[1][1], self.players_moves[2][0]]:
            return True

    def o_wins(self):

        if self.players_moves[0] == ["O", "O", "O"]:
            return True
        if self.players_moves[1] == ["O", "O", "O"]:
            return True
        if self.players_moves[2] == ["O", "O", "O"]:
            return True
        if ["O", "O", "O"] == [x[0] for x in self.players_moves]:
            return True
        if ["O", "O", "O"] == [x[1] for x in self.players_moves]:
            return True
        if ["O", "O", "O"] == [x[2] for x in self.players_moves]:
            return True
        if ["O", "O", "O"] == [self.players_moves[0][0], self.players_moves[1][1], self.players_moves[2][2]]:
            return True
        if ["O", "O", "O"] == [self.players_moves[0][2], self.players_moves[1][1], self.players_moves[2][0]]:
            return True

# test = ("XX OO XO ")
# moves = [[test[j] for j in range(i, i + 3)] for i in range(0, len(test), 3)]
# print(moves)

tic_tac = tic_tac_toe()
tic_tac.playground()
while tic_tac.state != "end_game":
    tic_tac.user_input(tic_tac.screen_printout())

