import gc

def gc_collect():
    if not gc.isenabled():
        gc.enable()
    gc.collect(0)