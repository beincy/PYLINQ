from PYLINQ import PYLINQ


def main():
    # a=PYLINQ([1,2,3,4,5]).where(lambda x:x>3).first()
    # print(a)
    
    a=PYLINQ([1,2,3,4,5]).where(lambda x:x>2).where(lambda x:x>3)
   
    count=0
    for _ in a:
        count+=1
    print(count)
    count=0
    for _ in a:
        count+=1
    print(count)

if __name__ == "__main__":
    main()