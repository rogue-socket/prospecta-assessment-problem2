import pandas as pd
import re


def extract_components(expression):
    """
    This returns the output of the parsing of the formula that is stored in any cell

    Example: =A4+5 returns [('A', '4'), '+', '5', 3]
    ('A', '4') shows the cell_number
    '+' shows the operator
    '5' shows the number
    3 shows the type of formula it is(out of 3 cases)

    :param expression: a string representing the formula
    :return: list of the breakdown of the function
    """
    pattern = r"^=([A-Za-z]+\d*|\d*\.?\d+)([+\-*/])([A-Za-z]+\d*|\d*\.?\d+)"
    to_return = []
    try:
        match = re.match(pattern, expression)
        if match:
            component1, operator, component2 = match.groups()
            # Determine case based on the components
            is_component1_coordinate = re.match(r"^[A-Za-z]+\d+$", component1)
            is_component2_coordinate = re.match(r"^[A-Za-z]+\d+$", component2)
            if is_component1_coordinate and is_component2_coordinate:
                to_return.append((component1[0], component1[1:]))
                to_return.append(operator)
                to_return.append((component2[0], component2[1:]))
                to_return.append(2)
            elif is_component1_coordinate or is_component2_coordinate:
                coord = component1 if is_component1_coordinate else component2
                num = component2 if is_component1_coordinate else component1
                to_return.append((coord[0], coord[1:]))
                to_return.append(operator)
                to_return.append(num)
                to_return.append(3)
            else:
                to_return.append(expression[1:])
                to_return.append(1)
    except Exception as e:
        print(f"Error in extract_components: {e}")

    return to_return


try:
    df = pd.read_csv("data2.csv")
    data_dict = {}

    for elem in df.columns:
        try:
            temp_data_list = elem.split(":")
            temp_data_list2 = [plem.strip() for plem in temp_data_list]
            data_dict[temp_data_list2[0]] = temp_data_list2[1]
        except Exception as e:
            print(f"Error in conversion to dict: {e}")

    for cell in data_dict:
        extracted_values = extract_components(data_dict[cell])

        if extracted_values:
            case_number = extracted_values[-1]

            try:
                if case_number == 1:
                    # =4+5 type expressions
                    data_dict[cell] = str(eval(extracted_values[0]))

                elif case_number == 2:
                    # Both components are coordinates
                    try:
                        cell_number_1 = extracted_values[0][0] + extracted_values[0][1]  # "A3"
                        cell_number_2 = extracted_values[2][0] + extracted_values[2][1]  # "A3"

                        # Extract the values from the referenced cells
                        cell_value_1 = extract_components(data_dict[cell_number_1])
                        part1 = data_dict[cell_number_1] if not cell_value_1 else None

                        cell_value_2 = extract_components(data_dict[cell_number_2])
                        part2 = data_dict[cell_number_2] if not cell_value_2 else None

                        if part1 and part2:
                            expression = part1 + extracted_values[1] + part2
                            data_dict[cell] = str(eval(expression))
                        else:
                            print(f"Could not retrieve both parts for {cell} in case 2")

                    except Exception as e:
                        print(f"Got error in case number 2: {e}")

                elif case_number == 3:
                    # Coordinate and the other is a number
                    try:
                        cell_number = extracted_values[0][0] + extracted_values[0][1]  # "A3"
                        rest_expression = extracted_values[1] + extracted_values[2]

                        # Extract the value from the referenced cell
                        cell_value = extract_components(data_dict[cell_number])
                        part1 = data_dict[cell_number] if not cell_value else None

                        if part1:
                            expression = part1 + rest_expression
                            data_dict[cell] = str(eval(expression))
                        else:
                            print(f"Could not retrieve cell value for {cell} in case 3")

                    except Exception as e:
                        print(f"Got error in case number 3: {e}")

            except Exception as e:
                print(f"Error processing cell {cell}: {e}")

except FileNotFoundError as fnf_error:
    print(f"Error reading CSV file: {fnf_error}")
except Exception as e:
    print(f"General error occurred: {e}")

# Saving to CSV
try:
    df_list = [key + ": " + data_dict[key] for key in data_dict]
    df_final = pd.DataFrame(columns=df_list)
    df_final.to_csv("final1.csv")
    print("Results saved successfully to final1.csv")
except Exception as e:
    print(f"Error saving final CSV: {e}")
