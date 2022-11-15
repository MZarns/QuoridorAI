from console.test import Game

if __name__ == '__main__':
    num_games = 2
    a2wins = 0
    a1times = []
    a2times = []
    a1 = "minimax"
    a2 = "minimax-alpha-beta-pruning"
    a3 = "expectimax"
    a4 = "monte-carlo-tree-search"
    a5 = "mcts2"
    algorithm1 = a1
    algorithm2 = a5
    
    g = Game(algorithm1,algorithm2)
    time_array = g.test()
    a1times.append(time_array[0])
    a2times.append(time_array[1])
    if g.game_state.get_winner() == "P2":
        a2wins += 1
    print("Game 1 Complete")

    g = Game(algorithm2,algorithm1)
    time_array = g.test()
    a1times.append(time_array[1])
    a2times.append(time_array[0])
    if g.game_state.get_winner() == "P1":
        a2wins += 1
    print("Game 2 Complete")
    print(algorithm1," avg time: ",sum(a1times)/num_games)
    print(algorithm2," avg time: ",sum(a2times)/num_games)
    print(algorithm2," win rate:", a2wins/num_games)

