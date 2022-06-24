import numpy as np
import random
import itertools
import pandas as pd

parasites = pd.Series(['parasites','noparasites'], name='parasites')
env = pd.Series(['resource4task4','resource4task8','resource4task12','resource4task16','resource4task20','resource1task4','resource1task8','resource1task12','resource1task16','resource1task20','resource10task20','resource20task20'], name='env')
rep = pd.Series(['1','2','3','4','5','6','7','8','9','10'], name='rep')
df = pd.DataFrame(list(itertools.product(env,mu,rep)),columns=['parasites','env','rep'])

for index, row in df.iterrows():
	parasites = row['parasites']
	env = row['env']
	rep = row['rep']
	print index
	print env
	print mu
	print rep
	f = open("configs/event_{0}_{1}_{2}.cfg".format(parasites,env,rep), "w")
    if parasites == 'parasites':
		f.write("u begin LoadPopulation {0}_{1}_{2}_detail-300000.spop \nu 5000 InjectParasite parasite-smt.org ABB 0 400 \nu 0:100:end PrintHost PhenotypeData \nu 0:100:end PrintParasitePhenotypeData \nu u:100:end PrintHostTasksData \nu 0:100:end PrintParasiteTasksData \nu 1000:100:end DumpParasiteTaskGrid \nu 1000:100:end DumpHostTaskGrid \nu 0:100:end PrintParasiteData ParasiteData.dat \nu 0:100:end PrintAverageData \nu 0:100:end PrintTasksData \nu 0:100:end PrintCountData \nu 0:100:end PrintDominantData \nu 0:100:end PrintResourceData \nu 50000:50000:end SavePopulation \nu 300000 Exit \n".format(parasites,env,rep))
    else:
   		f.write("u begin LoadPopulation {0}_{1}_{2}_detail-300000.spop \nu 0:100:end PrintHost PhenotypeData \nu 0:100:end PrintParasitePhenotypeData \nu u:100:end PrintHostTasksData \nu 0:100:end PrintParasiteTasksData \nu 1000:100:end DumpParasiteTaskGrid \nu 1000:100:end DumpHostTaskGrid \nu 0:100:end PrintParasiteData ParasiteData.dat \nu 0:100:end PrintAverageData \nu 0:100:end PrintTasksData \nu 0:100:end PrintCountData \nu 0:100:end PrintDominantData \nu 0:100:end PrintResourceData \nu 50000:50000:end SavePopulation \nu 300000 Exit \n".format(parasites,env,rep))


