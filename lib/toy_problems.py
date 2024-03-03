########## Challenge 1 ##########


def bricks_moves_solution(A):
    moves = 0

    for i in range(len(A)):
        if A[i] != 10:
            difference_in_current_value = 10 - A[i]
            A[i] += difference_in_current_value
            if i + 1 < len(A):
                A[i + 1] -= difference_in_current_value
                moves += difference_in_current_value
            else:
                return -1

    return moves


########## Challenge 2 ##########
def sum_of_intergers_solution(B):
    max_sum = -1
    for i in range(len(B)):
        for j in range(i + 1, len(B)):
            sum_i = sum(int(digit) for digit in str(B[i]))
            sum_j = sum(int(digit) for digit in str(B[j]))
            if sum_i == sum_j:
                max_sum = max(max_sum, B[i] + B[j])
    return max_sum


########## Challenge  ##########
def letter_occurrence_solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = "".join([alphabet[i] for i in range(N // 2)]) * 2
    if N % 2 == 1:
        letters += alphabet[N // 2]
    return letters
