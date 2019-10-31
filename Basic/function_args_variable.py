import copy

org_dict_var = {'1':'A', '2':'B', '3':'C'}
org_list_var = ['A', 'B', 'C']
org_tup_var = ('A', 'B', 'C')
org_str_var = 'ORIGIN'
org_int_var = 1234567890

class ClassVar():
    def __init__(self):
        self.cls_dict_var = {}
        self.cls_list_var = []
        self.cls_tup_var = ()
        self.cls_str_var = ""
        self.cls_int_var = 0

    def __str__(self):
        return "\n\t CLASS VAR \n\t [DICT] {0}, \n\t [LIST] {1}, \n\t [TUP] {2}, \n\t [STR] {3}, \n\t [INT] {4}".format(self.cls_dict_var, self.cls_list_var, self.cls_tup_var, self.cls_str_var, self.cls_int_var)

org_cls_var = ClassVar()

def args_value_copy(dict_param, list_param, tup_param, str_param, int_param, cls_param):
    dict_param_copy = dict_param.copy()
    list_param_copy = list_param.copy()
    tup_param_copy = tuple(tup_param)
    str_param_copy = str_param
    int_param_vopy = int_param
    #cls_param_copy = copy.copy(cls_param)
    cls_param_copy = copy.deepcopy(cls_param)

    dict_param_copy['1'] = '1'
    list_param_copy[0] = '1'
    #tup_param[0] = '1'      # tuple not change
    str_param_copy = 'CHANGE'
    int_param_copy = 987654321
    cls_param_copy.cls_dict_var['1'] = 'A'
    cls_param_copy.cls_list_var.append('A')
    #cls_param.cls_tup_var['1'] = 'A'
    cls_param_copy.cls_str_var = 'CLASS VAR CHANGE'
    cls_param_copy.cls_int_var = 777

def args_value_change(dict_param, list_param, tup_param, str_param, int_param, cls_param):
    dict_param['1'] = '1'
    list_param[0] = '1'
    #tup_param[0] = '1'      # tuple not change
    str_param = 'CHANGE'
    int_param = 987654321
    cls_param.cls_dict_var['1'] = 'A'
    cls_param.cls_list_var.append('A')
    #cls_param.cls_tup_var['1'] = 'A'
    cls_param.cls_str_var = 'CLASS VAR CHANGE'
    cls_param.cls_int_var = 999

print("BEFORE CALL FUNCTION \n [DICT] {0}, \n [LIST] {1}, \n [TUP] {2}, \n [STR] {3}, \n [INT] {4}, \n [CLS] {5}".format(org_dict_var, org_list_var, org_tup_var, org_str_var, org_int_var, org_cls_var))
print("----------------------------------")

args_value_copy(org_dict_var, org_list_var, org_tup_var, org_str_var, org_int_var, org_cls_var)
print("COPY CHANGE FUNCTION \n [DICT] {0}, \n [LIST] {1}, \n [TUP] {2}, \n [STR] {3}, \n [INT] {4}, \n [CLS] {5}".format(org_dict_var, org_list_var, org_tup_var, org_str_var, org_int_var, org_cls_var))
print("----------------------------------")

args_value_change(org_dict_var, org_list_var, org_tup_var, org_str_var, org_int_var, org_cls_var)
print("VALUE CHANGE FUNCTION \n [DICT] {0}, \n [LIST] {1}, \n [TUP] {2}, \n [STR] {3}, \n [INT] {4}, \n [CLS] {5}".format(org_dict_var, org_list_var, org_tup_var, org_str_var, org_int_var, org_cls_var))
print("----------------------------------")
