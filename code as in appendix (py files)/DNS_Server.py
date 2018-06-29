import NetworkFileManager as netMang
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import NetworkHashTable as netHash
import numpy as np
import os
import re
import shutil


class Server(object):
    @staticmethod
    def create_domain(domain):
        filename = domain
        filename_list = re.sub('[^\w]', " ", filename).split()
        dns_file = "./DNS_files"
        for i in range(len(filename_list) - 1, -1, -1):
            word = "/" + filename_list[i]
            dns_file += word
        check_dir = dns_file
        dns_file = dns_file + "/HashTable.txt"
        try:
            if not os.path.exists(dns_file):
                directory = os.path.dirname(dns_file)
                os.makedirs(directory)
        except FileExistsError:
            pass
        dirlist = os.listdir(check_dir)
        if filename is ".txt":
            return "Please Enter Domain Name"
        elif "HashTable.txt" in dirlist:
            return "DNS file already exists"
        else:
            file = open(dns_file, 'w')
            default_length = 17
            arr = np.array([None] * default_length)
            for x in range(arr.size):
                file.write("{}\n".format(arr[x]))
            file.close()
            return "DNS_Server Created"

    @staticmethod
    def delete_domain(domain_name):
        filename_list = re.sub('[^\w]', " ", domain_name).split()
        dns_file = "./DNS_files"
        for i in range(len(filename_list) - 1, -1, -1):
            word = "/" + filename_list[i]
            dns_file += word
        try:
            directory = dns_file
            dirlist = os.listdir(dns_file)
            dns_file += "/HashTable.txt"
        except FileNotFoundError:
            return "DNS not Found"
        if "HashTable.txt" in dirlist:
            shutil.rmtree(directory)
            netHash.popuptext("Domain Deleted")
        else:
            return "Not Found"

    @staticmethod
    def print_domains(self):
        root_dir = 'DNS_files'
        count = 0
        str_dom = ''
        text = ''
        for dirName, subdirList, fileList in os.walk(root_dir):
            if dirName == 'DNS_files':
                continue
            filename_list = re.sub('[^\w]', " ", dirName).split()
            for i in range(len(filename_list) - 1, 0, -1):
                str_dom += filename_list[i] + "."
            text += '  {}. {} |'.format(count + 1, str_dom)
            count += 1
            str_dom = ''
            if count % 4 == 0:
                str_dom += "\n"
        popup = Popup(title='Domains',
                      content=Label(text=text),
                      size_hint=(None, None), size=(1000, 700))
        popup.open()

    @staticmethod
    def print_directory(domain):
        domain = "dammy." + domain
        text = 'Domain Name : IP Address \n-----------------------------------------------\n'
        hashtable = netMang.get_file(netMang.choose_dns(domain))
        count = 0
        for entry in range(len(hashtable)):
            if hashtable[entry] is None:
                continue
            elif hashtable[entry].__contains__('Deleted'):
                continue
            else:
                gen_tuple = eval(hashtable[entry])
                text += "     |     " + str(count + 1) + ". " + gen_tuple[0] + " : " + gen_tuple[1]
                count += 1
                if count % 2 == 0:
                    text += "\n--------------------------------------------------------------" \
                            "-----------------------------------------------------------------" \
                            "-------------------------------------------------------------------------\n"
        popup = Popup(title='Domain Names',
                      content=Label(text=text),
                      size_hint=(None, None), size=(1000, 700))
        popup.open()
