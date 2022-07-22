from api.Model.CallBackResponseModel import CallBackResponseModel

class CallBackResponse:
       
    @staticmethod
    def success(response, description = None): 
        return CallBackResponse.genericResponse(res = response, status= "SUCCESS", description = description )
    
    @staticmethod
    def error(error_message = ''): 
        return CallBackResponse.genericResponse(res= None, status= "ERROR", description = error_message )
    
    @staticmethod
    def bad_request(error_message = ''): 
        return CallBackResponse.genericResponse(res= None, status= "BAD REQUEST", description = error_message )
    
    @staticmethod
    def genericResponse(res=None, status= None, description = None):
        return CallBackResponseModel(
            data = res,
            length = len(res) if hasattr(res,'__len__') else None ,
            status = status,
            description = description
        )
