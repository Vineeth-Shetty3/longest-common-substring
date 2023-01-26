from difflib import SequenceMatcher 
def longest_substrng(s1,s2):

    seq_match = SequenceMatcher(None,s1,s2)
    match = seq_match.find_longest_match(0, len(s1), 0, len(s2))

    #return the longest substring
    if(match.size!=0):
        return(s1[match.a: match.a + match.size])
    else :
        return('longest common substring not present')
s1= 'abcdefgh'
s2 = 'wklabcdefnji'
print("original substring:\n", s1+"\n",s2)
print ("\ncommon longest substring:")
print(longest_substrng(s1,s2))