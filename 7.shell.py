import os
import subprocess
import sys

def execute_command(cmd_input):
    """
    Parses and executes a command line string with support for pipes and redirection.
    """
    # 1. Handle Piping (|)
    # Split the input by '|' to find distinct commands in the chain
    commands = cmd_input.split('|')
    
    prev_process_stdout = None  # Holds the stdout of the previous process in a pipe chain
    processes = [] # Keep track of processes to wait for them later

    try:
        for i, cmd_str in enumerate(commands):
            cmd_str = cmd_str.strip()
            if not cmd_str:
                continue

            # Parse the individual command for parts
            parts = cmd_str.split()
            
            # --- Handle 'cd' command (Special Case) ---
            # Subprocesses cannot change the parent directory, so we do it in python
            if parts[0] == 'cd':
                try:
                    target_dir = parts[1] if len(parts) > 1 else os.path.expanduser("~")
                    os.chdir(target_dir)
                except FileNotFoundError:
                    print(f"cd: no such file or directory: {parts[1]}")
                return # Stop processing this command line
            
            # --- Handle Redirection (> and <) ---
            input_file = None
            output_file = None
            clean_args = []
            
            # Iterate through parts to find redirection symbols
            skip_next = False
            for idx, part in enumerate(parts):
                if skip_next:
                    skip_next = False
                    continue
                
                if part == '>':
                    # Output redirection
                    if idx + 1 < len(parts):
                        output_file = parts[idx + 1]
                        skip_next = True
                elif part == '<':
                    # Input redirection
                    if idx + 1 < len(parts):
                        input_file = parts[idx + 1]
                        skip_next = True
                else:
                    clean_args.append(part)

            # --- Setup Standard Input/Output ---
            stdin = prev_process_stdout # Default to previous pipe output
            stdout = None
            
            # If explicit input file is provided (<), override stdin
            if input_file:
                try:
                    stdin = open(input_file, 'r')
                except FileNotFoundError:
                    print(f"Error: File '{input_file}' not found.")
                    return

            # If explicit output file is provided (>), override stdout
            if output_file:
                stdout = open(output_file, 'w')
            
            # If this is NOT the last command in a pipe chain, output to a PIPE
            elif i < len(commands) - 1:
                stdout = subprocess.PIPE

            # --- Execute ---
            # We use Popen for granular control over input/output streams
            proc = subprocess.Popen(
                clean_args,
                stdin=stdin,
                stdout=stdout,
                stderr=subprocess.PIPE, # Capture errors to print them nicely
                text=True # Ensure we deal with strings, not bytes
            )
            
            processes.append(proc)
            
            # Update prev_process_stdout for the next iteration
            prev_process_stdout = proc.stdout
            
            # If we used a file for input, we can close the file handle in the parent
            # (The subprocess has its own handle now)
            if input_file and stdin != subprocess.PIPE and stdin is not None:
                stdin.close()

        # Wait for the last process to finish and print its output if not redirected
        last_proc = processes[-1]
        out, err = last_proc.communicate()
        
        if out: print(out, end='')
        if err: print(err, end='')

    except Exception as e:
        print(f"Shell Error: {e}")

def main():
    print("Welcome to Custom Python Shell. Type 'exit' to quit.")
    
    while True:
        try:
            # Display prompt with current directory
            current_dir = os.getcwd()
            user_input = input(f"{current_dir} $ ")
            
            if user_input.strip() == "exit":
                break
            
            if user_input.strip():
                execute_command(user_input)
                
        except KeyboardInterrupt:
            print("\nType 'exit' to quit.")
        except EOFError:
            break

if __name__ == "__main__":
    main()