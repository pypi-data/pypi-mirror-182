#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# This the EXUDYN module initialization file
#
# Author:   Johannes Gerstmayr
# Date:     2020-08-14
#
# Copyright:This file is part of Exudyn. Exudyn is free software. You can redistribute it and/or modify it under the terms of the Exudyn license. See 'LICENSE.txt' for more details.
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#This is a workaround to let users define the 'fast' track, 
#  avoiding range checks in exudyn (speedup may be 30% and more)
#  to activate the __FAST_EXUDYN_LINALG compiled version, use the 
#  following lines (must be done befor first import of exudyn);
#  Note that this is a hack and may be changed in future; it is only available for certain exudyn versions:
#import sys
#sys.exudynFast = True
#import exudyn

import sys
__useExudynFast = hasattr(sys, 'exudynFast')
if __useExudynFast:
    __useExudynFast = sys.exudynFast #could also be False!

__cpuHasAVX2 = hasattr(sys, 'exudynCPUhasAVX2')
if __cpuHasAVX2:
    __cpuHasAVX2 = sys.exudynCPUhasAVX2 #could also be False!

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#use numpy.core to find if AVX+AVX2 is available ...
try:
    from numpy.core._multiarray_umath import __cpu_features__
    if (('AVX' in __cpu_features__) and ('AVX2' in __cpu_features__)):
        if not __cpuHasAVX2 and hasattr(sys, 'exudynCPUhasAVX2'):
            print('WARNING: user deactivated AVX2 support, but support detected on current CPU')
        else:
            __cpuHasAVX2 = True
    elif __cpuHasAVX2:
        print('WARNING: user activated AVX2 support, but no AVX2 support has been detected on current CPU; may crash')
except:
    print('Warning: during import of exudyn, it was detected that either numpy or the numpy.core module "_multiarray_umath" is missing')

try:
    #for regular loading in installed python package
    if __useExudynFast and __cpuHasAVX2:
        try:
            from .exudynCPPfast import *
            print('Imported exudyn fast version without range checks')
        except:
            __useExudynFast = False
            print('Import of exudyn fast version failed; falling back to regular version')
    else:
        __useExudynFast = False #in case __useExudynFast=True but no AVX

    if not __useExudynFast:
        if __cpuHasAVX2:
            try:
                from .exudynCPP import *
            except:
                raise ImportError('Warning: Import of exudyn C++ module (with AVX2) failed; check your installation or try to import without VX by settings sys.exudynCPUhasAVX2=False')
        else:
            try:
                from .exudynCPPnoAVX import *
            except:
                raise ImportError('Import of exudyn C++ module (without AVX2) failed; non-AVX2 versions are only available in release versions (without .dev1 appendix); check your installation, Python version, conda environment and site-packages for exudyn; try re-installation')
            
except:
    #for run inside Visual Studio (exudynCPP lies in Release or Debug folders); no exudynFast! :
    try:
        from exudynCPP import *
    except:
        raise ImportError('Import of exudyn C++ module failed; check 32/64 bits versions, restart your iPython console or try to uninstall and install exudyn')

#import very useful solver functionality into exudyn module (==> available as exu.SolveStatic, etc.)
try:
    from .solver import SolveStatic, SolveDynamic, ComputeODE2Eigenvalues
except:
    #for run inside Visual Studio (exudynCPP lies in Release or Debug folders):
    from solver import SolveStatic, SolveDynamic, ComputeODE2Eigenvalues

# remove SolutionViewer as it makes problems if no tkinter or matplotlib installed
# try:
    # from .interactive import SolutionViewer
# except:
    # try:
        # #for run inside Visual Studio (exudynCPP lies in Release or Debug folders):
        # from interactive import SolutionViewer
    # except:
        # print("SolutionViewer not loaded (missing tkinter or matplotlib?)")
        # pass

__version__ = GetVersionString() #add __version__ to exudyn module ...


#add a functionality to check the current version
def RequireVersion(requiredVersionString):
    """
    Parameters
    ----------
    requiredVersionString : string
        Checks if the installed version is according to the required version.
        Major, micro and minor version must agree the required level.
    Returns
    -------
    None. But will raise RuntimeError, if required version is not met.

    Example
    ----------
    RequireVersion("1.0.26")

    """
    vExudyn=GetVersionString().split('.')
    vRequired = requiredVersionString.split('.')
    isOk = True
    if int(vExudyn[0]) < int(vRequired[0]):
        isOk = False
    elif int(vExudyn[0]) == int(vRequired[0]): #only for equal major versions
        if int(vExudyn[1]) < int(vRequired[1]): #check minor version
            isOk = False
        elif int(vExudyn[1]) == int(vRequired[1]): #only for equal minor versions
            if int(vExudyn[2]) < int(vRequired[2]): #check micro version
                isOk = False
    if not isOk:
        print("EXUDYN version "+requiredVersionString+" required, but only " + exu.GetVersionString() + " available")
        #raise RuntimeError("EXUDYN version "+requiredVersionString+" required, but only " + exu.GetVersionString() + "available")
    

#do not import itemInterface here, as it would go into exu. scope
#from .itemInterface import *


