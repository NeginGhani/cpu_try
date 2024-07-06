import class_core
from Components import memory

core = class_core.Core()
core.register_write({'AC': '0x3'})
core.memory_write({'address': '0xa', 'value': '0x1'})
istru = ['AND 0xa', 'STA 0xb', 'HLT']
core.compile(istru)
print("COMPILE DONE!")
print(core.memory_bulk_read())
core.execute_instruction()

