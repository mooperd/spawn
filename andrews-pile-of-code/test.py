from pysphere import VIServer, MORTypes

s = VIServer()
s.connect("10.51.101.12", "aholway", "Carrot1")

#IF YOU ARE USING THE VERSION ON TRUNK DO
print s._get_managed_objects(MORTypes.Folder)

#IF YOU ARE USING THE LAST STABLE VERSION (0.1.6) DO
#it was a private method which is not private anymore in trunk
# print s._VIServer__get_managed_objects_dict(MORTypes.Folder, None)
