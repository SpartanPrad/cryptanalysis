# A one-time pad is a Shannon cipher f = (E,D), where the keys, messages, and
# ciphertexts are bit strings of the same length; that is, f is defined over (K,M, C), where
#       K := M:= C := {0, 1}L for some fixed length L

# E(k,m) := k xor m
# D(k,m) := k xor c

k = 15
m = 14

c = m^k

# D(k, E(k, m) ) = D(k, k xor m) = k xor (k xor m) = (k xor k) xor m = 0L xor m = m.

assert m == (c^k)
