class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[first]
        for i in encoded:
            arr.append(i^first)
            first=i^first
        return arr
