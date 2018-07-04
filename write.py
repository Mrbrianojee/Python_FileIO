f = open("newfile.txt", 'a')
lines = ["Hello", "world","welcome", "to", "file", "io"]
text = '\n'.join(lines)
f.writelines(text)
f.close()