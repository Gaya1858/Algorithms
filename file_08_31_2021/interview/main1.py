class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_length =len(pattern)
        s_arr =s.split()
        s_length =len(s_arr)
        result = 'true'
        if(p_length != s_length):
            return 'false'
        else:
            if(pattern[0] == pattern[p_length-1]) and (s_arr[0] == s_arr[s_length-1]):
                x=1
                y=p_length-2
                while x<p_length and y >=0:
                    if(pattern[x-1] == pattern[x] and s_arr[x-1] == s_arr[x]):
                        if(pattern[x] == pattern[y]) and (s_arr[x] == s_arr[y]):
                            x+=1
                            y -=1
                        else:
                            result ='false'
                            return result
                    elif (pattern[x-1] != pattern[x] and s_arr[x-1] != s_arr[x]):
                        if(pattern[x] == pattern[y]) and (s_arr[x] == s_arr[y]):
                            x+=1
                            y -=1
                        else:
                            result ='false'
                            return result
                    else:
                        result ='false'
                        return result
                return result



s =Solution()
print(s.wordPattern('aaaa','dog cat cat dog'))