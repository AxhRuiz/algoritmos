from typing import Any, Optional
import json
class List(list):
    CRITERION_FUNCTIONS={}
    
    def add_criterion(self, key_criterion:str,function):
        self.CRITERION_FUNCTIONS[key_criterion]=function
    
    def show(self)->None:
        if self and  isinstance(self[0], dict):
            for element in self:
                print(json.dumps(element, indent =4, ensure_ascii=False))
        else:
            print(list(self))
    
    def delete_value(self,value,key_value: str=None)-> Optional[Any]:
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index
    
    def sort_by_criterion(self,criterion_key: str=None)-> None:
        criterion= self.CRITERION_FUNCTIONS.get(criterion_key)
        
        if criterion is not None:
            self.sort(key=criterion)
        elif self and isinstance(self[0], (int,str,bool)):
            self.sort()
        else:
            print('Criterio de orden no encontrado')
    
    def search(self, search_value,search_key: str=None)-> int:
        self.sort_by_criterion(search_key)
        start=0
        end=len(self)-1
        middle= (start+end) //2
        
        while start <= end:
            criterion =self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], int,str,bool):
                return None
            value=criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value < search_value:
                start = middle+1
            else:
                end= middle-1
            middle=(start+end)//2
                