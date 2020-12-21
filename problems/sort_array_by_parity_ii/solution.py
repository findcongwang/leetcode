class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # edit the arr in place with swaps
        
        if len(A) % 2 == 0:
            # even length
            end_odd_idx = len(A) - 1
            end_even_idx = len(A) - 2
            
        else:
            # odd length
            end_even_idx = len(A) - 1
            end_odd_idx = len(A) - 2
            
        
        i = 0
        while i < max(end_odd_idx, end_even_idx):
            # print(i, A[i])
            
            if A[i] % 2 == i % 2:
                i += 1
                # print("kept")
                
            elif A[i] % 2 == 1:
                # swap with odd
                A[i], A[end_odd_idx] = A[end_odd_idx], A[i]
                end_odd_idx -= 2
                
                # print("swap odd")
            else:
                # swap with even
                A[i], A[end_even_idx] = A[end_even_idx], A[i]
                end_even_idx -= 2
                
                # print("swap even")
                
        return A
