########## Challenge 1 ##########
def solution(A):
    total_bricks = sum(A)
    target_bricks = len(A) * 10

    if total_bricks != target_bricks:
        return -1

    moves = 0
    diff = 0

    for i in range(len(A) - 1):
        diff = A[i] - 10
        A[i] -= diff
        A[i + 1] += diff
        moves += abs(diff)

    return moves


print(solution([11, 10, 8, 12, 8, 10, 11]))


########## Challenge 2 ##########
def sum_of_intergers_solution(B):
    digit_sums = {}
    max_sum = -1

    for num in B:
        digit_sum = sum(int(digit) for digit in str(num))
        if digit_sum in digit_sums:
            max_sum = max(max_sum, digit_sums[digit_sum] + num)
            digit_sums[digit_sum] = max(digit_sums[digit_sum], num)
        else:
            digit_sums[digit_sum] = num

    return max_sum if max_sum != -1 else -1


print(sum_of_intergers_solution([51, 71, 17, 42]))


########## Challenge 3 ##########
def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(N):
        result += alphabet[i % 26]
    return result


print(solution(30))
