
def main():

  final = []                            #Final answer
  start = []                            #Start set
  V = str(input())                      #Enter sequence 101010101...
  
  ''' Test set in task
  #V = '11001110011'
  #V = '1111111'
  #V = '10101010111110000101010010'
  #V = '000001111110000001111110000110'
  '''
  for i in V:
    start.append(i)             #String to list (I feel so comfortable)

  final.append(start.pop(0))    #first element of the sequence 

  while len(start)>0:           #While in Start to have elements, do...
    scan = start.pop(0)         #Take the first item (in Start) to scan
    i=0                         #Counter (No...)

    if scan == final[i]:        #If the first element in the “Start” == the first element in the “Final” 
      try:                      #Exception
        c = scan + start.pop(i) #C = line 20 + next elements in the “Start”
        for k in final:         #Check other elements in the Final
          if c == k:
            c +=start.pop(i)    #If true then plus one more elements        
        final.append(c)         #Write to Final
      except IndexError:        #If missing "one more elements", then...
        try:
          if c > scan:          #Compare which is longer (string)
            final.append(c)
          else:
            final.append(scan)
        except TypeError:       #Exception, mb c = "None" / line 46
          final.append(scan)
    else:                       #If line 23 / Read as "If scan != final[0]"
      for k in final:           #Check other elements in the Final
        if k == scan:           #Similar like on line 26-28
          try:
            scan += start.pop(i)
          except IndexError:    #If last element, then break
            break                    
      final.append(scan)        #Write to Final
    c = None

  #Output on the task
  Res = ''
  for R in final:
    Res += R + ' '
  print (Res)


main()
