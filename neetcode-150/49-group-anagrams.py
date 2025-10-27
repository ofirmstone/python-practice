class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = {}
        
        for string in strs:
            sortedString = ''.join(sorted(string))

            if sortedString in sortedStrs:
                sortedStrs[sortedString].append(string)
            else:
                sortedStrs[sortedString] = [string]
        
        return list(sortedStrs.values())
