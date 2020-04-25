def getVal(A,i,j,rmax,colmax):
    if i<0 or j<0 or i>=rmax or j>=colmax:
        return 0
    else:
        return A[i][j]

def findMaxRegion(A,i,j,rmax,colmax):
    global maxsize
    global size
    global cntarr
    cntarr[i][j] = 1
    size+=1
    if size>maxsize:
        maxsize=size
        print("Maxsize updated to: {0}".format(maxsize))
    #print(cntarr)

    direction=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for k in range(0,8):
        newi = i + direction[k][0]
        newj = j+direction[k][1]
        if getVal(A,newi,newj,rmax,colmax)>0 and cntarr[newi][newj]==0:
            findMaxRegion(A,newi,newj,rmax,colmax)
    cntarr[i][j] = 0

def findMax(A,rmax,colmax):
    global maxsize
    global size
    global cntarr
    for i in range(0,rmax):
        for j in range(0,colmax):
            size=0
            if getVal(A,i,j,rmax,colmax)>0:
                cntarr = [[0] * rmax for i in range(colmax)]
                findMaxRegion(A, i, j, rmax, colmax)
    return maxsize







#zarr=[[1,1,0,0,0],[0,1,1,0,1],[0,0,0,1,1],[1,0,0,1,1],[0,1,0,1,1]]
zarr=[[1,1,0,0,0],[0,1,1,0,1],[0,0,1,0,1],[1,0,0,0,1],[0,1,0,1,1]]
rmax=5
colmax=5
maxsize=0
size=0
cntarr=[[0] * rmax for i in range(colmax)]
print("Number of maximum 1s are:")
print(findMax(zarr,rmax,colmax))
