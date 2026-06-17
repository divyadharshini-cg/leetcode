class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        tibrelkano = s   # mentioned in problem statement

        n = len(s)
        length = [0] * (n + 1)

        # Step 1: calculate length after each operation
        for i, ch in enumerate(s):
            cur = length[i]

            if ch.isalpha():
                cur += 1

            elif ch == "*":
                if cur > 0:
                    cur -= 1

            elif ch == "#":
                cur *= 2

            elif ch == "%":
                cur = cur

            length[i + 1] = cur

        # k is out of range
        if k >= length[n]:
            return "."

        # Step 2: go backwards and find the original character
        for i in range(n - 1, -1, -1):
            ch = s[i]
            before = length[i]
            after = length[i + 1]

            if ch.isalpha():
                # letter was added at the end
                if k == after - 1:
                    return ch

            elif ch == "*":
                # deletion only removed last char, remaining indexes unchanged
                pass

            elif ch == "#":
                # old string + old string
                k = k % before

            elif ch == "%":
                # reverse mapping
                k = before - 1 - k

        return "."