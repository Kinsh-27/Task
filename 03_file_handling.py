''' Create a script to read a text file, count the number of
 words, and write the results to a new file. '''

input_file = "03_input.txt"   # Input file name
output_file = "03_output.txt" # Output file name

try:
    # Read the text file
    with open(input_file, "r") as file:
        count = 0
        # Count the number of words
        for line in file:
            words = line.split()  
            count += len(words)
    
    # Display word count in the console
    print(f"Number of words in the text file '{input_file}': {count}")
    
    # Write the result to the output file
    with open(output_file, "w") as file:
        file.write(f"The total number of words in '{input_file}' is: {count}\n")
    print(f"Word count result saved in '{output_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
