from multiprocessing.dummy import Pool

import time

work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])


def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    print(" Process %s Finished." % work_data[0])
    

    
def without_pool(work_data):
    start = time.time()
    for data in work_data:
        print(" Process %s waiting %s seconds" % (data[0], data[1]))
        print(" Process %s Finished." % data[0])
        
    end = time.time()
    print(end-start)
    
def with_pool(work_data):
    start = time.time()
    
    with Pool(10) as p:
        p.map(work_log, work_data)
    end = time.time()
    
    