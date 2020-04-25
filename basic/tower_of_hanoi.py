def tower_of_hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, " -> ", to_pos)
        return

    tower_of_hanoi(n - 1, from_pos, aux_pos, to_pos)

    print(from_pos, " -> ", to_pos)

    tower_of_hanoi(n - 1, aux_pos, to_pos, from_pos)
