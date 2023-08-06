from .LonginusP import *
from Cryptodome.Cipher import AES #line:32
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP
import subprocess,threading,sys,os
from socket import *
from getpass import *
from datetime import datetime
from asyncio import *
import PyQt5
from hashlib import blake2b
from argon2 import PasswordHasher
import msvcrt,re,secrets,secrets,base64,requests

__all__=['Server']

class Server:
    L= Longinus()
    Server_DB:dict=dict()
    Login_list:list=list()
    address=list()
    def __init__(self,set_addr:str,set_port:int):
        self.s=socket()
        self.s.bind(("0.0.0.0",9997))
        self.s.listen(0)
        th=threading .Thread (target =self.send_Token() ).start ()

    def Index():
        pass

    def send_Token(self):
        while True:
            print('waiting for response from client...')
            self.c,self.addr=self.s.accept()
            temp=Longinus().Token_generator(set_data=self.addr);send_Token=temp[0];self.TokenDB=temp[1]
            self.c.send(send_Token)
            print('Token transfer to client successful!')
            th2=threading .Thread (target =self.recv() ).start ()

    def recv(self):
        print("waiting for response from client...")
        while True:
            self.recv_data=self.c.recv(32)
            if self.recv_data in self.TokenDB:
                print('got the correct token : ',self.recv_data)
                break
            else:
                print('Invalid token received! : ',self.recv_data)
                break

    def SignUp(self,UserID:str,User_pwrd:bytes):
        self.UserID=UserID
        self.Userpwrd=User_pwrd
        if (" " not in self.UserID and "\r\n" not in self.UserID and "\n" not in self.UserID and "\t" not in self.UserID and re.search('[`~!@#$%^&*(),<.>/?]+', self.UserID) is None):
            if self.user_checker(UserID)==False:
                if len( self.Userpwrd.decode()) > 8 and re.search('[0-9]+', self.Userpwrd.decode()) is not None and re.search('[a-zA-Z]+', self.Userpwrd.decode()) is not None and re.search('[`~!@#$%^&*(),<.>/?]+', self.Userpwrd.decode()) is not None and " " not in self.Userpwrd.decode() :
                    self.hash.update(base64.b64encode(bytes(a ^ b for a, b in zip( self.Token,self.Userpwrd))))
                    self.Userpwrd=PasswordHasher().hash(self.hash.digest())
                    self.login_data={self.UserID:self.Userpwrd}
                    return self.login_data
                else:
                    print(User_pwrd.decode())
                    raise  Exception("Your password is too short or too easy. Password must be at least 8 characters and contain numbers, English characters and symbols. Also cannot contain whitespace characters.")
            else:
                raise  Exception("A user with the same name already exists. Please change the name.")
        else:
            raise  Exception("Name cannot contain spaces or special characters")

    def ReSign(self,Token:bytes):
        pass
#############################################################################################################################################################################################################################
    def Login(self,UserName:str,User_pwrd:bytes):
        self.hash = blake2b(digest_size=32)
        self.UserName=UserName
        self.Userpwrd=User_pwrd
        if (" " not in self.UserName and "\r\n" not in self.UserName and "\n" not in self.UserName and "\t" not in self.UserName and re.search('[`~!@#$%^&*(),<.>/?]+', self.UserName) is None):
            if len( self.Userpwrd.decode()) > 8 and re.search('[0-9]+', self.Userpwrd.decode()) is not None and re.search('[a-zA-Z]+', self.Userpwrd.decode()) is not None and re.search('[`~!@#$%^&*(),<.>/?]+', self.Userpwrd.decode()) is not None and " " not in self.Userpwrd.decode() :
                self.hash.update(base64.b64encode(bytes(a ^ b for a, b in zip( self.Userpwrd, self.Token))))
                self.Userpwrd=PasswordHasher().hash(self.hash.digest())
                self.Server_DB.setdefault(self.Token,{self.UserName:self.Userpwrd})
                return {self.Token:{self.UserName:self.Userpwrd}}
            else:
                print(User_pwrd.decode())
                raise  Exception("Your password is too short or too easy. Password must be at least 8 characters and contain numbers, English characters and symbols. Also cannot contain whitespace characters.")
        else:
            raise  Exception("Name cannot contain spaces or special characters")
