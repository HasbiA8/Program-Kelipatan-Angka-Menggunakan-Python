def seto(n):
  result = []
  for x in range(1, n+1):
    if x % 3 == 0 and x % 5 == 0:
      result.append("se to")
    elif x % 3 == 0:
      result.append('se')
    elif x % 5 == 0:
      result.append('to')
    else:
      result.append(str(x))
  return result
def main():
  print(', '.join(seto(100)))
main()