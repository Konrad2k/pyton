

# message1='processing file %s'
# print(message1 % ('file_1.txt'))
# message2 = 'file %s has size %d KB'
# print(message2 %('file1_txt', 100))

# message3 = 'file %20s has size %10d KB'
# print(message3 %('file1_txt',100))

# message4='processing file{0:s}'
# print(message4.format('file1.txt'))


# message5='file {0:s} has size {1:d}'
# message5.format('file1.txt', 100)

# message6 ='file {0:20s} has size {1:10d}'
# print(message6.format('file1/txt',100))

helloMessage="Hello %s!"
print(helloMessage %('Kate'))

print(helloMessage %('Chris'))


helloMessage="Hello {0:s}!"
print(helloMessage.format ('Kate'))

print(helloMessage.format ('Chris'))

helloMessage1="%s has %d %s"

print(helloMessage1 % ("Kate",1,"animal"))


print(helloMessage1 %('Chris',100000, '$'))

helloMessage2="{0:s} has {1:d} {2:s}"

print(helloMessage2.format ("Kate",1,"animal"))

