from Basic.sampleClass import SampleClass
from Basic.sampleVoClass import SampleVO

from Basic import sampleClass
from Basic import sampleVoClass

'''
sample_1 = SampleClass()
sample_2 = SampleClass()

print("before : " + str(sample_1))
#print(sample_1.global_var_dict_data)        # AttributeError: 'SampleClass' object has no attribute 'global_var_dict_data'
#print(sample_1.global_var_list_data)        # AttributeError: 'SampleClass' object has no attribute 'global_var_list_data'
#print(SampleClass.global_var_dict_data)     # AttributeError: type object 'SampleClass' has no attribute 'global_var_dict_data'
#print(SampleClass.global_var_list_data)     # AttributeError: type object 'SampleClass' has no attribute 'global_var_list_data'
#print(sampleClass.global_var_dict_data)    # OK
#print(sampleClass.global_var_list_data)    # OK

sample_1.change_global_var()
sample_1.change_instance_var()
sample_1.change_local_var()
print("after : " + str(sample_1))
'''

'''
sample_1.create_vo()

sample_vo = SampleVO("id", "A-1234")
print(sample_vo)

sample_vo.set_global_var("SET_GLOBAL_DATA")
print(sample_vo.get_global_var())

sampleVoClass.global_vo_data = "Not Call Func Change Global Data"
print(sample_vo.get_global_var())

sample_vo.set_class_var("class var data")
print(sample_vo.get_class_var())

SampleVO.class_vo_data = "Not Call Func Change Class Data"
print(sample_vo.get_class_var())
'''

sample_1 = SampleClass()
sample_1.create_vo()

sampleClass.sample_vo_global = None
sample_1.create_vo()
