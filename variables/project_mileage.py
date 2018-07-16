'''
Created on 30 Jun 2018

@author: jegramos
'''

#Converting kilometers to miles

question = "How may kilometers did you ran today?"

kms = input(question)

kms = float(kms)

mls = kms * 0.621371

mls = round(mls, 2)

print(f"You ran {kms} kilometers which is {mls} miles")