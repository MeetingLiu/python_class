
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import math

UNCLASSIFIED = False
NOISE = -1


# In[19]:


# p=np.array([[m[0,0]],[m[1,0]]])
# q=np.array([[m[0,1]],[m[1,1]]])


# In[20]:


def _dist(p,q):
#     p=np.array([[m[0,i]],[m[1,i]]])[1,0]
#     q=np.array([[m[0,i]],[m[1,i]]])[1,0]
#     p=np.array([[m[0,3]],[m[1,3]]])
#     q=np.array([[m[0,0]],[m[1,0]]])
    d=((p[0,0]-q[0,0])**2+(p[1,0]-q[1,0])**2)**0.5
    return d

# _dist(p,q)


# In[21]:


def _eps_neighborhood(p,q,eps):
    d=_dist(p,q)
    if d.any() <= eps:
        return True
    elif d > eps:
        return False
# a=_eps_neighborhood(p,q,1.6)
# if a:
#     print('a')
# else:
#     print('b')


# In[22]:


# # point_id 已整理的array
# # p:假設為中心的點  q:與p做比較距離的點
# # seeds 
# # m 還沒被判斷或沒有cluster的點
# # cluster_id 判斷的cluster裡面有幾個點
# def _region_query(m, point_id, eps):
#     n_points = m.shape[1]
#     seeds = []
#     for point_id in range(n_points):
#         p=np.array([[m[0,point_id]],[m[1,point_id]]])
#         for point_id in range(n_points):
        
# #     p=np.array([[m[0,0]],[m[1,0]]])
#             q=np.array([[m[0,point_id]],[m[1,point_id]]])
#             if _eps_neighborhood(p,q,eps):
#                 seeds.append(q)

    
# #     for i in range(n_points):
# # #         p=np.array([[m[0,i]],[m[1,i]]])
# #         q=np.array([[m[0,i]],[m[1,i]]])
# #         go=_eps_neighborhood(p,q,eps)
# #         if go:
# #             seeds.append(q)
#     return seeds


# In[23]:


def _region_query(m, point_id, eps, classifications, cluster_id):
    n_points = m.shape[1]
    seeds = []
#     for point_id in range(n_points):
    p=np.array([[m[0,point_id]],[m[1,point_id]]])
#     classifications[point_id]=cluster_id
    for i in range(n_points):
        if classifications[i]==False:
            q=np.array([[m[0,i]],[m[1,i]]])
            inside=_eps_neighborhood(p,q,eps)
            if inside:
                classifications[i]=cluster_id
                seeds.append(i)
    return seeds


# In[24]:


# i=1
# np.array([[m[0,i]],[m[1,i]]])[1,0]


# In[25]:


# def _expand_cluster(m, classifications, point_id, cluster_id, eps, min_points, seeds):
# #     classifications[point_id]=cluster_id
# #     for p in seeds:
#         __seeds=[]
# #         point_id=p
#         __seeds=_region_query(m, point_id, eps, classifications, cluster_id)
        
#         seeds.append(__seeds)
# #         if len(__seeds)>=min_points:
# #             seeds.append(__seeds)
            
# #             return False

        


# In[26]:


def dbscan(m, eps, min_points):
    """Implementation of DBSCAN
    You can refer to wikipedia for detailed algorithm: https://en.wikipedia.org/wiki/DBSCAN
    Use Euclidean Distance as the measure
    
    Inputs:
    m - A matrix whose columns are feature vectors
    eps - Maximum distance two points can be to be regionally related
    min_points - The minimum number of points to make a cluster
    
    Outputs:
    An array with either a cluster id number or dbscan.NOISE (None) for each column vector in m
    """
    cluster_id = 1
    n_points = m.shape[1]
    classifications = [UNCLASSIFIED] * n_points
#     p=np.array([[m[0,0]],[m[1,0]]])
    
    for point_id in range(n_points):
        all_seeds=[]
        if classifications[point_id]!=False:
            continue
        elif classifications[point_id]==False:            
            seeds=_region_query(m, point_id, eps, classifications, cluster_id)
            

#             if len(seeds)<min_points:
                
            if len(seeds)<min_points:
                    classifications[point_id]=NOISE
            elif len(seeds)>=min_points:
                all_seeds.append(seeds)
                for i in all_seeds:
#                 core.append(seeds)
                    point_id=i
                    seeds=_region_query(m, point_id, eps, classifications, cluster_id)
#                     if len(seeds)<min_points:
                    if len(seeds)>=min_points:
                        all_seeds.append(seeds)
#                     while True:
#                     _expand_cluster(m, classifications, point_id, cluster_id, eps, min_points, seeds)
        cluster_id+=1
#             for c in seeds:
#                 p=c
#                 seeds=_region_query(m, point_id, eps)
            
    
            
            
            
#         cluster_id+=1
        
        
        
        
        
        
#         if classifications[point_id]==False:
            
#         for point_id in range(n_points):
#             q=np.array([[m[0,point_id]],[m[1,point_id]]])
#             if _eps_neighborhood(p,q,eps):
                
            
#         q=np.array([[m[0,i]],[m[1,i]]])[1,0]
#         seeds=_region_query(m, point_id, eps)
        
        
        #     core=_expand_cluster(m, classifications, point_id, cluster_id, eps, min_points)
    
    # the main dbscan algorithm
    # put your code here
    
    return classifications


# In[27]:


# # test here
# dataset_1 = pd.read_csv("C:\Python 3.7\\blobs.csv")[:80].values
# m = np.asmatrix(dataset_1)
# m = m.transpose()
# m
# # p=np.array([[m[0,2]],[m[1,2]]])
# # p[1,0]
# i=0
# point_id=
# p=np.array([[m[0,i]],[m[1,i]]])[1,0]
# point_id
# p
# np.array([[m[0,i]],[m[1,i]]])
# # m.shape[1]
# # m.shape


# In[28]:


# np.array([[m[0,i]],[m[1,i]]])[0,0]


# In[29]:


# eps = 1.6
# min_points = 5
# a = dbscan(m, eps, min_points)


# In[30]:


# cluster=np.array([[0,0]])
# cluster=np.append(cluster,[[1,1]],axis=0)
# cluster


# In[31]:


# test here
dataset_1 = pd.read_csv("C:\Python 3.7\\blobs.csv")[:80].values
m = np.asmatrix(dataset_1)
m = m.transpose()


# In[32]:


eps = 1.6
min_points = 5
a = dbscan(m, eps, min_points)


# In[53]:


get_ipython().run_line_magic('matplotlib', 'inline')
import __dbscan_lab_helper__ as helper

result = np.asarray(a)
helper.plot_clustered_dataset(dataset_1, result, neighborhood=True, epsilon=eps)

