import ftplib
import urllib.request


def get_file(url):
    urllib.request.urlretrieve(url, "data.txt.aes")


def upload_file():
    server = "m3s4ge.cba.pl"
    username = "admin@m3s4ge.cba.pl"
    pssd = "M4t1K0jr0"
    ftp_connection = ftplib.FTP(server, username, pssd)
    remote_path = "/"
    ftp_connection.cwd(remote_path)
    fh = open("output.txt.aes", 'rb')
    ftp_connection.storbinary('STOR output.txt.aes', fh)
    fh.close()
