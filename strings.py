'''
Topic #1: Strings (chuỗi ký tự) - 
'''
# String: ordered, immutable, text presentation
# Escaping Backslash \
'''
my_string = 'I\'m a "Sinh viên năm 2 Trường SPKT"'
my_string = "I'm living in \"Việt Nam\""
print(my_string)
'''
# backslash if you want to continue in the next line 
# (ở code thì gọn gàng, nhưng ở terminal thì chỉ có 1 line)
'''
my_string = "Với mong muốn trở thành lập trình viên giỏi \
thành thạo ngôn ngữ lập trinh python"
print(my_string)
'''

'''
Topic #3: Access characters and substrings
'''

my_string = "Hello World"
# get character by referring to index
char = my_string[0] #--> "H"
char = my_string[-1] #--> "d"
char = my_string[-2] #--> "l"
# print(char)
# String is immutable -> Cannot be changed
#my_string [0] = "M" #-> error

my_string = "Hello World"

# Substrings with slicing
# stringName [startIndex:endIndex]
# start at index 1 and go until index 5 (not include #5)
sub_string = my_string[1:5] #--> "ello"
sub_string = my_string[:5] #--> "Hello"
sub_string = my_string[6:] #--> "World"
sub_string = my_string[::-1] # Reverse the String (đảo chuỗi) --> "dlroW olleH"
sub_string = my_string[::2] # take every second character (lấy vị trí thứ 2 mỗi lần đếm)
#print(sub_string)

'''
Topic #3: Concatenate two or more strings
'''

# concat strings with +

greeting = "Hello, chào mọi người"
channel = "Hành trình tự do tài chính!!"
sentence = greeting + " Chào mừng các bạn đến với " + channel
#print(sentence) Hello, chào mọi người Chào mừng các bạn đến với Hành trình tự do tài chính!!

# join elements of a list into a string: .join()
# Nối chuỗi

my_list = ['How', 'are', 'you', 'doing']
sentence = ' '.join(my_list)
#print(sentence) --> How are you doing

'''
Topic #4: Iterating
'''
# Iterating over a string by using a for in loop

my_string = "Hello Xin Chao Cac Ban"

# for char in my_string:
#     print(char)

if "X" in my_string:
    print("yess")
else:
    print("No")
'''
Topic #5: Basic & Useful Function (Hàm cơ bản và Hữu ích)
'''
#strip()
# 'I am alone' --> Strips all whitespace characters from both ends.
print("   I am alone   ".strip()) #->"I am alone"
print("On an island".strip('O')) #-> "n an island"
 
#split()
print('but life is good'.split())
A = "I am alone, but life is good"
print(A.split())
print(''.join(A))
print('but, very boring'.split(',')) # tách ra chỗ dấu ','

#replace()
print('Help me'.replace("me", "you")) #thay thế từ me thành you

#Hàm kiểm tra
my_string = 'Need to make a fire'
print(my_string.startswith('Need')) #-->True

my_string = 'and cook rice'
print(my_string.endswith('Need')) #-->False

my_string = 'bye bye bae'
print(my_string.index('bye')) #--> 0 return vị trí 
print(my_string.find('W')) #--> -1 không tìm thấy

#upper()
my_string = 'still there?'
print(my_string.upper()) # in hoa

#lower()
my_string = 'HELLO WORLD'
print(my_string.lower()) # in thường

#title()
my_string = 'how are you?'
print(my_string.title()) # in hoa chữ cái đầu mỗi chữ 'How Are You?'

my_string = 'ok, I am fine thank you'
print(my_string.capitalize()) #--> 'Ok, i am fine thank you'

#count()
my_string = 'ok, I am fine thank you'
print(my_string.count('a'))

'''
String Formatting
'''
# %, .format(), f-Strings

# %
name = "CodeXplore"
my_string = "welcome to %s" % name
print(my_string)

pi = 3.14159
s = "pi number"
my_string = "Variable is %.2f from to %s " % (pi, s)
print(my_string)

# .format()
age = 24
B = "old"
height = 170.5
my_string = "I am {} years {}, {:.3f} cm".format(age, B, height) 
print(my_string)

# f-Strings
pi = 3.14159
name = "Thanh Huy"
age = 20
my_string = f"Pi is {pi:.2f} and my name is {name}, {age} years old" 
print(my_string)