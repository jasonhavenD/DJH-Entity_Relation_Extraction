def getEn(list,nn):
    #print "nn="+str(nn)
    flag_left = nn
    flag_right = nn
    enl = ""
    enr = ""
    for (j,n) in list:
        #print "n="+str(n)
        if n < nn:
            if nn == flag_left:
                flag_left = n
                enl = j
            elif n > flag_left:
                flag_left = n
                enl = j
        else:
            if nn == flag_right:
                flag_right = n
                enr = j
            if n < flag_right:
                flag_right = n
                enr = j
    ll = nn - flag_left
    rr = flag_right - nn

    return enl,enr,ll,rr
'''
    if ll > 6:
        enl = ""
    if rr > 4:
        enr = ""
'''
    
        
def main():
    f1 = open('test-info1.txt')
    f2 = open('test_sentence_my4.txt','w')
    f3 = open('relation-list-my4.txt','w')
    lines = f1.readlines()
    list1 = []
    list2 = []
    list3 = []
    str1 = ''
    str2 = ''
    n = 0
    count = 0
    ll = 0
    rr = 0
    for line in lines:
             n = n+1
             if line == '\n':
               #print(list2)
               for i in list1:
                   f2.write(i+" ")
               f2.write("\t")
               
               for (j,nn) in list2:
                   entity1,entity2,l,r = getEn(list3,nn)
                   
                   if entity1 != "" and entity2 != "":
                      count = count + 1
                      ll = ll + l
                      rr = rr + r
                      if j == list2[-1][0]:
                          f2.write("#"+entity1+"#"+entity2+"#"+j)
                          f3.write("#"+entity1+"#"+entity2+"#"+j+"\n")
                      else:
                          f2.write("#"+entity1+"#"+entity2+"#"+j+"\t")
                          f3.write("#"+entity1+"#"+entity2+"#"+j+"\n")

               f2.write("\n")
               list1 = []
               list2 = []
               list3 = []
             else:
               word,part,entitytag,relationtag1,relationtag2 = line.split()
               tag = relationtag2
               list1.append(word)
               if tag.startswith('B'):
                   if str1 != '':
                       list2.append((str1,n))
                       str1 = word
                   else:
                       str1=word
               elif tag.startswith('I'):
                   str1=str1+" "+word
               elif tag.startswith('E'):
                   str1=str1+" "+word
               elif tag.startswith('S'):
                   if str1 != '':
                       list2.append((str1,n))
                       str1 = word
                   else:
                       str1 = word
               else:
                   if str1 != '':
                      list2.append((str1,n))
                      str1 = ''
               tag = entitytag
               if tag.startswith('B'):
                   if str2 != '':
                       list3.append((str2,n))
                       str2 = word
                   else:
                       str2=word
               elif tag.startswith('I'):
                   str2=str2+" "+word
               elif tag.startswith('E'):
                   str2=str2+" "+word
               elif tag.startswith('S'):
                   if str2 != '':
                       list3.append((str2,n))
                       str2 = word
                   else:
                       str2 = word
               else:
                   if str2 != '':
                      list3.append((str2,n))
                      str2 = ''
    zuo = ll/count
    you = rr/count
    print(str(zuo)+" "+str(you))
 
                   
if __name__ == "__main__":
  main()
