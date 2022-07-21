from api.Model.CallBackResponseModel import CallBackResponseModel

class CallBackResponse:
       
    @staticmethod
    def success(response, description = None): 
        return CallBackResponse.genericResponse(res = response, error= None, description = description )
    
    @staticmethod
    def error(error_message = ''): 
        return CallBackResponse.genericResponse(res= None, error= "ERROR", description = error_message )
    
    @staticmethod
    def bad_request(error_message = ''): 
        return CallBackResponse.genericResponse(res= None, error= "BAD REQUEST", description = error_message )
    
    @staticmethod
    def genericResponse(res=None, error= None, description = None):
        return CallBackResponseModel(
            data = res,
            lenght = len(res) if hasattr(res,'__len__') else 1,
            error = error,
            description = description
        )
