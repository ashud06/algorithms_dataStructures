def sort_towers(num,src=2,dst=3):
    if num:
        #print("num:{0}".format(num))
        #print("src:{0}".format(src))
        #print("dst:{0}".format(dst))
        sort_towers(num-1,src,6-src-dst)
        try:
            print('moved disk number {0} from src {1} to dst {2}'.format(num,src,dst))
        except:
            pass
        sort_towers(num-1,6-src-dst,dst)

sort_towers(3)