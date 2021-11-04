# coding:utf-8
# Created:03/24/2020
# author:Radioman-lhq
import json

from M2Crypto import *
from base64 import b64encode, b64decode




def read_key(file_path, type):
    """
    读取RSA密钥
    :param file_path: 文件路径
    :param type: 密钥类型，private：私钥|public：公钥
    :return:
    """
    with open(file_path, "rb") as file_handler:
        rea_key = BIO.MemoryBuffer(file_handler.read())
    if type == "private":
        return RSA.load_key_bio(rea_key)
    else:
        return RSA.load_pub_key_bio(rea_key)


def read_key_from_conf(rsa_key, key_type="private"):
    """
    读取RSA密钥
    :param rsa_key: rsa密钥
    :param key_type: 密钥类型，private：私钥|public：公钥
    :return:
    """
    if key_type == "private":
        rsa_key = "-----BEGIN RSA PRIVATE KEY-----\n{}\n-----END RSA PRIVATE KEY-----".format(rsa_key)
        return RSA.load_key_string(str.encode(rsa_key))
    else:
        rsa_key = "-----BEGIN PUBLIC KEY-----\n{}\n-----END PUBLIC KEY-----".format(rsa_key)
        return RSA.load_pub_key_bio(BIO.MemoryBuffer(str.encode(rsa_key)))


def hash(message, algorithm="md5"):
    """
    计算散列值
    :param message: 消息
    :param algorithm: 散列算法
    :return:
    """
    hash = EVP.MessageDigest(algorithm)
    hash.update(message.encode(encoding='utf-8'))
    return hash.digest()


def rsa_sign(message, private_key, algorithm="md5"):
    """
    RSA签名
    :param message: 消息
    :param private_key: 私钥
    :param algorithm: 散列算法
    :return:
    """
    digest = hash(message, algorithm)
    return b64encode(private_key.sign(digest, algorithm)).decode(encoding='utf-8')


def rsa_verify(message, sign, public_key, algorithm="md5"):
    """
    RSA验签
    :param message: 消息
    :param sign: 签名
    :param public_key: 公钥
    :param algorithm: 散列算法
    :return:
    """
    digest = hash(message, algorithm)
    return public_key.verify(digest, b64decode(sign), algorithm)


def rsa_pkcs1_encrypt(plaintext, private_key):
    """
    RSA私钥加密
    :param plaintext: 明文
    :param private_key: 私钥
    :return:
    """
    print("Rsa私钥加密明文: %s." % plaintext)

    # 密钥长度为1024时，最大加密块
    max_encrypt_block = 117
    # 填充方式
    padding = RSA.pkcs1_padding

    # 字节编码
    plainBytes = plaintext.encode(encoding='utf-8')

    # 明文长度
    plaintext_length = len(plainBytes)

    # 不需要分段加密
    if plaintext_length < max_encrypt_block:
        return b64encode(private_key.private_encrypt(plainBytes, padding)).decode(encoding='utf-8')

    # 分段加密
    offset = 0
    ciphers = []
    while plaintext_length - offset > 0:
        if plaintext_length - offset > max_encrypt_block:
            ciphers.append(private_key.private_encrypt(plainBytes[offset:offset + max_encrypt_block], padding))
        else:
            ciphers.append(private_key.private_encrypt(plainBytes[offset:], padding))
        offset += max_encrypt_block
    return b64encode(b"".join(ciphers)).decode(encoding='utf-8')


