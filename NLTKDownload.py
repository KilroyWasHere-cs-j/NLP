import nltk


def Download(item):
    nltk.download(item)

print('Enter package to download')
Input = input()
print('Downloading: ', Input)


Download(Input)

print('Dowmload complete')

