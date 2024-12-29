class BoyerMoore:
    def __init__(self, pattern):
        self.pattern = pattern
        self.m = len(pattern)
        self.badChar = self.badCharHeuristic(pattern)

    def badCharHeuristic(self, pattern):
        badChar = [-1] * 256
        for i, char in enumerate(pattern):
            badChar[ord(char)] = i
        return badChar

    def search(self, text):
        n = len(text)
        s = 0 
        match_positions = [] 

        while s <= n - self.m:
            j = self.m - 1

            while j >= 0 and self.pattern[j] == text[s + j]:
                j -= 1

            if j < 0:
                match_positions.append(s)
                s += (self.m - self.badChar[ord(text[s + self.m])] 
                      if s + self.m < n else 1)
            else:
                s += max(1, j - self.badChar[ord(text[s + j])])
        
        return match_positions

    def run(self, text):
        return self.search(text)