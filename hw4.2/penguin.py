
penguin = """
   _~_
  (o o)
 /  V  \\
/(  _  )\\
  ^^ ^^
"""

n = int(input())

penguin_parts = penguin.split('\n')
width = max((len(x) for x in penguin_parts)) +2

for part in penguin_parts:
    print(f'{part:{width}}'*n)