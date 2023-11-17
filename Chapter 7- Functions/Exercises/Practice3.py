#prime or not

def is_prime(number):
    count=0
    for i in range(1,number+1):
        if number%i == 0:
          count +=1
    if count == 4:
       print('the number {0} is the prime number.'.format(number)) 
    else:
        print('the number {0} is  not the prime number.'.format(number))   

print(is_prime(2))             
