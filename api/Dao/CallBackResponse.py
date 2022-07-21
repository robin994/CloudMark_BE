from api.Model.CallBackResponseModel import CallBackResponseModel

class CallBackResponse:
       
    @staticmethod
    def success(response, description = None): 
        return CallBackResponse.genericResponse(res = response, lenght=response, error= None, description = description )
    
    @staticmethod
    def error(error_message): 
        return CallBackResponse.genericResponse(res= None, lenght=None, error= "ERROR", description = error_message )
    
    @staticmethod
    def bad_request(error_message , description): 
        return CallBackResponse.genericResponse(res= None, lenght=None, error= "BAD REQUEST", description = error_message )
    
    @staticmethod
    def genericResponse(res=None, lenght=0, error= None, description = None):
        return CallBackResponseModel(
            data = res,
            lenght = len(lenght),
            error = error,
            description = description
        )
