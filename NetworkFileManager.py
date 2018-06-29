import os
import numpy as np
import re


def write_file(domain, array):
    dns_server = choose_dns(domain)
    filename = dns_server + "/HashTable.txt"
    file = open(filename, 'w')
    listtofile = array
    for item in listtofile:
        file.write("{}\n".format(item))
    file.close()


def get_file(server):
    server = server + "/HashTable.txt"
    arr = np.array([])
    empty = np.array([None])
    try:
        if os.path.exists(server):
            name = server
            file = open(name, 'r')
            content = file.readlines()
            for x in content:
                entry = x.strip('\n')
                if entry == 'None':
                    entry = None
                arr = np.append(arr, entry)
            return arr
        else:
            return empty
    except FileNotFoundError:
        return "Fetch Error"


def choose_dns(name):
    char_arr = []
    count = 0
    ch = ''
    if len(name) < 1:
        return "Invalid name"
    else:
        filename_list = re.sub('[^\w]', " ", name).split()
        dns_file = "./DNS_files"
        for i in range(len(filename_list) - 1, 0, -1):
            word = "/" + filename_list[i]
            dns_file += word
        ch = dns_file
    return ch

