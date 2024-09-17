''' 
    Lesson 3 - Using Strings
    Author: Mr. Kalisz 
    Date Created: September 17th, 2024 
    Date Last Modified: September 17th, 2024 
'''

#Review

num = 3 #3
num = 3 + 4 #7
num = num + 5 #12

print(num)

#print - no new line

print("Hello World") #Outputs the value in the brackets, then moves to the next line

print("Hello World", end = "") #replace the ending with nothing instead of a new line
print("Hello World Again")

#Concatentation - combine strings it puts them side by side

word = "123"
word2 = "456"

print(word + word2 + "!") #Combining strings always put them side by side
#print(word + 123) #Will not allow you to combine values of different data types usually

#Escape Character - "\"

#It alters the behaviour of the character that follows it inside of a string

print("\n") #newline character
print("Hello\nWorld")
print("Hello\tWorld") #tab

print("\"") #remove functionality from characters that are not standard
print("\\") #escape the escape character

#escape it adds functionality to characters that have none - n, t
#It removes functionality from character that are special - "" '' \

print("Hel'lo World")
print('World Hel"lo')