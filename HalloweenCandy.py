from typing import List

class HalloweenCandy:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        n = len(ratings)
        candies = [1] * n #Each child gets 1 candy
        
        # Children with higher ratings than the previous child get more candies 
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Children with higher ratings than the next child get more candies
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        #O(1)
        print(f"Candy distribution: {candies}")
        print(f"Total = {sum(candies)}")
        
        return sum(candies)

# Example
result = HalloweenCandy()
ratings = [4, 9, 3, 1, 7, 6]
total_candies = result.candy(ratings)

ratings = [4, 9, 3, 1]
total_candies = result.candy(ratings)
