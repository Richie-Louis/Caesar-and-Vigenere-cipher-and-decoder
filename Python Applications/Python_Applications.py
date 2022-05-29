def LongestWord(sen):

  # code goes here

  #sen2 = sen2.strip()
  #sen3 = sen2.split()
  sen2 = sen.replace('&','').replace(':','').replace('!','').replace('~','').replace('/','').replace('[','').strip().split()
  test = sen2[0]
  for index in range(1,len(sen2)):
    if len(sen2[index-1]) < len(sen2[index]) and len(test) < len(sen2[index]):
      test = sen2[index]
  return test

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def Decoder(string, offset):
    decode = ""
    for letter in string:
        for index in range(len(alphabet)):
            if letter == alphabet[index]:
                decode += alphabet[(index + offset) % 26]
            elif letter == " ":
                decode += " "
                break
            elif letter == '!':
                decode += '!'
                break
            elif letter == ".":
                decode += "."
                break
            elif letter == '\'':
                decode += '\''
                break
    return decode

def Coder(string, offset):
    decode = ""
    for letter in string:
        for index in range(len(alphabet)):
            if letter == alphabet[index]:
                decode += alphabet[(index - offset) % 26]
            elif letter == " ":
                decode += " "
                break
            elif letter == '!':
                decode += '!'
                break
            elif letter == ".":
                decode += "."
                break
            elif letter == '\'':
                decode += '\''
                break
    return decode

def VigenereDecoder(string, keyword):
    decode = ""
    test = ""
    i = 0
    for index in range(len(string)):
        test += keyword[i]
        i += 1
        if i >= len(keyword):
            i = 0
    j = 0
    for s in string:
        for index in range(len(alphabet)):
            if s == alphabet[index]:
                decode += alphabet[index - alphabet.index(test[j])]
                j += 1
            elif s == " ":
                decode += " "
                break
            elif s == '?':
                decode += '?'
                break
            elif s == '!':
                decode += '!'
                break

    return decode

    #for s in string:
    #    for k in keyword:
    #        for index in range(len(alphabet)):
    #            if s == alphabet[index]:
    #                decode += alphabet[(index - alphabet.index(k)) % 26]
    #                break
                
    return test
 
# The string to test is "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

# The offset is 10 to the right


# print(LongestWord("a confusing /:sentence:/[ this is not!!!!!!!~ time"))

#print(Decoder("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"))
#print(Coder("hey buddy! i was able to decipher your code. it was fun. i am looking forward to deciphering your next one!"))
#print(Decoder("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.",10))
#for index in range(len(alphabet)):
#    print(index, Decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",index))

#print(Decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",7))
#for index in range(len(alphabet)):
#    print(index , alphabet[index])
# print((16 + 10) % 26)

print(VigenereDecoder("dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!", "friends"))
