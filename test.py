from PYLINQ import PYLINQ
import ujson

def main():
    # a=PYLINQ([1,2,3,4,5]).where(lambda x:x>3).first()
    # print(a)
    mylist=[{"name":"卞辉","age":18,"size":41}
    ,{"name":"袁伟","age":2,"size":41}
    ,{"name":"赵雪峰","age":50,"size":41}
    ,{"name":"姜坤","age":18,"size":42}
    ,{"name":"国豪","age":2,"size":41}]
    a=PYLINQ(mylist).where(lambda x:x['age']>1).distinct(lambda t:t['age'])
    print(a)
    # print(ujson.dumps(a,ensure_ascii=False,indent=4))
    for item in a:
        print(ujson.dumps(item,ensure_ascii=False,indent=4))
       

if __name__ == "__main__":
    main()