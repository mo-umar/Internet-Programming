import requests


def save_page(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully Reached Website!!")
        response.encoding = 'utf-8'
        with open(file_name + '.txt', 'w') as f:
            print('File Created')
            f.write(response.text)
            print('Page Contents Copied Successfully!!')
    else:
        print("An Error Occurred.")


url = input("Enter Page URL: ")
file_name = input("Enter File Name: ")
save_page(url, file_name)
