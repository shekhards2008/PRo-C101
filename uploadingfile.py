import dropbox
import os

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
                    dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.A6kWXk0lV6FHFKJCwtaeouHFfLnZLpH6d5_511D4FjWjB_J0ZATsS0SqFIo7Y30azF0sGeFxPEgsTfB2EbjtYhSlt_Pba4ISoEVyBm10EjDpe0dZeMur7UH1xhKH0T2nZjwhq8M'
    transferdata = TransferData(access_token)

    file_from = 'C:/Users/Desktop/Whitehatjr Projects/PRO-C101 Cloud Storage/test.txt'
    file_to = 'C:/Users/Desktop/Whitehatjr Projects'
    transferdata.upload_folder(file_from,file_to)
    print("Files uploaded successfully!")

if __name__ == '__main__':
    main()