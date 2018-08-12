# def handle(func, success, failure, exception1, exception2, exception3, exception4):
#     # Handle an exception without using try except
#     try:
#         success(func, func())
#     except exception1:
#         failure(func, exception1)
#     except exception2:
#         failure(func, exception2)
#     except exception3:
#         failure(func, exception3)
#     except exception4:
#         failure(func, exception4)
#     except:
#         raise
def handle(func, success, failure, exc):
    def success():
        return 'success'
    
    def failure():
        return 'failure'
    
    return success()