#############################################################################################################################################################################################################################
    def Logout():
        pass
    def Rename():
        pass
    def Repwrd():
        pass
    def verify():
        pass

    def Encryption_Token(self,Token:bytes=L.Token_generator(),set_file:str='public_key.pem'):
        self.Token=Token
        self.file=set_file
        print(self.file)
        if (self.Token==list and type(Token).__name__=="bytes" and [self.keys for self.keys in self.ClientDB.keys() if self.keys in self.Token]):
            self.h = open(self.file, 'rb')  
            self.public_key = RSA.import_key(self.h.read())
            self.cipher_rsa = PKCS1_OAEP.new(self.public_key)
            self.h.close() 
            for self.t in self.Token:
                self.Token_RSA = self.cipher_rsa.encrypt(self.t)
                self.iv_RSA = self.cipher_rsa.encrypt(self.L.Token_secrets_token[self.t])
                self.ClientDB[self.Token_RSA] = self.ClientDB.pop(self.t)
                self.Token_RSA=list()
                self.Token_RSA.append(self.Token_RSA)
            return self.Token_RSA,self.iv_RSA
        elif self.file!=str:
            if Token in self.ClientDB.keys():
                try:
                    self.h = open(self.file, 'rb')  
                    self.public_key = RSA.import_key(self.h.read())
                    self.cipher_rsa = PKCS1_OAEP.new(self.public_key)
                    self.h.close() 
                    self.Token_RSA = self.cipher_rsa.encrypt(self.Token)
                    self.iv_RSA = self.cipher_rsa.encrypt(self.L.Token_secrets_token[self.Token])
                    self.ClientDB[self.Token_RSA] = self.ClientDB.pop(self.Token)
                    return self.Token_RSA,self.iv_RSA
                except FileNotFoundError:
                    raise Exception("The path to the specified key file could not be found!")
            else:
                raise  Exception("The token you entered is not stored in the database! Tokens to be encrypted must be in the database")
        else:
            raise  Exception("Could not find information about that token in the database data!")

    def Encryption_userdata(self,Token:bytes=L.Token_generator()):
        self.keydata = Token
        cbytes = lambda x: str.encode(x) if type(x) == str else x
        if self.keydata in self.ClientDB.keys():
            self.data=(str(self.ClientDB[self.keydata])).encode()
            self.iv=self.L.Token_secrets_token[self.keydata]
            padding = 16-len(self.data)%16
            padding = cbytes(chr(padding)*padding)
            self.cipher = AES.new(self.keydata, AES.MODE_CBC, self.iv)
            self.output= self.cipher.encrypt(cbytes(self.data+padding))
            self.ClientDB[self.keydata]=self.output
            return self.output
        else:
            raise  Exception("Could not find information about that token in the database data!")

    def Decryption_Token(self,Token:bytes,IV_RSA:bytes,Keyfile:str):
        self.Token=Token
        self.iv_RSA=IV_RSA
        self.file=Keyfile
        if (self.Token==list and type(Token).__name__=="bytes" and [self.keys for self.keys in self.Server_DB.keys() if self.keys in self.Token]):
            try:
                self.h = open(self.file, 'rb')  
                self.private_key = RSA.import_key(self.h.read())
                self.cipher_rsa = PKCS1_OAEP.new(self.private_key)
                self.h.close() 
                for self.t in self.Token:
                    self.Token_decrypt = self.cipher_rsa.decrypt(self.t)
                    self.iv=self.cipher_rsa.decrypt(self.iv_RSA)
                    self.Server_DB[self.Token_decrypt] = self.Server_DB.pop(self.t)
                    Server.L.Token_secrets_token.setdefault(self.Token_decrypt,self.iv)
                    self.Token_decrypt=list()
                    self.Token_decrypt.append(self.Token_decrypt)
                return self.Token_decrypt,self.iv
            except FileNotFoundError:
                raise Exception("The path to the specified key file could not be found!")
        else:
            raise  Exception("Could not find information about that token in the database data!")
    def Decryption_userdata(self,Token:bytes):
        self.keydata = Token
        if self.keydata in self.Server_DB.keys():
            self.data=(str(self.Server_DB[self.keydata])).encode()
            self.iv=self.L.Token_secrets_token[self.keydata]
            self.cipher = AES.new(self.keydata, AES.MODE_CBC, self.iv)
            self.output= self.cipher.dencrypt(self.data)
            self.Server_DB[self.keydata]=self.output
            return self.output
        else:
            raise  Exception("Could not find information about that token in the database data!")