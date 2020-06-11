# Python Vigenere Cipher

Python3 function to encrypt/decrypt a message with a key.

## How to Run

Run program in Python3:

```
$ python3 vigCipher.py
```

or import into another Python program:

```
import VigCipher
```

Call command as such:

```
VigCipher(inputString, inputKey, eOrD)
```

*inputString*: message that you wish to encrypt or encryptDecrypt
*inputKey*: key to encrypt or decrypt your message
*eOrD*: indicate if you wish to encrypt or decrypt the message, using either *e* or *d*. Defaults to *e* if invalid response.

## Example
```
VigCipher("This is my secret message.","panda","e")
```
