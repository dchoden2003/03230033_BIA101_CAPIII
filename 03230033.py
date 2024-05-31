# Dawa Choden
# BBI A
# 03230033
#reference : https://www.youtube.com/watch?v=rxS9GY7ISi0&list=PLVJiPhsW8Gnf5rQCOXoptugEtJneB0ZOd
#Your Solution Score: <480893>


def read_input(file_path):#read the inputn file.
    with open(file_path, 'r') as file:# it will open the file located at specific file path.
        lines = file.readlines()# reads all the lines from  the file.
    return lines
    
def extract_digits(line):
    digits = [] #to store the characters theat are digits.
    for char in line:
        if char.isdigit():
            digits.append(char)# if character is digit it will append to the digit list.
    if len(digits) >= 2:# check digit count, atleast two digit is needed.
        first_num= digits[0]
        second_num=digits[-1]#exteacting the first and the last digit fromm the list.
        return int(first_num + second_num)
    else:
        return 0


def solve(lines):
    total_sum = 0 # initialize the sum to zero.
    for line in lines: #using the for loop to iterate over each element in the line list. 
        two_digit_num = extract_digits(line) 
        if two_digit_num != 0:
            total_sum += two_digit_num # adding the total sum to two digit sum if it is not equal to 0.
    return total_sum


def main():
    input_file_path = "033.txt" 
    lines = read_input(input_file_path)
    answer = solve(lines)


    print(f"The total sum of  given input file {input_file_path} is {answer}")
if __name__ == "__main__":
    main()