def game(terra, power=1):
    for i in terra:
        for j in i:
            if j <= power:
                power += j
            else:
                break
    return power

print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]]))  