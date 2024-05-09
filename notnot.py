'''names: list[str] = ['b', 't', 'jef']

if 'b' not in names:
    print('not bob')
else:
    print('among us')
'''
#or

sel_user: str | None = None

if sel_user is not None:
    print(f'you in: {sel_user}')

else:
    print('go home')
    