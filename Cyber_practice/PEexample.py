# Didatic Example on how to classify PE files as malware vs. goodware

import sys              # Read argv. You can read from file too.
import pefile           # lib to parse PE file. Change lib to parse ELF
from sklearn import svm # Some ML classifier, you can change it
import os
import IPython
import pickle

##################################################################################################################################


# Receive [goodware, malware, and unknown file] as argument
gw_train = sys.argv[1]
mw_train = sys.argv[2]
unknown  = sys.argv[3]

##################################################################################################################################

# Parse goodware file
# I'm considering only one to be didactic
# In real world, you should consider multiple files in a loop
# Study task: Consider multiple files

# pe1=pefile.PE(gw_train) # example of parsing PE file
# sys.argv[1] is a string


for file in os.listdir(sys.argv[1]):   # method in python is used to get the list of all files and directories in the specified directory
    pe1=pefile.PE(gw_train)
    pe_gw_imps = len(pe1.DIRECTORY_ENTRY_IMPORT)
    # idx+=1


# Number of imports (libraries) as feature
# Single feature to be didcatice
# in real world, use a vector of features
# Study task: Consider multiple features!
pe_gw_imps = len(pe1.DIRECTORY_ENTRY_IMPORT)

# open the file with ipython?
# need to find more features






############################################################################################################################################################
# Do the same for the malware file
# pe2=pefile.PE(mw_train)
# pe_mw_imps = len(pe2.DIRECTORY_ENTRY_IMPORT)

for file in os.listdir(sys.argv[2]):   # method in python is used to get the list of all files and directories in the specified directory
    pe2=pefile.PE(mw_train)
    pe_mw_imps = len(pe2.DIRECTORY_ENTRY_IMPORT)





##################################################################################################################################
# Create vectors to be classified
# Feature in X. Labels in Y
# X = [[pe_gw_imps],[pe_mw_imps]]
X = [pe_gw_imps + pe_mw_imps]

# 0=goodware, 1=malware
# Y = [0,1]
# Y = [0,0,0,1] # create a loop to make this // based on actual num of gw and mw
# Y = [0] * idx_gw + [1] * idx_mw
Y = [0] * idx_gw + [1] * idx_mw

# # Instantiate a classifier and train it with the vectors
clf = svm.SVC()
clf.fit(X, Y) # x is all features and Y are all labels

# Now parse the unknown file
# pe3=pefile.PE(unknown)


for file in os.listdir(sys.argv[3]):
    pe3=pefile.PE(unknown)
    pe_ukn_imps = len(pe3.DIRECTORY_ENTRY_IMPORT)
    # ask classifier if unknown is malware or goodware
    res = int(clf.predict([[pe_ukn_imps]]))
    # Instead of printing 0 or 1, print name
    label_map = ["goodware","malware"]
    print(label_map[res])

# pe_ukn_imps = len(pe3.DIRECTORY_ENTRY_IMPORT)

# # Ask classifier if unknown is malware or goodware
# res = int(clf.predict([[pe_ukn_imps]]))

# Instead of printing 0 or 1, print name
# label_map = ["goodware","malware"]
# print(label_map[res])


######################################################

# pickle.dump(clf, myfile)




# run file `python filename.py gw/file1.exe mw/file2.exe unknown/file3.exe`  

# python3
# >> import pefile OR import IPython **
# >> IPython.embed()
# >> pefile.###opens up a list of stuff to access