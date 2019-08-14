#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate


def main():

    array = ["en","af","ar","az","be","bg","ca","cs","cy","da","de","dv","el","eo","es","et","eu","fa","fi","fo","fr","gl","gu","he","hi","hr","hu","hy","id","is","it","ja","ka","kk","kn","ko","kok","ky","lt","lv","mi","mk","mn","mr","ms","mt","nb","nl","ns","pa","pl","ps","pt","qu","ro","ru","sa","se","sk","sl","sq","sv","sw","syr","ta","te","th","tl","tn","tr","tt","ts","uk","ur","uz","vi","xh","zh","zu"]

    array2 = ["english","Afrikaans","Arabic","Azeri","Belarusian","Bulgarian","Catalan","Czech","Welsh","Danish","German","Divehi","Greek","Esperanto","Spanish","Estonian","Basque","Farsi","Finnish","Faroese","French","Galician","Gujarati","Hebrew","Hindi","Croatian","Hungarian","Armenian","Indonesian","Icelandic","Italian","Japanese","Georgian","Kazakh","Kannada","Korean","Konkani","Kyrgyz","Lithuanian","Latvian","Maori","FYRO Macedonian","Mongolian","Marathi","Malay","Maltese","Norwegian","Dutch","Northern Sotho","Punjabi","Polish","Pashto","Portuguese","Quechua","Romanian","Russian","Sanskrit","Sami","Slovak","Slovenian","Albanian","Swedish","Swahili","Syriac","Tamil","Telugu","Thai","Tagalog","Tswana","Turkish","Tatar","Tsonga","Ukrainian","Urdu","Uzbek","Vietnamese","Xhosa","Chinese","Zulu"]

    pos = 0
    
    print("Translating Text\n Please Wait...")

    file_n = open("translation_output.txt","w",encoding="utf-8")

    while pos < len(array):
        file_n.write("Language: " + array2[pos])
        file_n.write("\n")
        file_n.write("\nTitle: \n")
        with open('longdesc.txt',"r",encoding="utf-8") as f1:
            get_long_desc = 0
            for line in f1:
                line = line.rstrip('\n')
                if line == "[long_description]":
                    get_long_desc = 1
                elif line == "[short_description]":
                    get_long_desc = 2
                elif line == "[title]":
                    get_long_desc = 3
                elif get_long_desc == 3:
                    file_n.write(translate(line, array[pos]))
                    file_n.write("\n")
        f1.close()
        file_n.write("\nShort Desc: \n")
        with open('longdesc.txt',"r",encoding="utf-8") as f1:
            get_long_desc = 0
            for line in f1:
                line = line.rstrip('\n')
                if line == "[long_description]":
                    get_long_desc = 1
                elif line == "[short_description]":
                    get_long_desc = 2
                elif get_long_desc == 2:
                    file_n.write(translate(line, array[pos]))
                    file_n.write("\n")
        f1.close()
        file_n.write("\nLong Desc:\n")
        with open('longdesc.txt',"r",encoding="utf-8") as f1:
            get_long_desc = 0
            for line in f1:
                line = line.rstrip('\n')
                if line == "[long_description]":
                    get_long_desc = 1
                elif get_long_desc == 1:
                    file_n.write(translate(line, array[pos]))
                    file_n.write("\n")
        f1.close()
        file_n.write("\n================================================\n")
        print("Translation " + str(pos+1) + " of 79 completed.")
        pos += 1


    file_n.close()
    
 

if __name__ == '__main__':
    main()
