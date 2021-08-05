class Pitch:
    pitch_list = [['◻', '◻', '◻'], ['◻', '◻', '◻'], ['◻', '◻', '◻']]

    def show_pitch(self):
        print("\n" * 20)
        for i in self.pitch_list:
            for j in i:
                print(j, end=" ")
            print()

    def x_turn(self):
        while True:
            print("  X turn X  ")
            x = int(input("type x: "))
            y = int(input("type y: "))
            if self.pitch_list[x - 1][y - 1] == '◻':
                self.pitch_list[x - 1][y - 1] = '✗'
                break

    def o_turn(self):
        while True:
            print("  O turn O  ")
            x = int(input("type x: "))
            y = int(input("type y: "))
            if self.pitch_list[x - 1][y - 1] == '◻':
                self.pitch_list[x - 1][y - 1] = 'o'
                break

    def winner_check(self):
        if self.pitch_list[0][0] == self.pitch_list[1][1] == self.pitch_list[2][2] == '✗' or \
                self.pitch_list[0][2] == self.pitch_list[1][1] == self.pitch_list[2][0] == '✗':
            print("\nX won!!!")
            return True
        elif self.pitch_list[0][0] == self.pitch_list[1][1] == self.pitch_list[2][2] == 'o' or \
                self.pitch_list[0][2] == self.pitch_list[1][1] == self.pitch_list[2][0] == 'o':
            print("\nO won!!!")
            return True
        else:
            for i in range(3):
                flag = True
                flag_2 = True
                for j in range(3):
                    if self.pitch_list[i][j] != 'o':
                        flag = False
                    if self.pitch_list[j][i] != 'o':
                        flag_2 = False
                if flag_2 or flag:
                    self.show_pitch()
                    print("\nO won!!!")
                    return True

            for i in range(3):
                flag = True
                flag_2 = True
                for j in range(3):
                    if self.pitch_list[i][j] != '✗':
                        flag = False
                    if self.pitch_list[j][i] != '✗':
                        flag_2 = False
                if flag_2 or flag:
                    self.show_pitch()
                    print("\nX won!!!")
                    return True

    def start_game_for_two(self):
        while True:
            self.show_pitch()
            self.x_turn()
            if self.winner_check():
                break
            self.show_pitch()
            self.o_turn()
            if self.winner_check():
                break


b = Pitch()
b.start_game_for_two()