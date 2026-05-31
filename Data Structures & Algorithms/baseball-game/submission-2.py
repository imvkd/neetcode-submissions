class Solution:
    def isDigit(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def calPoints(self, operations: List[str]) -> int:
        score = []

        for i in operations:
            if i == '+':
                score.append(score[-1] + score[-2])
            elif i == 'C':
                score.pop()
            elif i == 'D':
                score.append(2 * score[-1])
            else:
                score.append(int(i))
        # print(score)

        return sum(score)