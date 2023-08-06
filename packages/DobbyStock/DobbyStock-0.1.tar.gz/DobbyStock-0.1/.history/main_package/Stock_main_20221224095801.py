# stock main
# class for Stock
# contain the input for number of rounds to paly with
import random
class SizeError(Exception):
      def __init__(self):
            self.message = "Error: size must be a positive integer"

class Stock(object):
      def __init__(self):
            try:
                  size = int(input("How many round do you want to play with?"))
                  if size <= 0:
                        raise SizeError
                  self.n = int(size)
                  
                  print("You are going to play {} round, get ready!!!!!!!!\n".format(self.n))
                  self.high_price_list = [random.randint(201, 500) for i in range(int(self.n))]
                  self.low_price_list = [random.randint(50, 200) for i in range(int(self.n))]
                  self.volume_list = [random.randint(1, 200) for i in range(int(self.n))]
            except TypeError:
                  print("Error: size must be a numeric value")
            except ValueError:
                  print("Error: size must be a positive integer")
            except ZeroDivisionError:
                  print("Error: size cannot be zero")
            except Exception:
                  print("An unknown error occurred")
                  
      
      def get_high_price(self):
            try:
                  return self.high_price_list
            except AttributeError:
                  print("Error: high_price_list is not initialized")
            except Exception:
                  print("An unknown error occurred")
                  
      def get_low_price(self):
            try:
                  return self.low_price_list
            except AttributeError:
                  print("Error: low_price_list is not initialized")
            except Exception:
                  print("An unknown error occurred")
                  
      def get_volume(self):
            try:
                  return self.volume_list
            except AttributeError:
                  print("Error: volume_list is not initialized")
            except Exception:
                  print("An unknown error occurred")
                  
      def get_size(self):
            try:
                  return int(self.n)
            except AttributeError:
                  print("Error: n is not initialized")
            except Exception:
                  print("An unknown error occurred")
      
      def __str__(self):
            try:
                  print('high price list: {}','\nlow price list: {}','\nvolume list:{}'.format(self.high_price_list, self.low_price_list, self.volume_list))
                  # return f'high price list: {self.high_price_list}\nlow price list: {self.low_price_list}\nvolume list: {self.volume_list}'
            except AttributeError:
                  print("Error: high_price_list, low_price_list, or volume_list is not initialized")
            except TypeError:
                  print("Error: high_price_list, low_price_list, and volume_list must be lists")
            except ValueError:
                  print("Error: high_price_list, low_price_list, and volume_list must contain only integers")
            except Exception:
                  print("An unknown error occurred")  

