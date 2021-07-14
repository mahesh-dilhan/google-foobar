def answer(x):
    lc_norm = [i for i in range(97, 123)]
    lc_rev = [j for j in range(122, 96, -1)]
    dict_lc = {lc_norm[n]: lc_rev[n] for n in range(len(lc_norm))}

    decrypted_str = []

    for char in x:
        if dict_lc.has_key(ord(char)):
            decrypted_str.append(chr(dict_lc[ord(char)]))
        else:
            decrypted_str.append(char)

# print (''.join(decrypted_str))
    return ''.join(decrypted_str)

answer("wrw blf hvv ozhg mrtsg'h vkrhlwv?");