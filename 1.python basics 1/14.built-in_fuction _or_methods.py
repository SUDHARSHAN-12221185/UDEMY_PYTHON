print(len('hellloooo')) #it dont start from zero but from one like us

greet='hellloooo'

print(greet[:len(greet)])
#buit in functions are words like print len and ext



#string methods are something which can only performed onn strings
#unlike function methods start with (.) for example we have .format

quote='to be or not to be'


print(quote.upper())#it converts everything into upper case and we have lower for lower case


print(quote.capitalize())#it capitalize first char 


print(quote.find('be'))#it tells us from which index given input is started (only first occurence)


print(quote.replace('be', 'me'))#it replaces as per given inputs in these case be with me
                #note it doesnt overwrite the quote so next time you print you can see be but not me
