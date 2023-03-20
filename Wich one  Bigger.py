while True:
    
    A=float(eval(input("Enter A (Number) ")))
    B=float(eval(input("Enter B (Number) ")))
    C=float(eval(input("Enter C (Number) ")))

    if (A==B==C):
        print("ABC are Equal")
    else:
        if(A==B):
            if(A>C):
                print("A and B are the biggest numbers and equal")
                print("C is the second biggest number")
            else:
                print("C is the biggest number")
                print("A and B are the equal and the second biggest numbers")
        else:
            if(A==C):
                if(A>B):
                    print("A and C are the biggest numbers and equal")
                    print("B is the second biggest number")
                else:
                    print("B is the biggest number")
                    print("A and C are equal and the second biggest numbers")
                    
            else:
                if(B==C):
                    if(B>A):
                        print("B and C are the biggest numbers and equal")
                        print("A is the second biggest number")
                    else:
                        print("A is the biggest number")
                        print("B and C are equal and the second biggest numbers")

                else:
                    if(A>B and A>C):
                        print("A is the biggest number")
                        if(B>C):
                            print("B is the second biggest number")
                            print("C is the third biggest number")
                        else:
                            print("C is the second biggest number")
                            print("B is the third biggest number")
                            
                    else:
                        if(B>A and B>C):
                            print("B is the biggest number")
                            if(A>C):
                                print("A is the second biggest number")
                                print("C is the third biggest number")
                            else:
                                print("C is the second biggest number")
                                print("A is the third biggest number")
                        else:
                            print("C is the biggest number")
                            if(A>B):
                                print("A is the second biggest number")
                                print("B is the third biggest number")
                            else:
                                print("B is the second biggest number")
                                print("A is the third biggest number")
                            

    answer = input("Do you want to repeat? (y/n): ")
    if answer.lower() != "y":
        break

                
