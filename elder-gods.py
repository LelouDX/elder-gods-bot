import random

lines = ['It is certain.', 'It is destined to be.', 'Without a doubt.', 'You have our blessing.', 'The Elder Gods will it so.', 'Yes.', 'Affirmative.', 'The realms are in agreement.', 'GO BALLS DEEP NIGGA', 'As certain as Sub-Zero is blue.', 'We have no time to attend to the folly of mortals.', 'You may consult with us at a later juncture.', 'Mortals are best left uninformed at times.', 'Some things elude our understanding even if for a short while.', 'RAIDEN IS A TWAT. Pass it on then you may consult us again.', 'Do not hope for it.', 'No.', 'We disagree to keep the realms in check.', "You Shao Kahn't", 'We, the Elder Gods, say no.']

def consult():
    st = input()
    if '!consult' in st:
        if len(st.split()) == 2 or '?' not in st:
            print('You did not ask a question, mortal.')
        else:
            print(lines[random.randint(0, 20)])
    else:
        pass
        
consult()