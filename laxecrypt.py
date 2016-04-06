#-*- coding: utf-8 -*-
#Data: 22/07 22:17
#Pedro Laxe
from termcolor import colored

print colored(" __     __   _  _  ____  ___  ____  _  _  ____  ____","red");
print colored("(  )   / _\ ( \/ )(  __)/ __)(  _ \( \/ )(  _ \(_  _)","red");
print colored("/ (_/\/    \ )  (  ) _)( (__  )   / )  /  ) __/  )(","red");
print colored("\____/\_/\_/(_/\_)(____)\___)(__\_)(__/  (__)   (__)","red");
print "\n\n"

print "1 - Encriptar\n"
print "2 - Decriptar\n"
escolha = int(raw_input("Digite uma opção: "))
if escolha == 1:
	encriptarvar = raw_input("Digite algo para Encriptar: ");
elif escolha == 2:
	decriptarvar = raw_input("Digite algo para Decriptar: ");
chaves = [
'a', 'A',
'b', 'B',
'c', 'C',
'd', 'D',
'e', 'E',
'f', 'F',
'g' ,'G',
'h', 'H',
'i', 'I',
'j', 'J',
'k', 'K',
'l', 'L',
'm', 'M',
'n', 'N',
'o', 'O',
'p', 'P',
'q', 'Q',
'r', 'R',
's', 'S',
't', 'T',
'u', 'U',
'v', 'V',
'w', 'W',
'x', 'X',
'y', 'Y',
'z', 'Z',
'$',
'#',
'-',
'|',
':',
';',
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'0'
]
cchaves = [
'01jw', '01Jw',
'03fp', '03Fp',
'02eg', '02Eg',
'03bo', '03Bo',
'01hp', '01Hp',
'04bb', '04Bb',
'09mm', '09Mm',
'01ee', '01Ee',
'05xx', '05Xx',
'02pe', '02Pe',
'07jw', '07Jw',
'03cp', '03Cp',
'02rr', '02Rr',
'09oq', '09Oq',
'08oo', '08Oo',
'03ww', '03Ww',
'06aq', '06Aq',
'09cc', '09Cc',
'05km', '05Km',
'08bb', '08Bb',
'07aa', '07Aa',
'04vv', '04Vv',
'09jj', '09Jj',
'06bd', '06Bd',
'03ss', '03Ss',
'01zz', '01Zz',
'05si',
'09tr',
'08cx',
'08mm',
'09dx',
'07ml',
'01gg',
'02hg',
'03jk',
'04lp',
'05po',
'06io',
'07kl',
'08hj',
'09uu',
'01oo'
]

encryp = ''
decryp = ''

#Funções

def laxeCrypt(string):

	global chaves
	global cchaves

	global encryp

	for letter in string:
		sid = chaves.index(letter)

		encryp = encryp + cchaves[sid]

	return (encryp)

def laxeDecrypt(string):
	global chaves
	global cchaves

	global decryp

	dec = string.split('0')

	for setConj in dec:
		# Remove Array vazio
		if (setConj == ''):
			continue

		decSet = '0' + setConj
		did = cchaves.index(decSet)
		decryp = decryp + chaves[did]

	return (decryp)

#testes
if escolha ==1:
	print "Resultado: ",laxeCrypt(encriptarvar)
elif escolha == 2:
	print "Resultado: ",laxeDecrypt(decriptarvar)
else:
	print "Opção Inválida!"
#laxeDecrypt("08oo02eg01jw09cc01jw03bo01hp03fp09cc05xx09oq02eg08oo01hp03fp05xx02eg01ee01jw")
