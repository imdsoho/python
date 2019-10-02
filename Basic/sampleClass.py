from Basic.sampleVoClass import SampleVO

global_var_dict_data = dict()
global_var_list_data = []

sample_vo_global = SampleVO("id", "G-1111")

class SampleClass:
    class_var_str = "class_var_str"
    sample_vo_class = SampleVO("id", "L-2222")

    def __init__(self):
        self.instance_var_str = "_blank"
        self.instance_var_int = 0

    def __str__(self):
        return self.instance_var_str + " : " + str(self.instance_var_int)

    def change_global_var(self):
        global_var_dict_data = {'chang': 'global dict var'}
        global_var_list_data.append("change global list var")

        print (global_var_dict_data)
        print (global_var_list_data)

    def change_instance_var(self):
        self.instance_var_str = "change instance var"
        self.instance_var_int = 10

        print (self.instance_var_str)
        print (self.instance_var_int)

    def set_local_var(self):
        local_var_str = "local var"
        print(local_var_str)

    def change_local_var(self):
        self.set_local_var()
        #print(local_var_str)    # ERROR

    def create_vo(self):
        print("global instance used : ")
        print(type(sample_vo_global))
        print(sample_vo_global.get_dict())
        print(SampleClass.sample_vo_class.get_dict())

