import csv

def automation_rule(rules):
    while True:
        cells = int(input("Amount of cells: "))
        if cells > 2:
            break
        print("wrong amount of cells")
    while True:
        generations = int(input("Amount of generations: "))
        if generations > 0:
            break
        print("wrong amount of generations")
    while True:
        boundary_condition = int(input("Boundary_condition (None - 0, Periodic - 1, Absorptive - 2): "))
        if -1 <boundary_condition < 3:
            break
        print("wrong boundary condition")
    with open('cellular_automaton.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Generation", "Cell States"])
        
        for num in rules:
            if num > 255:
                print("rules is out of range")
            else:
                writer.writerow([" "," "])
                print(num)
                rule_bin = format(num, '08b')
                print(rule_bin + "\n")
                current_generation = [0] * cells
                current_generation[cells//2] = 1
                for generation in range(generations):
                    writer.writerow([generation, "".join(map(str, current_generation))])
                    print("".join(map(str, current_generation)))
                    next_generation = [0] * cells

                    if boundary_condition == 0:
                        for i in range(1, cells - 1):
                            pattern = int("".join(map(str, current_generation[i - 1:i + 2])), 2)
                            next_generation[i] = int(rule_bin[7 - pattern])

                        current_generation = next_generation
                    elif boundary_condition == 1:
                        for i in range(cells):
                            left_neighbor = current_generation[(i - 1) % cells]
                            right_neighbor = current_generation[(i + 1) % cells]
                            pattern = int(f"{left_neighbor}{current_generation[i]}{right_neighbor}", 2)
                            next_generation[i] = int(rule_bin[7 - pattern])
                        current_generation = next_generation
                    elif boundary_condition == 2:
                        for i in range(cells):
                            if i == 0 or i == cells - 1:
                                left_neighbor = 0
                                right_neighbor = 0
                            else:
                                left_neighbor = current_generation[i - 1] 
                                right_neighbor = current_generation[i + 1]
                            pattern = int(f"{left_neighbor}{current_generation[i]}{right_neighbor}", 2)
                            next_generation[i] = int(rule_bin[7 - pattern])
                        current_generation = next_generation
            print("\n")
automation_rule([90, 30 ,60, 55])
