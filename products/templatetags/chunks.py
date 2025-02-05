from django import template

register=template.Library()

@register.filter(name='chunks')
def chunks(lst, chunk_size):
    print('lstlstlst', lst)
    chunk = []
    i=0
    for x in lst:
        chunk.append(x)
        i+=1
        if i==chunk_size:
            yield chunk
            i=0
            chunk=[]
    if chunk:
        yield chunk
    
    