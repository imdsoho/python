from dataServiceESImpl import DataObjectESServiceImpl
from dataServiceDBImpl import DataObjectDBServiceImpl
from instance_factory import getInstance

es_data = getInstance(DataObjectESServiceImpl)
print(es_data.get_data())

#db_data = getInstance(DataObjectDBServiceImpl)
#print(db_data.get_data())
