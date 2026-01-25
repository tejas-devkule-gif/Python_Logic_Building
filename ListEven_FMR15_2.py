# write a lambda function using filter() which accepts a list of numbers and return a list of even numbers.

def main():
    
    #L1=[10,20,30,40,50]
    L1=list(map(int,input("Enter numbers :").split()))   #.split() → splits string by spaces
    print(L1)                                            # map(int, ...) → converts each string to integer
                                                         # list() → converts result into a list
    FData=list(filter(lambda No:No%2==0,L1))
    print("The list of even no is :",FData)
    
    MData=list(map(lambda No:No%2==0,L1))
    print("The list of even no is :",MData)

if __name__=="__main__":
    main()