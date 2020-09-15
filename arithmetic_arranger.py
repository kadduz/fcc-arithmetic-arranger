def arithmetic_arranger(problems, show_answers = False):
  MAX_NUM_LEN = 4
  MAX_OPERATIONS = 5
  MAX_OPERANDS = 3
  OPERAND_ADMITTED = ['+','-']

  class MathOper:
    def __init__(self, num1, num2, operand):
      self.num1 = int(num1)
      self.num2 = int(num2) 
      self.operand = operand
      
    def result(self):
      if self.operand == '+':
        return self.num1 + self.num2
      elif self.operand == '-':
        return self.num1 - self.num2

    def arrange(self, show_answers=show_answers):
      l = max(len(str(self.num1)), len(str(self.num2)))
      arranged = ['  {n:' '>{l}}'.format(n=self.num1, l=l), \
          '{o} {n:' '>{l}}'.format(n=self.num2, l=l, o=self.operand), (2+l)*'-']
      if show_answers:
        n = self.result()
        if n >= 0:
          arranged.append('  {n:' '>{l}}'.format(n=n, l=l))
        else:
          arranged.append(' {n:' '>{l}}'.format(n=n, l=l))
      return arranged
  
  operations = []
  if len(problems) > MAX_OPERATIONS:
    return "Error: Too many problems."

  for problem in problems:
    operands= problem.split(' ') 
    if len(operands) > MAX_OPERANDS:
      return "Error: Too many operands."
    elif (not operands[0].isdigit()) or (not operands[2].isdigit()):
      return "Error: Numbers must only contain digits."
    elif len(str(operands[0])) > MAX_NUM_LEN \
      or len(str(operands[2])) > MAX_NUM_LEN:
      return "Error: Numbers cannot be more than four digits."
    elif operands[1] not in OPERAND_ADMITTED:
      return "Error: Operator must be '+' or '-'."
    operations.append(MathOper(operands[0], operands[2], operands[1]))

  list_string = ['','','']
  if show_answers:
    list_string.append('')
  for i in range(len(operations)):
    problem = operations[i].arrange()
    for j in range(len(problem)):
      if i > 0:
        list_string[j] += '    '
      list_string[j] += problem[j] 

  return '\n'.join(list_string)
