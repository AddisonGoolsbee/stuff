'''
1.
list of html tags
2.

'''

[("addison", "12.23.42.1"), ("koray", "1.1.1.1"), ("addison12", "12.23.42.1"), ("addison1s", "1.1.1.1")]

# dictionary of ips
# ip -> (trie of prefixes, name)
# list of default_names
# prefix tree for names?
# if ip in ips, check for prefix. Otherwise, add new ip and prefix with full name
# check for prefix: check if first letter in dictionary. If so, 2 pointers through strings, if contains prefix, toss. If earlier prefix, update prefix. If no prefix, add new 2-list

'''
ip -> [name]
sort names
valid = []
d = {}
aba
abababa
abababfa
asbabaa
'''

def doit(users):
    ips = {}
    for user in users:
        username, ip = user
        ips.setdefault(ip, [])
        ips[ip].append(username)

    unique_users = []
    for ip_usernames in ips.values():
        usernames = [ip_usernames]
        for username in ip_usernames:
            for testname in ip_usernames:
                if username[:-1].startswith(testname):
                    break

    
    return unique_users
        
        

test_input = [("addison", "12.23.42.1"), ("koray", "1.1.1.1"), ("addison12", "12.23.42.1"), ("addison1s", "1.1.1.1"), ("aba", "1.1.1.1"), ("ababababa", "1.1.1.1"), ("ababasef", "1.1.1.1"), ("abdsa", "1.1.1.1")]
print(doit(test_input))