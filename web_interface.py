import ftplib
import urllib.request


def get_file(url):
    urllib.request.urlretrieve(url, "data.txt.aes")


def upload_file():
    server = "ftp://m3s4ge.cba.pl"
    username = "admin@m3s4ge.cba.pl"
    pssd = "M4t1K0jr0"
    ftp_connection = ftplib.FTP(server, username, pssd)
