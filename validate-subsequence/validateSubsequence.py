# `O(n) time` because in the worst case we'll have to traverse the whole array
# once
# `O(1) space` because we're not storing any additional data which depends on 
# the input arrays; we're just storing two pointers which is constant space
# no matter the lengths of the two arrays
def isValidSubsequence_v1(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        # looking for a match
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


# `O(n) time` because in the worst case we'll have to traverse the whole array
# once
# `O(1) space` because we're not storing any additional data which depends on 
# the input arrays; we're just storing one pointer which is constant space
# no matter the lengths of the two arrays
def isValidSubsequence_v2(array, sequence):
    seqIdx = 0
    for item in array:
        # check if we've traversed the whole sequence array
        if seqIdx == len(sequence):
            # the fact that we've traversed the whole `sequence` array means
            # that the `sequence` is a subsequence of the `array`. We may now
            # break the for loop because the subsequence have been found
            return True
        # looking for a match
        if item == sequence[seqIdx]:
            seqIdx += 1
    # there's a possibility that we have reached the last item in the
    # `sequence` during the last iteration of the for loop so we didn't
    # really have a chance to break out of the sequence during the iteration
    # and thus, we need to check now
    return seqIdx == len(sequence)


array = [5, 1, 22, 25, 6,-1, 8, 10]
sequence = [1, 6, -1, 10]

print(isValidSubsequence_v1(array, sequence))