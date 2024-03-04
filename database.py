import requests
import re

class Database:

    def md5decrypt(hashvalue, hashtype):
        """
        md4, md5, sha1, sha256, sha384, sha512
        """
        response = requests.get('https://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=hogad85544@themesw.com&code=85d8d439297a8764' % (hashvalue, hashtype)).text
        if len(response) != 0:
            return response
        else:
            return False

    def nitrxgen(hashvalue, hashtype):
        """
        md5
        """
        response = requests.get('https://www.nitrxgen.net/md5db/' + hashvalue).text
        if response:
            return response
        else:
            return False
        
    def my_addr(hashvalue, hashtype):
        """
        md5
        """
        response = requests.post('http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php', {
            'md5': hashvalue
        })
        result = re.findall(r"Hashed string</span>:\s(.+?)</div>", response.text)
        if result:
            return result[0]
        else:
            return False
        
    def gromweb(hashvalue, hashtype):
        """
        md5, sha1
        """
        if hashtype == 'md5': 
            mode = 'md5' 
        else:
            mode = 'hash'
        response = requests.get(f'https://{hashtype}.gromweb.com/?{mode}={hashvalue}').text
        if response.find('successfully reversed into the string') > 0:
            plain = re.findall(r'<a class="String" href=".+">(.*?)<\/a>', response)[0]
            return plain
        else:
            return False
        
    def gromweb(hashvalue, hashtype):
        """
        md5, sha1
        """
        if hashtype == 'md5': 
            mode = 'md5' 
        else:
            mode = 'hash'
        response = requests.get(f'https://md5hashing.net/hash/sha256/{hashvalue}').text
        if response.find('successfully reversed into the string') > 0:
            plain = re.findall(r'<a class="String" href=".+">(.*?)<\/a>', response)[0]
            return plain
        else:
            return False