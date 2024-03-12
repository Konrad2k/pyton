Tax=(4,7,8,23)
print(Tax[-1])
print(Tax)

print(Tax.index(7))
print(max(Tax))

TaxList=list(Tax)
print(TaxList)
TaxList.append(30)
NewTaq=tuple(TaxList)
print(NewTaq)

(tax1,tax2,tax3,tax4)=Tax
print( tax1,tax2,tax3,tax4)
a=1
b=5
(a,b)=(b,a)
print("a =",a, " b = ",b)

#exercises
#1
marketing=['loyality program','client promotion','market research']
#2
marketing.append('public relations')
#3
print(marketing[3])
#4
marketing.insert(2,'investor relations')
#5
emailMarketing=marketing.copy()
print(emailMarketing)
#6
emailMarketing.sort()
#7
internalEmails=['internal communication']
#8
emailMarketing.extend(internalEmails)
#9
mails=tuple(emailMarketing)
print(mails)