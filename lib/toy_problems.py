class Bricks:

    def solution(self, A):
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
    

