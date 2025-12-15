from typing import List


def normalize_num(dial):
    if dial >= 100:
        dial = dial - 100
        return normalize_num(dial)
    elif dial < 0:
        dial = 100 + dial
        return normalize_num(dial)
    else:
        return dial


def rotate_left(instr, current_dial):
    rotated_num = current_dial - int(instr.lstrip("L"))
    current_dial = normalize_num(rotated_num)
    return current_dial


def rotate_right(instr, current_dial):
    rotated_num = current_dial + int(instr.lstrip("R"))
    current_dial = normalize_num(rotated_num)
    return current_dial


def read_instruction(file_path: str) -> List[str]:
    instructions = []
    with open(file_path, "r") as f:
        for i in f:
            instructions.append(i.strip())
    return instructions


def main():
    # initiate password sequence & current dial point
    password = 0
    current_point = 50
    instructions_list = read_instruction("./01_input.txt")
    for instruction in instructions_list:
        if "L" in instruction:
            current_point = rotate_left(instruction, current_dial=current_point)
            if current_point == 0:
                password += 1
        elif "R" in instruction:
            current_point = rotate_right(instruction, current_dial=current_point)
            if current_point == 0:
                password += 1
        else:
            raise f"Unrecognized instruction: {instruction}"
        print(f"Instruction: {instruction} - current point: {current_point}\n")
    return password


if __name__ == "__main__":
    print(main())
