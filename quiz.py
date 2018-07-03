f = open("/home/ubuntu/workspace/files/relative_data.txt", 'r')
lines =  f.read()
f.close()
print(lines)




# brianojee:~/workspace/files (master) $ ls
# relative_data.txt
# brianojee:~/workspace/files (master) $ pwd
# /home/ubuntu/workspace/files
# brianojee:~/workspace/files (master) $ readlink -f relative_data.txt
# /home/ubuntu/workspace/files/relative_data.txt
# brianojee:~/workspace/files (master) $ 