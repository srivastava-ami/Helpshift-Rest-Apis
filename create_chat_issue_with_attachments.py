import requests
import filetype


payload = {'identifier': 'amit.srivastava@helpshift.com',
           'message-body': 'Creating issue with multiple/single attachment',
           'platform-type': 'webchat',
           'platform-id': 'amits-demo_platform_20191206215417695-311dd0dd4141146'}

headers = {
    'Authorization': 'Basic '
}

url = "https://api.helpshift.com/v1/amits-demo/chat/issues"
filename = "Quotient-Jira Integration.pdf"
file_content_type = filetype.guess_mime(filename)
files = []
with open(filename, 'rb') as filedata:
    attachment_data = files.append(('attachments', (filename, filedata, file_content_type)))
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.status_code)
    print(response.json())
