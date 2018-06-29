import numpy as np
import NetworkFileManager as netMang
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from functools import lru_cache

# uses open addressing collison resolution
hashcode = 0
'''
Uses System Cache Least Recently Used Removal = lru_cache
'''


@lru_cache(maxsize=64)
class HashTable(object):
    _array = np.array([None])

    def __init__(self):
        self.array = np.array([None] * 17)

    def insert(self, domain_name, ip_address):
        hashtable = netMang.get_file(netMang.choose_dns(domain_name))
        hash_number = hash_func(domain_name, hashtable)
        if hashtable.size < 2:
            return "Domain does not exists "
        # inserted = False
        if hashtable[hash_number] is None:
            hashtable[hash_number] = (domain_name, ip_address)
            netMang.write_file(domain_name, hashtable)
            return "{} insertion successful".format(domain_name)
        elif hashtable[hash_number].__contains__('Deleted'):
            hashtable[hash_number] = (domain_name, ip_address)
            netMang.write_file(domain_name, hashtable)
            return "{} insertion successful".format(domain_name)
        else:
            check = eval(hashtable[hash_number])
            check = str(''.join(check[0]))
            if domain_name != check:
                i = 1
                while hashtable[hash_number] is not None and not hashtable[hash_number].__contains__('Deleted'):
                    hash_number = quadratic_probing(i, domain_name, hashtable)
                    i += 1
                    if i == hashtable.size:
                        hashtable = self.rehash_table(domain_name, hashtable)
                        self.insert(domain_name, ip_address)
                        break

                else:
                    hashtable[hash_number] = (domain_name, ip_address)
                    netMang.write_file(domain_name, hashtable)
                    return "{} insertion successful".format(domain_name)
            else:
                return domain_name + " already exists"
        array = hashtable

    def search(self, element):
        search_hashtable = netMang.get_file(netMang.choose_dns(element))
        hash_number = hash_func(element, search_hashtable)
        if search_hashtable[hash_number] is None:
            popuptext("{} is not on DNS Server".format(element))
        else:
            while search_hashtable[hash_number] is not None:
                tuple = eval(search_hashtable[hash_number])
                check = str(''.join(tuple[0]))
                if check == element:
                    popuptext("NAME: {}\nADDRESS: {}\n".format(tuple[0], tuple[1]))
                    break
                else:
                    i = 1
                    check = str(''.join(tuple[0]))
                    while check != element:
                        hash_number = quadratic_probing(i, element, search_hashtable)
                        i += 1
                        if search_hashtable[hash_number] is None:
                            pass
                            break
                        tuple = eval(search_hashtable[hash_number])
                        check = str(''.join(tuple[0]))
                        if i == search_hashtable.size:
                            break
                    else:
                        pass

            else:
                popuptext("{} is not on DNS Server".format(element))

    def delete_address(self, element):
        delete_from_hashtable = netMang.get_file(netMang.choose_dns(element))
        hash_number = hash_func(element, delete_from_hashtable)
        if delete_from_hashtable[hash_number] is None:
            popuptext("{} is not on DNS Server".format(element))
        else:
            while delete_from_hashtable[hash_number] is not None:
                tuple = eval(delete_from_hashtable[hash_number])
                check = str(''.join(tuple[0]))
                if check == element:
                    delete_from_hashtable[hash_number] = ("Deleted", "None")
                    netMang.write_file(element, delete_from_hashtable)
                    popuptext("{} Deleted from DNS".format(check))
                    break
                else:
                    i = 1
                    check = str(''.join(tuple[0]))
                    while check != element:
                        hash_number = quadratic_probing(i, element, delete_from_hashtable)
                        i += 1
                        if delete_from_hashtable[hash_number] is None:
                            pass
                            break
                        tuple = eval(delete_from_hashtable[hash_number])
                        check = str(''.join(tuple[0]))
                        if i == delete_from_hashtable.size:
                            break
                    else:
                        delete_from_hashtable[hash_number] = ("Deleted", "None")
                        netMang.write_file(element, delete_from_hashtable)
                        popuptext("{} Deleted from DNS".format(check))

            else:
                popuptext("{} is not on DNS Server or Was Deleted".format(element))

    def rehash_table(self, domain_name, hashtable):
        temp = hashtable
        size_of_hashtable = next_prime(temp.size * 2)
        domain = netMang.choose_dns(domain_name)
        arr = np.array([None] * size_of_hashtable)
        netMang.write_file(domain_name, arr)
        hashtable = netMang.get_file(netMang.choose_dns(domain_name))
        for i in range(temp.size):
            if temp[i] is None:
                continue
            else:
                try:
                    element = eval(temp[i])
                    self.insert(element[0], element[1])
                except EOFError:
                    continue

        return hashtable


def quadratic_probing(iteration, element, hashtable):
    hash_number = hash_func(element, hashtable)
    hash_number = (hash_number + iteration ** 2) % hashtable.size
    return hash_number


def next_prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            num += 1
            i = 2
        elif i == (num // 2) + 1:
            break
        else:
            i += 1
            print(num, "/", i)

    return num


def hash_func(element, array):
    element = ascii_converter(element)
    hash_number = element % array.size
    return hash_number


def ascii_converter(entry):
    entry_result = int(''.join(str(ord(char)) for char in entry))
    return entry_result


def popuptext(text_input):
    popup = Popup(title='',
                  content=Label(text=text_input),
                  size_hint=(None, None), size=(400, 200))
    popup.open()