def rsa_pkcs1_decrypt(cipher_text, public_key):
    """
    RSA公钥解密
    :param cipher_text:
    :param public_key:
    :return:
    """
    encrypt_result = b64decode(cipher_text)
    # 密钥长度为1024时，最大解密块
    max_decrypt_block = 128
    # 加密结果长度
    encrypt_result_length = len(encrypt_result)
    # 填充方式
    padding = RSA.pkcs1_padding

    # 不需要分段解密
    if encrypt_result_length < max_decrypt_block:
        plaintext = public_key.public_decrypt(encrypt_result, padding)

        print("Rsa公钥解密明文: %s." % plaintext)
        return plaintext

    # 分段解密
    offset = 0
    plains = []
    while encrypt_result_length - offset > 0:
        if encrypt_result_length - offset > max_decrypt_block:
            plains.append(public_key.public_decrypt(encrypt_result[offset:offset + max_decrypt_block], padding))
        else:
            plains.append(public_key.public_decrypt(encrypt_result[offset:], padding))
        offset += max_decrypt_block
    plaintext = b"".join(plains).decode(encoding='utf-8')

    print("Rsa公钥解密明文: %s." % plaintext)

    return plaintext


if __name__ == '__main__':
    # RSA私钥加密
    data = {
      "data": {
        "parkingCode": "1001",
        "totalBerthNum": 150,
        "openBerthNum": 130,
        "freeBerthNum": 10,
        "uploadTime": "2015-09-01 09:10:11"
      }
    }
    private_key = "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKBbUNr/d/GvjfwQ8jv7Jd4SEOHFKm6XFZO6uXUR5LLqg9X8s1iqoeIRVy/tqZ6C1XfCTDdt/tSmGXJB2vba2l7DL+j4B9d8edFfVLQgBlm8VZLG52o7IRtV8SPG32ElWaAZ9UkNj9bJecnWGfK1FPDF2wZsWwIRDq4qH0pE1boRAgMBAAECgYEAhmOBI8guMXK7P6DEIdidJ7tkQpIGuaANCT3X53EThY5c5p1dgNWfzeJSe2xmVt23ISLI1Ttt8bEyajse0vsfPikBUH8kGYnzWnsmz6ZPNxXZf5n25dcbi7Bu+fh3ISvZWDRbodcHLvdJx0Vuk5kiVzun6lgld3+yTKof6OyH8AECQQD4nJcFZAb0h+YhG+68wNWx1Fk3rDrseuUu7ax+WnSWONPCpMt5oKoNrJOI4rEL5pMJE9c1KuPaIGyqtRXWpQJBAkEApR9KtjsR2ZBj829ULTDVSVBCUxyI+anonMGatZmOJqK/Cj25d+0iHRnTqQKQW7mifKpexqdsGoJJfnYapNAj0QJAYW1kVa18eEnlqqX6qifb1uPDzuiE8vW6aOilh6LFO7WrbwUL5G9NFSzDaIqGHYbPqmgHF4PmZS39x+xNUZ+6wQJABWoaRBF5y12NuXzMENNKGyZTlnAYGb+1jfZXQV8wpxmtFAPkIgeXl8ayBxe7bhaPOnFHvFHfHJtrF4d95iuhEQJAKDQTnXd64Qoec2dTpF2ee1yAiWOtG3RYV5F4az3U2SGkgXeA68uqoO24i7cWyh4VloNcLIoXV/nvAjtL7Id/hA=="
    private_key = read_key_from_conf(private_key, "private")
    ciphertext = rsa_pkcs1_encrypt(json.dumps(data), private_key)
    print(ciphertext)
#
    # RSA签名
    sige_result = rsa_sign(ciphertext, private_key)
    print(sige_result)
#
#     # RSA公钥解密
#     public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCzfr8kgjXYXuQP9EG4ILrDUhf84SXEQX+ZZ7v/eAjLP8HQ/2ixtsLnN4/38mMRorIXNUazNdRnZykccfK8D2hIvMLFRPHv8AStA+OKG1fC6N1NMoQ15mrWDml/g0uDCUMRCxw/GIbDVBaK77oweF8pxiT0rxpvl2bemxFmJGrUCwIDAQAB"
#     public_key = read_key_from_conf(public_key, "public")
#     plaintext = rsa_pkcs1_decrypt(ciphertext, public_key)
#     print(plaintext)
#
#     # RSA验签
#     assert rsa_verify(ciphertext, sige_result, public_key)
