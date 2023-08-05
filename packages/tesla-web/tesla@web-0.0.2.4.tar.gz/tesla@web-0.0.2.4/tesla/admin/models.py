
from tesla.auth.modal import UserBaseModal
from tesla.modal import Model
from dataclasses import dataclass
            
            
@dataclass
class User(UserBaseModal):
    
    @classmethod
    def __meta__(self):
        
        return ('id', 'username', 'email')