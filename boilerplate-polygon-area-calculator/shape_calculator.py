class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
     self.width = width

  def set_height(self, height):
     self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture(self):
    shape = ''
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      for _ in range(self.height):
        shape = shape + ('*' * (self.width)) + '\n'
      return shape
      
  def get_amount_inside(self, shape):
    fit_shape_count = self.get_area()//shape.get_area()
    return fit_shape_count
    
  def __str__(self):
    return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.__init__(side)
    return self.__str__()

  def set_width(self, side):
    self.__init__(side)

  def set_height(self, side):
    self.__init__(side)

  def __str__(self):
    return f"{self.__class__.__name__}(side={self.width})"