import re
def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string)
    if match is not None:
        h = match.group(1)
        m = match.group(2)
        s = match.group(3)
        ms = match.group(4) or ('.000')
        ms = ms[1:]
        return (int(h), int(m), int(s), int(ms))
    else:
        return None
    
 
        
        
    