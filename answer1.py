import re
emails = [ "zuck26@facebook.com" , "page33@google.com" ,
"jeff42@amazon.com"]
desired_outputs=[]

for i in range(len(emails)):
    new=re.split('\W',emails[i])
    desired_outputs.append(new)

print(desired_outputs)