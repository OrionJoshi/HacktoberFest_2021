def bissexto():

   ano = input('ano:')

   if ano%4==0:
       if ano%100==0:
           if ano%400==0:
               print 'bissexto'
           else:
               print 'nao bissexto'
       else:
           print 'bissexto'
   else:
       print 'nao bissexto'

if __name__=='__main__':
   bissexto()
