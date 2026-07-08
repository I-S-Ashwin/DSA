class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        inv10 = [1] * (n + 1)
        inv10[n] = pow(pow10[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv10[i] = (inv10[i + 1] * 10) % MOD
            
        pref_sum = [0] * (n + 1)
        cnt = [0] * (n + 1)
        
        non_zeros = []
        
        for i in range(n):
            val = int(s[i])
            pref_sum[i + 1] = pref_sum[i] + val
            cnt[i + 1] = cnt[i]
            
            if val != 0:
                cnt[i + 1] += 1
                non_zeros.append(val)
                
        K = len(non_zeros)
        pref_val = [0] * (K + 1)
        
        for i in range(K):
            val = non_zeros[i]
            term = (val * pow10[K - 1 - i]) % MOD
            pref_val[i + 1] = (pref_val[i] + term) % MOD
            
        ans = []
        for li, ri in queries:
            S = pref_sum[ri + 1] - pref_sum[li]
            if S == 0:
                ans.append(0)
                continue
                
            L_cnt = cnt[li]
            R_cnt = cnt[ri + 1]
            
            if L_cnt == R_cnt:
                ans.append(0)
                continue
                
            V = (pref_val[R_cnt] - pref_val[L_cnt]) % MOD
            x = (V * inv10[K - R_cnt]) % MOD
            
            res = (x * S) % MOD
            ans.append(res)
            
        return ans