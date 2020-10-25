class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        numSoldiers  = [(sum(row), idx) for idx, row in enumerate(mat)]
        return [x[1] for x in sorted(numSoldiers)[:k]]
        