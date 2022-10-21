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
print("my name is Ståle".encode())   #encodes the string, using the specified encoding, if no encoding is specified, UTF-8 will be used
                                     #syntax is: encode(encoding,errors) default encoding="UTF-8" while errors could be 'backslashreplace' 'ignore' 'namereplace' 'strict' 'replace' 'xmlcharrefreplace'
