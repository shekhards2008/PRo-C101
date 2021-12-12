import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_folder(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dir,files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root,file)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = "/"+file_to+"/"+relative_path
                print(dropbox_path)
                with open(file_from,'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A-BbX95axp5CqQdk9S3-xeKuZxRx2lWksV8NQ9FjxL4YvOrOmSUCMNgli4m-wute5QP_pygPEFVFJq2XX3_3Gm2lt1ZJZgy4eW1y7vllByPhf9svL-SImKq4i3-60dUZbA5IOAo'
    transferdata = TransferData(access_token)

    file_from = input("Enter Your Source Location")
    file_to = input("Write your Location")
    transferdata.upload_folder(file_from,file_to)
    print("Files uploaded successfully!")

if __name__ == '__main__':
    main()