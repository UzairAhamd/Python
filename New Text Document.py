#######################Strings
#multiline strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings in python are arrays of bytes representing unicode characters.
#python doesn't have a character data type, a character is simply a string with a length of 1

a="hello world"
print(a[0])

#Looping throughh a string
for x in a:
  print(x)
print(len(a))

#check for a phrase or character
print("hell" in a)
if "hell" in a:
  print("yes")
print("well" not in a)
if "well" not in a:
  print("No")

#slice 3rd and 4th
print(a[2:5])

print(a[:5]) #first five
print(a[2:]) #from 3rd and onward
print(a[-5:-2]) #rerurns orl

#uppercase
prinyt(a.upper())
#lowercase
print(a.lower())

#remove whitespaces(before and/or after)
a=" Hello world "
print(a.strip())

#replace string
a=" Hello world "
print(a.replace("H","J")

#split string
print(a.split(" ")) # retruns ["Hello","world"]

#string concatenation
print("Hello"+"world")
print("Hello"+" "+"world")

##we can combine string and number using format() method
## the format() takes the passed arguments, formats them, and places in the string where the placeholders{} are
print("my age is {}".format(5))
print("my age is {} and I'm {} tall and my weight is {}".format(3, 48,50)) 
print("I want to pay {2} dollars for {0} pieces of item {1}.".format(10,25.4,35)) ##indexing to be sure about correct placement

#escape character \  -- to insert characters that are illegal in a string
print("we are \"vikings\" from the north")
# \' single quote
# \\ backlash
# \n new line
# \r carriage return
# \t tab
# \b backspace
# \f formfeed
# \ooo octal value
# \xhh hex value

#String built-in methods
print(a.capitalize())     #first character in upper case and rest in lower case, but if the first charater is a number it won't capitalize the number
print(a.casefold())     # returns a string with all lower, more stronger than lower() method
print(a.center(20)      # taking up the space of 10 characters with Hello world in the middle, by default space is the padding
print.center(20,"O")        # padding with O now character
print(a.count("l"))
print(a.count("l",2,-2)        #from third member till the second last

txt = "My name is Ståle."
print("my name is Ståle.".encode())   #encodes the string, using the specified encoding, if no encoding is specified, UTF-8 will be used
                                     #syntax is: encode(encoding,errors) default encoding="UTF-8" while errors could be 'backslashreplace' 'ignore' 'namereplace' 'strict' 'replace' 'xmlcharrefreplace'
print(txt.encode(encoding="ascii",errors="backslashreplace"))         #b'My name is St\\xe5le'
print(txt.encode(encoding="ascii",errors="ignore"))                   #b'My name is Stle'
print(txt.encode(encoding="ascii",errors="namereplace"))              #b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(txt.encode(encoding="ascii",errors="replace"))                  #b'My name is St?le'
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))        #b'My name is Ståle'

print(txt.endswith(".")												#check if the string ends with a dot
print(txt.endswith("my world.",5,11))
			
print("H\te\tl\tl\to")												# default tab size is 8
print("H\te\tl\tl\to".expandable(2))					# sets the tab to 2 whitespaces

txt="Hello and welcome here"
print(txt.find("welcome")		#finds the first occurence of value, returns -1 if not, same as index() but it does not raise an exception if not found
print(txt.find("welcome",2,9)

