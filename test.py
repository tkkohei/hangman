# my_file = open('lib.txt', 'r')
# my_text = my_file.read()
# print(my_text)
# my_file.close()

# hello = '!?are you there?!'
# goodbye = '?!fine be that !way!?!!'

# hello = hello.strip('!?')
# goodbye = goodbye.strip('!?')

# print(hello)
# print(goodbye)

try:
    filename = 'notthere.txt'
    file = open(filename, 'r')
except FileNotFoundError:
    print('すみません、', filename, 'が見つかりませんでした。')
except IsADirectoryError:
    print("ファイルではなくディレクトリです")
else:
    print('うまくファイルを開きました')
    file.close()
finally:
    print("何が起こっても動作します")