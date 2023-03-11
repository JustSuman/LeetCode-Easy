class Solution:
    def distributeCandies(self, candyType):
        typeCandy = set(candyType)
        canEat = len(candyType)//2
        if len(typeCandy) < canEat:
            return len(typeCandy)
        else:
            return canEat