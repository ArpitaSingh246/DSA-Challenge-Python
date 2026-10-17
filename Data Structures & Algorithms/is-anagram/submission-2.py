def mannual_counter(s):
    d = dict()
    for i in s:
        d[i] = d.get(i,0)+1
    return d


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''return Counter(s) == Counter(t)'''
        return (mannual_counter(s) == mannual_counter(t))



