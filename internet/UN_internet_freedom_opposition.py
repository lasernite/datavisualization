some = ["Bolivia",
"Burundi",
"China",
"Cuba",
"Ecuador",
"India",
"Indonesia",
"Kyrgyzstan",
"Qatar",
"Russian Federation",
"Saudi Arabia",
"South Africa",
"United Arab Emirates",
"Venezuela",
"Vietnam",
"Algeria",
"Bangladesh",
"Congo",
"Cote D'Ivoire",
"Ethiopia",
"Mongolia",
"Namibia",
"Philippines",
"Togo",

"Bangladesh",
"Bolivia",
"Burundi",
"China",
"Cuba",
"Congo",
"Ecuador",
"India",
"Indonesia",
"Kenya",
"Qatar",
"Russian Federation",
"Saudi Arabia",
"South Africa",
"United Arab Emirates",
"Venezuela",
"Vietnam",
"Cote D'Ivoire",
"Ethiopia",
"Kyrgyzstan",
"Togo"]

someall = []

for country in some:
	if country not in someall:
		someall.append(country)

print someall
print len(someall)
print len(some)


['Bolivia', -1],
['Burundi', -1],
['China', -1],
['Cuba', -1],
['Ecuador', -1],
['India', -1],
['Indonesia', -1],
['Kyrgyzstan', -1],
['Qatar', -1],
['Russian Federation', -1],
['Saudi Arabia', -1],
['South Africa', -1],
['United Arab Emirates', -1],
['Venezuela', -1],
['Vietnam', -1],
['Algeria', -1],
['Bangladesh', -1],
['Congo', -1],
["Cote D'Ivoire", -1],
['Ethiopia', -1],
['Mongolia', -1],
['Namibia', -1],
['Philippines', -1],
['Togo', -1],
['Kenya', -1]
