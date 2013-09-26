import validio

files = ['control.txt', 'corncob_lowercase.txt']

for text_file in files:
    validio.check_words(text_file, True)
