myfile=ABopenfile("story.txt",False)
log("Hello World!")

firstCharacter = myfile.readat(1,0)
log(firstCharacter)

lengthOfFile = len(myfile.readat(None,0))
log(lengthOfFile)


endPosition = lengthOfFile - 1
lastCharacter =  myfile.readat(lengthOfFile,endPosition)
log(lastCharacter)


#change 'lamb' in first sentence to LAMB

myfile.writeat("LAMB",18)

#add sentence to the end
myfile.writeat("\nAnd the children loved the lamb as well.", endPosition + 1)

myfile.close
