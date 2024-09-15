tool= float ( input('lotfan tool mostatil ra vared konid :'))

Arz= float( input('lotfan arz mostatil ra vared konid :'))

if Arz < 0 or tool < 0 :
    print( ' Error' )
else:
    masahat = tool * Arz
    mohit = 2* (tool+Arz)

    print ( f' mohite in mostatil {mohit} ast.')
    print ( f'masahate in mostatil {masahat} ast.')
