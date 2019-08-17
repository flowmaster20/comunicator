import ftplib
import urllib.request


def get_file(usr):
    server = "m3s4ge.cba.pl"
    username = "admin@m3s4ge.cba.pl"
    pssd = "M4t1K0jr0"
    ftp_connection = ftplib.FTP(server, username, pssd)
    remote_path = "/" + str(usr)
    ftp_connection.cwd(remote_path)
    print(remote_path)
    fh = open("output.txt.aes", 'wb')
    ftp_connection.retrbinary('RETR output.txt.aes', fh.write)


def upload_file(usr):
    server = "m3s4ge.cba.pl"
    username = "admin@m3s4ge.cba.pl"
    pssd = "M4t1K0jr0"
    ftp_connection = ftplib.FTP(server, username, pssd)
    remote_path = "/" + str(usr)
    ftp_connection.cwd(remote_path)
    fh = open("output.txt.aes", 'rb')
    ftp_connection.storbinary('STOR output.txt.aes', fh)
    fh.close()
