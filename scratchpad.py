# import itertools
#
#
# for i in itertools.zip_longest(s, query, fillvalue='-'):
#     print(i)
# print()
# for i in zip(iter(s, query)):
#     print(i)

# for s[start: start+step] in s:
#     print(s[start: start+step])
#     start =+ 1

# def longest_sorted_string():
#     pass
#
#     import itertools
#     from pprint import pprint
#     s = 'azcbobobegghakl'
#     for combo_length in range(len(s), 0, -1):
#         combos = [combo for combo in itertools.permutations(s,combo_length)]
#         yield combos


def count_vowels():
    s = 'azcbobobeggaeohwwadfippowwqeeakl'
    v = ('a', 'e', 'i', 'o', 'u')
    t = 0
    for c in s:
        if c in v:
            t += 1
    print("Number of vowels:", t)


def count_occurences():
    s = 'azcbobobegghakl'
    query = 'bob'
    query_count = 0
    step = len(query)
    
    for start in range(0, len(s)):
        parse_elem =  [fragment for fragment in (s[start: start+step],) if fragment == query]
        query_count += 1 if parse_elem else 0
    print("Number of times {} occurs is: {}".format(query, query_count))
    
    
# def longest_sorted_string():
#     s = 'azcbobobegghakl'
#     sl = [s]
#
#     for fragment in s[0:]:
#         print(fragment)
#
# longest_sorted_string()


# from itertools import permutations as pm
# from pprint import pprint

# s = 'azcbobobegghakl'
# for pm_ in pm(s):
#     pprint(pm_)

def longest_sorted_older():
    s = 'azcbobobegghakl'
    slist = list(s)
    start = 0
    stop = len(s)
    done = False
    longest = 0
    second_longest = 0
    diff_start_find_all = []
    while not done:
        found = False
        print('   slist:', slist)
        while not found:
            fragment = slist[start: stop]
            sorted_frag = sorted(fragment)
            print('fragment:', fragment, '\n  sorted:', sorted_frag)
            found = fragment == sorted_frag
            stop -= 1
            
        longest = longest if len(fragment) <= longest else len(fragment)
        same_start_find = (fragment, sorted_frag, len(fragment))
        diff_start_find_all.append(same_start_find)
        start += 1
        stop = len(s)
        # del fragment, sorted_frag
    # print(fragment)
        # loop = input("loop(y/n)? ")
        # loop = True if loop.lower() == '' or 'y' else False

def longest_sorted_many_wrong():
    from pprint import pprint
    tests = (('azcbobobegghakl', 'beggh'),
             ('aeyxsepcixrcpymtyx', 'aey'),
             ('zyxwvutsrqponmlkjihgfedcba', 'z'),
             ('hslxcbjiogqhucfcwh', 'hs'),
             ('dbawzcoo', 'awz'),
             ('bnwenhqeeoect', 'bnw'),
             ('nwznnhlvqnvbbxpzlzjsck', 'nwz')
             )
    
    all_sorted = []
    for test_ in tests:
        max_length = 0
        s = test_[0]
        slist = list(s)
        common_start_sorted = [0, 0, 0]
        for start in range(0, len(slist) -1):
            for stop in range(len(slist), 0, -1):
                fragment = slist[start: stop]
                if fragment == sorted(fragment) and len(fragment) > max_length:
                    max_length = len(fragment)
                    if common_start_sorted[2] < len(fragment):
                        common_start_sorted = (s, ''.join(fragment), len(fragment))
                    break
        res = 'Pass' if common_start_sorted[1] == test_[1] else (common_start_sorted[1], test_[1])
        print(res)
        all_sorted.append(common_start_sorted)
        

# longest_sorted_many_wrong()

def longest_sorted(s):
    max_length = 0
    slist = list(s)
    common_start_sorted = [0, 0, 0]
    for start in range(0, len(slist) - 1):
        for stop in range(len(slist), 0, -1):
            fragment = slist[start: stop]
            if fragment == sorted(fragment) and len(fragment) > max_length:
                max_length = len(fragment)
                if common_start_sorted[2] < len(fragment):
                    common_start_sorted = (s, ''.join(fragment), len(fragment))
                break
    res = 'Pass' if common_start_sorted[1] == test_[1] else (common_start_sorted[1], test_[1])
    return common_start_sorted[1]
    
tests = (('azcbobobegghakl', 'beggh'),
             ('aeyxsepcixrcpymtyx', 'aey'),
             ('zyxwvutsrqponmlkjihgfedcba', 'z'),
             ('hslxcbjiogqhucfcwh', 'hs'),
             ('dbawzcoo', 'awz'),
             ('bnwenhqeeoect', 'bnw'),
             ('nwznnhlvqnvbbxpzlzjsck', 'nwz')
             )
for test_ in tests:
    print("Longest substring in alphabetical order is: ", longest_sorted(test_[0]))
