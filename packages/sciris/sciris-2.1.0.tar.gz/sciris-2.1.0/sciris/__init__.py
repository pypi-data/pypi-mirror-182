"""
Sciris root module

Functions in Sciris are of course organized into submodules. However, standard
usage is to call the functions directly, e.g. ``sc.parallelize()`` instead
of ``sc.sc_parallel.parallelize()``.
"""

# Optionally allow lazy loading
import os as _os
_lazy = _os.getenv('SCIRIS_LAZY', False)

# Otherwise, import everything
if not _lazy:
    from .sc_version   import *
    from .sc_utils     import *
    from .sc_printing  import *
    from .sc_nested    import *
    from .sc_odict     import *
    from .sc_settings  import *
    from .sc_datetime  import *
    from .sc_math      import *
    from .sc_dataframe import *
    from .sc_fileio    import *
    from .sc_profiling import *
    from .sc_parallel  import *
    from .sc_asd       import *
    from .sc_plotting  import *
    from .sc_colors    import *

del _os, _lazy
