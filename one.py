# import qrcode
# img = qrcode.make('hii hello')

# img.save('hello1.png')

import qrcode
img = qrcode.make('https://github.com/VigneswaranEngineer/claculator.git')
img.save('qr_code_for_calculator.png')

img1 = qrcode.make('https://github.com/VigneswaranEngineer/guess-the-number.git')
img1.save('guess_the_number.png')

img2 = qrcode.make('https://github.com/VigneswaranEngineer/rolling-dice.git')
img2.save('rolling_dice.png')