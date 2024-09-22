wish_height = int(input())
lose_jump = 0
jumps = 0

jump_height = wish_height - 30

while jump_height <= wish_height:
    jump = int(input())
    jumps += 1

    if jump > jump_height:
        if jump_height >= wish_height:
            print(f'Tihomir succeeded, he jumped over {jump_height}cm after {jumps} jumps.')
            break
        jump_height += 5
        lose_jump = 0
    else:
        lose_jump += 1
        if lose_jump == 3:
            print(f'Tihomir failed at {jump_height}cm after {jumps} jumps.')
            break
            