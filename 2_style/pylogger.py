# STYLE ***************************************************************************
# content     = assignment
#
# modified by = Elena Giuliani
#
# date        = 2025-10-20
# email       = contact@alexanderrichtertd.com
#************************************************************************************
# original: logging.init.py

def findCaller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    current_frame = currentframe()
    rv = "(unknown file)", 0, "(unknown function)"

    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.

    if current_frame:
        current_frame = current_frame.f_back


    while hasattr(current_frame, "f_code"):
        frame_code = current_frame.f_code
        filename = os.path.normcase(frame_code.co_filename)

        if filename == _srcfile:
            current_frame = current_frame.f_back
            continue
        
        rv = (frame_code.co_filename, current_frame.f_lineno, frame_code.co_name)
        break
    
    return rv


