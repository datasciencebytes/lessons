# @datasciencebytes

# order a Python dict by val

my_dict = {'Apple': 1700,       # order: 1
           'Dell': 3100,        # order: 4
           'HP': 3000,          # order: 3
           'System76': 2200}    # order: 2

print(sorted(my_dict, key=my_dict.get))
