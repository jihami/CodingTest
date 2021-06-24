def solution(s):
    return s.lower().count("p") == s.lower().count("y")
s1 = "pPoooyY"
print(solution(s1))
s2 = "Pyy"
print(solution(s2))