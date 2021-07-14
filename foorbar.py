# def answer(x):
#     lc_norm = [i for i in range(97, 123)]
#     lc_rev = [j for j in range(122, 96, -1)]
#     dict_lc = {lc_norm[n]: lc_rev[n] for n in range(len(lc_norm))}
#
#     decrypted_str = []
#
#     for char in x:
#         if dict_lc.has_key(ord(char)):
#             decrypted_str.append(chr(dict_lc[ord(char)]))
#         else:
#             decrypted_str.append(char)
#
# # print (''.join(decrypted_str))
#     return ''.join(decrypted_str)
#
# answer("wrw blf hvv ozhg mrtsg'h vkrhlwv?");

from fractions import Fraction
def solution(pegs):
    arrLength = len(pegs)
    if ((not pegs) or arrLength == 1):
        return [-1,-1]

    even = True if (arrLength % 2 == 0) else False
    sum = (- pegs[0] + pegs[arrLength - 1]) if even else (- pegs[0] - pegs[arrLength -1])

    if (arrLength > 2):
        for index in xrange(1, arrLength-1):
            sum += 2 * (-1)**(index+1) * pegs[index]

    FirstGearRadius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()

    if FirstGearRadius < 2:
        return [-1,-1]

    currentRadius = FirstGearRadius
    for index in xrange(0, arrLength-2):
        CenterDistance = pegs[index+1] - pegs[index]
        NextRadius = CenterDistance - currentRadius
        if (currentRadius < 1 or NextRadius < 1):
            return [-1,-1]
        else:
            currentRadius = NextRadius

    return [FirstGearRadius.numerator, FirstGearRadius.denominator]

answer({4, 30, 50});