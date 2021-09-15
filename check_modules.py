# coding=utf-8
#!/usr/bin/env python3

import sys

def check_modules():
    try:
        import requests
    except:
        print("[-] 'requests' moduleka nadozrayawa!")
        print("[*] Bnwsa 'pip install requests [socks]' bo away install bkai")
        sys.exit(0)

    try:
        import colorama
    except Exception as e:
        print("[-] 'colorama' package install nakrawa!")
        print("[*] Bnwsa 'pip install colorama' bo away install bkai!")
        print(e)
        sys.exit(0)

    try:
        import asyncio
    except:
        print("[-] 'asyncio' package install nakrawa!")
        print("[*] Bnwsa 'pip install asyncio' bo away install bkai!")
        sys.exit(0)

    try:
        import proxybroker
    except:
        print("[-] 'proxybroker' package install nakrawa!")
        print("[*] Bnwsa 'pip install proxybroker' bo away install bkai!")
        sys.exit(0)

    try:
        import warnings
    except:
        print("[-] 'warnings' package install nakrawa!")
        print("[*] Bnwsa 'pip install warnings' bo away install bkai")
        sys.exit(0)

    import warnings
    warnings.filterwarnings("ignore")

    from colorama import init
    init()
