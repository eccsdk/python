'''
@author: eccsdk
'''
import SM2Python

str_prikey = "92E608FA687C466527931C8A70E3BEB700BD0438A31C5470A4D92DEAD3657408"

str_cipher = "44DFAA4384DA7A10DEC311C5AE5CAA9448B129DEB4E3A809287138FDAB22B30685404F639925A77D994ABB3B11FBE6C7B58A2921C0C023DB47E97CEEFF14AFB7CAC6B826D47D7CBD12B27C5C933E4F9CDA3C72001263A9D6FC38CC5414A74B5AF726030BC82F78FE90BAA9033F772B69ED3B8B1C6C"

plain = SM2Python.SM2Decrypt(str_cipher, str_prikey)

print("plain :" + plain)

input()
