#!/usr/bin/env python
# Skeleton for Security Tools Lab 1 - Simple ciphers
# Student ID:
# StudentName:

import binascii as b
import requests
import json
import hashlib
import argparse

def xorString(s1,s2):
    """ 
        XOR two strings with each other, return result as string
    """
    rval = [ord(a) ^ ord(b) for a,b in zip(s1,s2)]
    return ''.join([chr(r) for r in rval])


def resolvePlainChallenge():
    """
        Solution of plain challenge
    """
    url = "http://{}:{}/".format(IP, PORT)
    headers = {'Content-Type': 'application/json'}

    r = requests.get(url + 'challenges/plain')
    data = r.json()
    print("[DEBUG] Obtained challenge ciphertext: %s with len %d" % (data['challenge'], len(data['challenge'])))

    # TODO: Add a solution here (conversion from hex to ascii will reveal that the result is in a human readable format)
    a = data['challenge'][2:]
    s = bytearray.fromhex(a).decode()

    payload = {'cookie': data['cookie'], 'solution': s}
    print("[DEBUG] Submitted solution is:")
    print(json.dumps(payload, indent=4, separators=(',', ': ')))

    r = requests.post(url + 'solutions/plain', headers=headers, data=json.dumps(payload))
    print("[DEBUG] Obtained response: %s" % r.text)


def resolveCaesarChallenge():
    """
        Solution of caesar challenge
    """
    url = "http://{}:{}/".format(IP, PORT)
    headers = {'Content-Type' : 'application/json'}

    r = requests.get(url + 'challenges/caesar')
    data = r.json()
    print("[DEBUG] Obtained challenge ciphertext: %s with len %d" % (data['challenge'], len(data['challenge'])))

    # TODO: Add a solution here (conversion from hex to ascii will reveal that the result is in a human readable format)
    s=data['challenge'][2:]
    s=b.unhexlify(s)
    solution = s


    payload = { 'cookie' : data['cookie'], 'solution' : solution}
    print("[DEBUG] Submitted solution is:")
    print(json.dumps(payload, indent=4, separators=(',', ': ')))

    r = requests.post(url+'solutions/caesar', headers=headers,data=json.dumps(payload))
    print("[DEBUG] Obtained response: %s" % r.text)

def resolvesubstitutionChallenge():
    """
        Solution of substitution challenge
    """
    url = "http://{}:{}/".format(IP, PORT)
    headers = {'Content-Type' : 'application/json'}

    r = requests.get(url + 'challenges/substitution')
    data = r.json()
    #print ("[DEBUG] Obtained challenge ciphertext: %s with len %d" % (data['challenge'], len(data['challenge'])))

    # TODO: Add a solution here (conversion from hex to ascii will reveal that the result is in a human readable format)
    s=data['challenge'][2:]
    s=b.unhexlify(s)
    solution = s

    payload = { 'cookie' : data['cookie'], 'solution' : solution}
    print("[DEBUG] Submitted solution is:")
    print(json.dumps(payload, indent=4, separators=(',', ': ')))

    r = requests.post(url+'solutions/substitution', headers=headers,data=json.dumps(payload))
    print("[DEBUG] Obtained response: %s" % r.text)

def resolveotpChallenge():
    """
        Solution of otp challenge
    """
    url = "http://{}:{}/".format(IP, PORT)
    headers = {'Content-Type' : 'application/json'}

    r = requests.get(url + 'challenges/otp')
    data = r.json()
    #print ("[DEBUG] Obtained challenge ciphertext: %s with len %d" % (data['challenge'], len(data['challenge'])))

    # TODO: Add a solution here (conversion from hex to ascii will reveal that the result is in a human readable format)
    a = data['challenge'][2:]
    c = b.unhexlify(a)
    solution = c

    payload = { 'cookie' : data['cookie'], 'solution' : solution}
    print("[DEBUG] Submitted solution is:")
    print(json.dumps(payload, indent=4, separators=(',', ': ')))

    r = requests.post(url+'solutions/otp', headers=headers,data=json.dumps(payload))
    print("[DEBUG] Obtained response: %s" % r.text)

def parseArgs():               
    """ 
        Function for arguments parsing
    """
    aparser = argparse.ArgumentParser(description='Script demonstrates breaking of simple ciphers: Caesar, Substitution cipher, and OTP.', formatter_class = argparse.RawTextHelpFormatter) 
    aparser.add_argument('--port', required=True, metavar='PORT', help='Port of challenge/response server.')
    aparser.add_argument('--ip', required=True, metavar='PORT', help='Port of challenge/response server.')
    aparser.add_argument("--mode", required=True, choices = ['p', 'c', 's', 'o'], help="p => demonstrates hexadecimal encoding challenge.\
                         \nc => demonstrates breaking of the Caesar cipher.\
                         \ns => demonstrates breaking of the Substitution cipher.\
                         \no => demonstrates breaking of the OTP cipher.")
    args = aparser.parse_args()
    
    return args


def main():
    args = parseArgs()

    global IP
    IP = args.ip

    global PORT
    PORT = args.port

    if args.mode == "o":
        resolveotpChallenge()
    elif args.mode == "p":
        resolvePlainChallenge()
    elif args.mode == "c":
        resolveCaesarChallenge()
    elif args.mode == "s":
        resolvesubstitutionChallenge()

if __name__ == '__main__':
    main()