""" python excise.
"""
#from collections import Counter

# FAQ one
def findMaxTimes(seq):
    # is it a good method to use library ?
	#dic = Counter(seq)
	#(h, *rest) = dic.keys()
    seqSet = set(seq)

    dic = {num: seq.count(num) for num in seqSet}

    return sorted(dic, key=lambda x: dic[x])[-1]

# FAQ second
def subList(seq):
	m = ref = min(seq)
	res = []
	tmp = []

	for v in seq:
		if v >= m:
			m = v
			tmp.append(v)
		else:
			m = ref
			res.append(tmp)
			tmp = []
			tmp.append(v)
	else:
		# the last sub list
		res.append(tmp)

	return res

# FAQ third
def reverseSentence(sentence):
    # split by space
    seq = sentence.split()
    # reverse list element
    seq.reverse()
    # join list element with space
    return ' '.join(seq)

def _perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in _perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

# FAQ four
def perms(str):
    seq = []
    for e in _perms(str):
        seq.append(e)
    return seq

# FAQ five
def isEqual(str1, str2):
    seq = perms(str1)

    if str1 in seq and str2 in seq:
        return True

    return False 
    
if __name__ == '__main__':
    assert 'stai? come Ciao,' == reverseSentence('Ciao, come stai?')

    assert 1 == findMaxTimes([1,2,3,1,1,2,2,3,3,1,1,2])

    assert [[1, 2, 3], [1, 4, 6], [0, 3]] == subList([1, 2, 3, 1, 4, 6, 0, 3])

    assert ['ab', 'ba'] == perms('ab')

    assert isEqual('ciao', 'aioc')
