# ctf
use for ctf
python is for Crypto 
C is for Reverse





Kali command list


#share folder
mount -t cifs -o uid=1000,gid=1000,username=chingsi,password=P@ssword1234567 //192.168.14.1/share ~/share



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