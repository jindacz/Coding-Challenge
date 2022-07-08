# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

def findJudge(n, trust):
    '''
    PR: array with only two?
    P: use a dict to store trust and untrust [a,b] and check if dict satisfiy first 
    '''
    d = {}
    for i in range(n):
        d[i+1] = [0, 0]
    for i in range(len(trust)):       
        d[trust[i][1]][1] += 1
        d[trust[i][0]][0] += 1
    for i in range(n):

        if d[i+1][0] == 0 and d[i+1][1] == n - 1:
            return i+1        
    return -1


print(findJudge(2, [[1,2]]))
print(findJudge(3, [[1,3],[2,3]]))
print(findJudge(3, [[1,3],[2,3],[3,1]]))