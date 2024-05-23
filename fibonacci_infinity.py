#  #using iterator
#  class FibonacciIterator:
#      def __init__(self):
#          self.current, self.next = 0, 1
# 
#      def __iter__(self):
#          return self
# 
#      def __next__(self):
#          fibonacci_number = self.current
#          self.current, self.next = self.next, self.current + self.next
#          return fibonacci_number
# 
# 
# 
# 
#  #using generator
#  def generate_fibonacci():
#      current, next_value = 0, 1
#      while True:
#          yield current
#          current, next_value = next_value, current + next_value
# 
#
#
#
# #example for .throw()
# class Stop(Exception):
#     pass
#
# def num_gen():
#     try:
#         n = 0
#         while True:
#             yield n
#             n += 1
#     except Stop:
#         print("Stopped")
#
# gen = num_gen()
# print(next(gen))
# print(next(gen))
# gen.throw(Stop)
#
#
# #example for .send()
# def accumulator():
#     total = 0
#     while True:
#         value = yield total
#         if value is not None:
#             total += value
#
# gen = accumulator()
# print(next(gen))
# print(gen.send(15))
# print(gen.send(10))
# print(gen.send(-4))
#
#
# #example for .close
# def countdown(n):
#     try:
#         while n > 0:
#             yield n
#             n -= 1
#     except GeneratorExit:
#         print("Stopped countdown.")
#
# gen = countdown(3)
#
# for num in gen:
#     print(num)
#
# gen.close()


