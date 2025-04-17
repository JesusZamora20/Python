class Phone:
  def __init__(self):
    pass

  def call(self):
    print("calling...")

  def busy(self):
    print("busy..")

  def message(self):
    print("messaging...")

class Camera:
  def __init__(self):
    pass

  def photo(self):
    print("taking picture...")

class Media:
  def __init__(self):
    pass

  def Playmusic(self):
    print("playing music...")
    
  def Playvideo(self):
    print("playing video...")

class Smartphone(Phone, Camera, Media):
  def __del__(self):
    print("phone off")

phone = Smartphone()
# print(dir(phone))
print(phone.Playmusic())
print(phone.call())











    
