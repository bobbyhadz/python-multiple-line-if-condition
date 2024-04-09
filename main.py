# Styling multiline if statements in Python

if ('hi' == 'hi' and
        len('hi') == 2 and
        2 == 2):  # 👈️ Last lines with extra indentation
    print('success')

# 👇️ All conditions on separate lines
if (
    'hi' == 'hi' and
    len('hi') == 2 and
    2 == 2
):
    print('success')
