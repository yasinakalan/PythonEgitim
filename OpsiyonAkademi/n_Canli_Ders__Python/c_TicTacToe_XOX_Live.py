class Tic_Tac_Toe():
    def __init__(self):
        self.state = [[0,0,0],[0,0,0],[0,0,0]]    # np.zeros(9).reshape(3,3)
        self.done = 0

    def step(self, action, agent_value):    # action = [1,1]
        if (agent_value == "X" and self.control_win() == agent_value):
            self.done = 1

        if (self.state[action[0]][action[1]] != 0):
            print("Sıkıntı var!")
        else:
            self.state[action[0]][action[1]] = agent_value

    def control_win(self):
        done = 0
        for i in range(3):
            if(self.state[i][0] != 0 and self.state[i][0] == self.state[1][1] and self.state[i][0] == self.state[1][2]):
                done = 1
                return self.state[i][0]     # agent_value