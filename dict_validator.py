
class ValiDict:
    
    def __init__(self,schema_dict):
        self.schema_dict = schema_dict
    
    def _evaluate(self, prop_dict, value):

            if prop_dict["type"] == str:
                min_len = prop_dict.get('min_len')
                max_len = prop_dict.get('max_len')

                if not isinstance(value, str):
                    return False

                if min_len and len(value) < min_len:
                    return False

                if max_len and len(value) > max_len:
                    return False
            
            if prop_dict["type"] == int:
                lt = prop_dict.get('lt')
                gt = prop_dict.get('gt')

                if not isinstance(value, int):
                    return False

                if lt and value > lt:
                    return False

                if gt and value < gt:
                    return False

            if prop_dict["type"] == bool:
                t_f = prop_dict['t/f']

                if not isinstance(value, bool):
                    return False

                if t_f and t_f != value:
                    return False
                
            return True

    def validate(self, vali_dict:dict):
        
        for key, val in vali_dict.items():
            prop_dict = self.schema_dict.get(key)
            print(prop_dict)
            if not prop_dict:
                return False

            if self._evaluate(prop_dict,val) == False:
                return False

        return True


schema_dict = {
    "name" : {
        "type":str,
        "min_len":2,
        "max_len":5
    },

    "age" : {
        "type": int,
        "gt": 3,
        "lt":38
    },

    "is_married":{
        "type":bool,
        "t/f":True
    }
}

my_dict = {
    "name" : "Kaus",
    "age" : 22,
    "is_married":True
}

v = ValiDict(schema_dict)
print(v.validate(my_dict))