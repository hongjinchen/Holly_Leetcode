
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digits= "23"
        numberList=list(digits)
        second=["a","b","c"]
        third=["d","e","f"]
        forth=["g","h","i"]
        fivth=["j","k","l"]
        sixth=["m","n","o"]
        seventh=["p","q","r","s"]
        eighth=["t","u","v"]
        ninth=["w","x","y","z"]
        for item in numberList:
            if item==2:
