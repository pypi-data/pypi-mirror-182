# Patches: CairoFunctionRunner
def CairoFunctionRunner(program, layout):
    runner = cairo_rs_py.CairoRunner(program=program.dumps(), entrypoint=None, layout=layout, proof_mode=False)
    runner.initialize_function_runner()
    return runner

# Patches: syscall_handler._allocate_segment
def allocate_segment(segments, data):
    pass
