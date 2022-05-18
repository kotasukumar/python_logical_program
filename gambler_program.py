import random


def gambling(stake, goal):
    win_count = loss_count = game_count = 0
    while stake != 0 and stake != goal:
        game_result = random.random()
        if game_result <= 0.5:
            stake += 1
            win_count += 1
            game_count += 1
        else:
            stake -= 1
            loss_count += 1
            game_count += 1
    win_percentage = win_count/game_count*100
    loss_percentage = loss_count/game_count*100

    return win_percentage, loss_percentage, win_count


if __name__ == "__main__":
    stake = float(input("Enter the stake you have: "))
    goal = float(input("Enter your goal amount: "))
    results = gambling(stake, goal)
    print(results)
