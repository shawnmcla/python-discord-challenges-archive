"""
Submission by Grote

Notes:
Only works for one operation
"""

lambda t, a={},v=lambda x:(y for y,z in enumerate(x) if z==' '):{*map(lambda b: b.strip().isdigit() and (a.update({len(a):b})or True)or b==" " or  a.update({len(a)-2:str(eval(f"{a.pop(len(a)-1)} {b} {a.pop(len(a)-1)}"))}),(t[a:b]for a,b in zip((0,*v(t)),(*v(t),len(t)))))} and a[0]
