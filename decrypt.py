from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABc4hJNU2TGZilZe4R_mjrxR9Bf3FAv59SJwHNvk64bRR1oB50x5Z44bi9_5Jfi38dc623Vi-zdFHI5umtylmAXg6_Rg_NEITKgiqthpej7HnQ39OwBIN5k-q02f47Euk-GN2Yui3MnQWSnHH-1aV5_tpXonqtZxSmc7lnqV1iifBti5nc='

def main():
    f = Fernet(key)
    print(f.decrypt(message))

if __name__ == "__main__":
    main()

