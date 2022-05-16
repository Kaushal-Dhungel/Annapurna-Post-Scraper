class ValiDict:
    
    def __init__(self,schema_dict):
        self.schema_dict = schema_dict
        self.required = []
        for key,val in schema_dict.items():
            if val.get('required') == True:
                self.required.append(key)

    def _evaluate(self, prop_dict, value):
        data_type = prop_dict.get('type')

        if data_type != type(value):  
            return False

        if data_type == str or data_type == int:

            min_val = prop_dict.get('min_len' if data_type == str else 'gt')
            max_val = prop_dict.get('max_len' if data_type == str else 'lt')
            compare_val = len(value) if data_type == str else value

            if min_val and compare_val < min_val:
                return False

            if max_val and compare_val > max_val:
                return False        

        if data_type == bool:
            t_f = prop_dict['t/f']
            if t_f and t_f != value:
                return False
                
        return True

    def validate(self, vali_dict:dict):
        
        for key, val in vali_dict.items():

            if key in self.required:
                self.required.remove(key)

            prop_dict = self.schema_dict.get(key)

            if prop_dict is not None:
                if self._evaluate(prop_dict,val) == False:
                    return False

        if self.required == []:
            return True

        return False



schema_dict = {
    "name" : {
        "type":str,
        "min_len":2,
        "max_len":8,
        "required" : True
    },

    "age" : {
        "type": int,
        "gt": 3,
        "lt":38,
        "required" : False

    },

    "is_married":{
        "type":bool,
        "t/f":True
    },
}

my_dict = {
    "name" : "Kaus",
    "age" : 22,
    "is_married":True,
    "my_list":[1,2,3]
}

v = ValiDict(schema_dict)
print(v.validate(my_dict))