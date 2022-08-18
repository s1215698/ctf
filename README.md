# ctf
use for ctf
python is for Crypto 
C is for Reverse

#python 61進位字串轉ASCII
bytearray.fromhex(字串).decode()



Kali command list


https://free.drweb.com/download+cureit/gr/?lng=en
Windows2016
redaltertuser
1qaz2wsx#RedAlert2021;

#share folder
mount -t cifs -o uid=1000,gid=1000,username=chingsi,password=P@ssword1234567 //192.168.14.1/ctf_share ~/share

btop--類似工作管理員


#arkime services
/opt/arkime/bin/Configure
systemctl start elasticsearch.service
/opt/arkime/db/db.pl http://localhost:9200 upgrade
/opt/arkime/bin/arkime_add_user.sh admin "Admin User" 1qaz2wsx --admin
sudo systemctl start arkimecapture.service
sudo systemctl start arkimeviewer.service


wget http://es.archive.ubuntu.com/ubuntu/pool/main/libf/libffi/libffi7_3.3-4_amd64.deb




openssl rsa -pubin -in [public key file] -text -modulus -noout   ==>可以求得n e 

openssl rsautl -decrypt -in [cipher file] -inkey [private key file] -out [output file nam]  ==>解密

python RsaCtfTool.py --publickey [public key file] --uncipherfile [cipher file] --attack fermat  ==>n太大 可使用



xortool -c " " -m 200 [enc_file]   (-c 最多的字元去爆破  -m最常key長度)


Kali Strings ==>  讀取檔案16進位==>可輸出成txt檔
strings [檔名] >> [輸出檔案名稱及格式EX:txt]

Kali steghide用法 ==> 檢查檔案中隱藏檔案(需要有password/key才可以解)
steghide extract -sf [檔名]

https://hackmd.io/XbJY7EF5TsG1DO88mvV8Rg
https://hackmd.io/uFesArA-Te2ZH3heJFQZ8Q   ##REMnux VM
https://hackmd.io/U46j4SsiS5uIYlpVZ0uhbQ   ##Volatility Memory Analysis Use





FTK mount ad1之後
再用autopsy 的add datasource 把mount的那個槽路徑加進去 就可以了~
