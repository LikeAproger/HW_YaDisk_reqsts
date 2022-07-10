import requests
import pathlib


class ya_disc_upload:
    token = ''

    def __init__(self, file_name, pth_file):
        self.file_name = file_name
        self.pth_file = pth_file

    def upload(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        hdrs = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        prms = {'path': self.file_name, 'overwrite': 'true'}
        upld_link = requests.get(url, headers=hdrs, params=prms).json()['href']
        req = requests.put(upld_link, data=open(pathlib.Path(self.pth_file, self.file_name), 'rb'))
        req.raise_for_status()
        if req.status_code == 201:
            return 'File uploaded successfully'
        return 'Uploading failed'


if __name__ == "__main__":
    file_name = 'testFile.txt'
    pth_file = 'D:\\'
    uploader = ya_disc_upload(file_name, pth_file)
    print(uploader.upload())
