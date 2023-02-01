import re
a='my phone number is 9851042091 and his phone number in usa is (999)-333-7777'
pattern=r"\(\d{3}\)-\d{3}-\d{4}|\d{10}"
z=re.findall(pattern,a)
print(z)


text="Detailed match information will be displayed here automatically. My phone number is 9851042091 and his phone number in usa is (999)-333-7777 Note 1 - Observation Note 2 - servation"
pattern=r'Note \d - ([^n]*)'
print(re.findall(pattern,text))

text='My name is Atit and my Company address are FY2020 Q4 , FY2022 Q1 ,FY2021 Q2 , FY2020 Q6 and so on fy2021 Q2'
pattern=r'FY\d{4} Q[1-4]'
print(re.findall(pattern,text,flags=re.IGNORECASE))



money='I have $20 million , I have $90.85 '
pattern=r'\$([0-9\.]+)'
print(re.findall(pattern,money))

