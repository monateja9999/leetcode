def count_palindromes_after_removal(s):
    n = len(s)
    base = 131
    mod = 10**9 + 7

    # Precompute prefix hash and suffix hash
    prefix_hash = [0] * (n + 1)
    suffix_hash = [0] * (n + 2)
    power = [1] * (n + 1)

    for i in range(1, n + 1):
        prefix_hash[i] = (prefix_hash[i-1] * base + ord(s[i-1])) % mod
        power[i] = (power[i-1] * base) % mod

    for i in range(n, 0, -1):
        suffix_hash[i] = (suffix_hash[i+1] * base + ord(s[i-1])) % mod

    def get_prefix_hash(l, r):
        # hash of s[l:r], 1-based indices
        length = r - l + 1
        return (prefix_hash[r] - prefix_hash[l-1] * power[length]) % mod

    def get_suffix_hash(l, r):
        # hash of reversed s[l:r], 1-based indices
        length = r - l + 1
        return (suffix_hash[l] - suffix_hash[r+1] * power[length]) % mod

    count = 0
    for i in range(1, n + 1):
        # Check if s without s[i-1] is palindrome
        # That means prefix s[1..i-1] + suffix s[i+1..n]
        # We check if this combined string is palindrome:
        # prefix part hash == suffix part hash

        # Length of combined string
        length = n - 1

        # Hash of combined string:
        # It's like prefix s[1..i-1] followed by s[i+1..n]

        # Compute hash of combined string forward
        prefix_len = i - 1
        suffix_len = n - i

        # combined hash forward:
        combined_forward = (get_prefix_hash(1, prefix_len) * power[suffix_len] + get_prefix_hash(i+1, n)) % mod

        # combined hash backward (reversed):
        # reversed combined string is suffix reversed + prefix reversed
        combined_backward = (get_suffix_hash(i+1, n) * power[prefix_len] + get_suffix_hash(1, prefix_len)) % mod

        if combined_forward == combined_backward:
            count += 1

    return count

# Driver code with given test cases
test_cases = ["zzz", "aba", "oppo"]
results = [count_palindromes_after_removal(tc) for tc in test_cases]
print(results)  # Expected output: [3, 1, 2]
