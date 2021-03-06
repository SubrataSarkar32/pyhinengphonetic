'''Python implementation of hindi to english phonetic in hindi.

-------------------------------------------------------------------------------
Copyright (C) 2016 Subrata Sarkar <subrotosarkar32@gmail.com>
original by:- Subrata Sarkar <subrotosarkar32@gmail.com>

This file is part of pyhinengphonetic.

pyhinengphonetic is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyhinengphonetic is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pybengengphonetic.  If not, see <http://www.gnu.org/licenses/>.

This tool converts unicode data to speakable pyttsx data
   using convert_to_pyttsx_speakable() and converts unicode data to speakable
   phonetic using convert_to_speakable_phonetic() and speak bengali
   using speak()
Example:convert_to_pyttsx_speakable(u'\u0915\u0948\u0938\u0947 \u0939\u0947')
        speak(u'\u0915\u0948\u0938\u0947 \u0939\u0947')'''
def convert_to_pyttsx_speakable(gitre=u''):
    text2=u''
    
    list19=[]
    import string
    for letter in gitre:
        list19+=[letter]
    singlet=0
    while singlet <(len(list19)):
        try:
                 str(list19[singlet])
                 text2+=list19[singlet]
        except UnicodeEncodeError:
                 matra=u'\u0905\u0906\u0907\u0908\u0909\u090a\u090f\u0910\u0913\u090b\u093e\u093f\u0940\u0941\u0942\u0943\u0947\u0948\u094b\u094c'
                 try:
                     if list19[singlet+1] in matra:
                         text2+=list19[singlet]
                         singlet+=1
                         text2+=list19[singlet]
                     elif list19[singlet] in unicode(string.printable):
                        text2=text2+list19[singlet]
                     elif list19[singlet] in matra:
                        text2=text2+list19[singlet]
                     else:
                         text2=text2+list19[singlet]+u'a'
                 except:
                     if list19[singlet] in unicode(string.printable):
                        text2=text2+list19[singlet]
                     elif list19[singlet] in matra:
                        text2=text2+list19[singlet]
                     else:
                         text2=text2+list19[singlet]+u'a'
        singlet+=1
    gitre=text2
    import hinavro
    gitre=hinavro.parse(gitre)
    return gitre

def convert_to_speakable_phonetic(gitre=u''):
    text2=u''
    
    list19=[]
    import string
    for letter in gitre:
        list19+=[letter]
    singlet=0
    while singlet <(len(list19)):
        try:
                 str(list19[singlet])
                 text2+=list19[singlet]
        except UnicodeEncodeError:
                 matra=u'\u0905\u0906\u0907\u0908\u0909\u090a\u090f\u0910\u0913\u090b\u093e\u093f\u0940\u0941\u0942\u0943\u0947\u0948\u094b\u094c'
                 try:
                     if list19[singlet+1] in matra:
                         text2+=list19[singlet]
                         singlet+=1
                         text2+=list19[singlet]
                     elif list19[singlet] in unicode(string.printable):
                        text2=text2+list19[singlet]
                     elif list19[singlet] in matra:
                        text2=text2+list19[singlet]
                     else:
                         text2=text2+list19[singlet]+u'a'
                 except:
                     if list19[singlet] in unicode(string.printable):
                        text2=text2+list19[singlet]
                     elif list19[singlet] in matra:
                        text2=text2+list19[singlet]
                     else:
                         text2=text2+list19[singlet]+u'a'
        singlet+=1
    return text2

def speak(text=u''):
    import pyttsx
    engine = pyttsx.init()
    engine.setProperty('volume', 1.0)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-110)    
    speakman1=convert_to_pyttsx_speakable(gitre=text)
    engine.say(speakman1)
    engine.runAndWait()
    return 'Speak Over'

if __name__ == "__main__":
    speak(u'\u0915\u0948\u0938\u0947 \u0939\u0947')
