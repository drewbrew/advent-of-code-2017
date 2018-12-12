#!/usr/bin/env python

TEST_INPUT = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".split('\n')

TEST_REG_NAMES = set(i[0] for i in TEST_INPUT)

REAL_INPUT = """<paste inputs here>""".split('\n')

REAL_REG_NAMES = set(i.split()[0] for i in REAL_INPUT)


def process_instruction(instruction, registers):
    reg, oper, amount, dummy, comp_reg, comp_oper, comp_value = \
        instruction.split()
    amount = int(amount)
    comp_value = int(comp_value)
    source_value = registers[comp_reg]
    if comp_oper == '>' and source_value <= comp_value:
        return
    if comp_oper == '>=' and source_value < comp_value:
        return
    if comp_oper == '==' and source_value != comp_value:
        return
    if comp_oper == '!=' and source_value == comp_value:
        return
    if comp_oper == '<' and source_value >= comp_value:
        return
    if comp_oper == '<=' and source_value > comp_value:
        return
    # we're here, so the condition must be satisfied
    if oper == 'inc':
        registers[reg] += amount
    else:
        registers[reg] -= amount
    return registers[reg]


def part_one(instructions, register_names):
    registers = {i: 0 for i in register_names}
    for instruction in instructions:
        process_instruction(instruction, registers)
    return max(registers.values())


def part_two(instructions, register_names):
    registers = {i: 0 for i in register_names}
    max_value = 0
    for instruction in instructions:
        value_assigned = process_instruction(instruction, registers)
        if value_assigned is not None and value_assigned > max_value:
            max_value = value_assigned
    return max_value



if __name__ == '__main__':
    test_part_one = part_one(TEST_INPUT, TEST_REG_NAMES)
    assert test_part_one == 1, test_part_one
    print(part_one(REAL_INPUT, REAL_REG_NAMES))
    print(part_two(REAL_INPUT, REAL_REG_NAMES))
