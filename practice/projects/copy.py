file1 = open("score.txt","r+")
data= file1.read()
file2=open("scorecopy.txt","w")
file2.write(data)