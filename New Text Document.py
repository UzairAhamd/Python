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
                                     #syntax is: encode(encoding,errors) default encoding="UTF-8" while errors could be 'backslashreplace'
                                                                              'ignore' 'namereplace' 'strict' 'replace' 'xmlcharrefreplace'
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

print("For only {price:.2f} dollars".format(price=58))    # returns the formatted string, forrmats the specified value(s) and insert 
                                                         #  them in the string's placeholders defined by {}
# placeholders can be identified using the named indexes {price}, numbered indexes{0} or even empty placeholders{}

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
      
'''
:< left aligns the result within the available space
:> right aligns the result within the available space
:^ center aligns the result within the available space
:= places the sign to the left most position
:+ use a plus sign to indicate if the result is positive or negative
:- use a minus sign for negative values only
:  use a space to insert an extra space before positive numbers(and a minus sign before negative numbers)
:, use a coomma as a thousand separator
:_ use an underscore as a thousand separator
:b binary format
:c converts the value into the corresponding unicode character
:d decimal format
:e scientic format, with a lower case e
:E scientic format, with an upper case E
:f fix point number format
:F fix point number format(in uppercase format show inf and nan as INF and NAN)
:g General fomat
:G General fomrat(using an upper case E for scientic notations)
:o octal format
:x hex format, lower case
:X hex format, upper case
:n number format
:% percentage format
'''
## format_map() ---formats specified values in a string to return a dictionary key's value and it doesn't create a new dictionary


print("hello world".index("e")
print("Company12".isalnum())			#space !#%&? etc. aren't alphanumeric
print("CompanyX".isalpha())			#if alphabets
print("Company234".isascii())			#check if all are ascii
print("\u0030".isdecimal(), "\u0047".isdecimal())	#checks if the unicode is of a decimal(0-9)  ## the output is True and False for 3 and G
print("5080".isdigit(),"\u00B2".isdigit())		#checks if the all are digits  ## second one is exponent of 2 and it gives true
print("Demo".isidentifier())			#only if alphanumeric or underscore but not the numberstart and with any space in it
print("hello world".islower())		#numbers symbols and spaces aren't checked only alphabets
print("3434".isnumeric(),"\u00B2".isnumeric()) 	#-1 and 4.5 aren't numeric bcz of - and . while exponents like 3/5 or 3 are numeric
print("hello #21".isprintable(),"hello\n there".isprintable())		#carriage return and line feed are not printable examples
print("   ".isspace())		#check if all the characters are whitespaces
print("Hello And, Welcome!".istitle())		#Check if each word start with an upper letter and the rest of it are lower letters
print("THIS IS NOW!".isupper())			#only alphabets are checked
print("@".join(("Horn","Peter","vicky"))) #output is Horn@Peter@vicky ##takes all itmes in an iterable and joins them into one string with specified serparator string
print("TEST".join({"name":"John","country":"Norway"})	#output is nameTESTcountry	##returned values are the keys not the values
print("banana".ljust(20),"is my favorite fruit.")	#returns a 20 character long left justified word banana with 14 whitespaces to the right
print("banana".ljust(20,"O"),"is my favorite fruit.")	#returns a 20 character long left justified word banana with 14 O to the right
print("Helo world".lower())	#lower the string case, names and symbols are ignored
print("you know","   banana   ".lstrip(),"is my favorite") 	#removes spaces to the left of the string
print("you you you yoooo ...banana".lstrip("yuo. "))






























































































