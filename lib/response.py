class ErrorResponse(Exception):
  """ Exception that can be raised by subclasses of `BaseEndpoint` which is caught
  by the view
  """
  
  def __init__(self, msg=None, data=None, code=400):
    self.msg = msg
    self.data = data
    self.code = code