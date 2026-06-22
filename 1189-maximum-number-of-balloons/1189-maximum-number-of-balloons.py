class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        result = min(min(text.count("b"),text.count("a")),min(text.count("a"),(text.count("l"))//2))
        result = min(result,min((text.count("o"))//2,text.count("n")))
        return result

