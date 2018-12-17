from dateutil.parser import parse

def datestr2timestamp(d):
    """Convert a str date representation to its corresponding timestamp.
    
    Arguments:
        d {str} -- date representation 'DD-MM-AAAA hh:mm'
    
    Returns:
        float -- timestamp
    """
    return parse(d).timestamp()