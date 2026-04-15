class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        list1 = [char for char in s]
        list2 = [char for char in t]
        print(list1)
        print(list2)

        if Counter(list1) == Counter(list2):
                return True  

        return False        


        

       
