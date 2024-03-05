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
        Md2, Md4, Md5, Sha1, Sha224, Sha256, Sha384, Sha512, Ripemd128, Ripemd160, Ripemd256, Ripemd320, Whirlpool, Snefru, Snefru256, Gost, Adler32, Crc32, Crc32b, Crc32b php, Fnv132, Fnv164, Fnv1a32, Fnv1a52, Fnv1a64, Fnv1a128, Fnv1a512, Fnv1a1024, Joaat php, Joaat, Murmur3, Djb2, Sdbm, Loselose, Pearson, Farm hash fingerprint32, Farm hash fingerprint64, Haval128,3, Haval160,3, Haval192,3, Haval224,3, Haval256,3, Haval128,4, Haval160,4, Haval192,4, Haval224,4, Haval256,4, Haval128,5, Haval160,5, Haval192,5, Haval224,5, Haval256,5, Tiger128, Tiger160, Tiger192, Tiger160,3 php, Tiger128,4, Tiger160,4, Tiger192,4, Base64, Tiger128,3, Tiger160,3, Tiger192,3, Md5x2, Md5x3, Md5x4, Md5x5
        """
        response = requests.get(f'https://md5hashing.net/hash/{hashtype}/{hashvalue}').text
        if response.find('successfully reversed into the string') > 0:
            plain = re.findall(r'<a class="String" href=".+">(.*?)<\/a>', response)[0]
            return plain
        else:
            return False