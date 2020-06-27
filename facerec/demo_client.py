import requests
import json

def test_face_match():
    url = 'http://127.0.0.1:5001/face_match'
    # open file in binary mode
    files = {'file1': open('sample_images/stark.jpg', 'rb'),
             'file2': open('sample_images/justin.jpg', 'rb')}     
    resp = requests.post(url, files=files)
    print( 'face_match response:\n', json.dumps(resp.json()) )
    
def test_face_rec():
    url = 'http://127.0.0.1:5001/face_rec'
    # open file in binary mode
    files = {'file': open('sample_images/hannah.jpg', 'rb')} 
    resp = requests.post(url, files = files)
    print( 'face_rec response:\n', json.dumps(resp.json()) )
    
def main():
    # test_face_match()
    test_face_rec()
    
if __name__ == '__main__':
    main()
