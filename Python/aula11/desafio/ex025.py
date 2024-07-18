name = str(input('\033[1;30;46mQual é seu nome completo? ')).strip()

print('Seu nome tem Silva? {}'.format('silva' in name.lower()))
