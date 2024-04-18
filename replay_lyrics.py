import time
import sys

# Define the lyrics with corresponding timestamps (in seconds) and custom delay times (in seconds)
lyrics_with_custom_delays = [
    (0, "Who would have ever knew", 1.4),
    (4, "That we would ever be more than friends?", 0.1),
    (9, "We're real worldwide, breaking all the rules", 1),
    (14, "She like a song played again and again", 2),
    (19, "", 1),
    (20, "(That girl) like something off a poster", 1.2),
    (24, "(That girl) is a dime they say", 1),
    (28, "(That girl) is a gun to my holster", 2),
    (32, "And she's running through my mind all day, ayy", 2),
    (36, "", 1),
    (37, "Shawty's like a melody in my head", 1.5),
    (41, "That I can't keep out, got me singing like ", 1),
    (45, "Na-na-na-na, every day", 1.1),
    (49, "It's like my iPod stuck on replay, replay-ay-ay-ay", 2),
    (53, "", 1),
    (54, "Shawty's like a melody in my head", 1.1),
    (58, "That I can't keep out, got me singing like", 1.5),
    (62, "Na-na-na-na, every day", 1.5),
    (66, "It's like my iPod stuck on replay, replay-ay-ay-ay", 1.5)
]

def print_lyrics():
    for timestamp, line, custom_delay in lyrics_with_custom_delays:
        if line.strip():  # Only process non-empty lines
            for char in line:
                sys.stdout.write(char)  # Print the character
                sys.stdout.flush()  # Flush the output to show immediately
                time.sleep(0.05)  # Adjust delay between characters (e.g., 0.05 seconds)

            # Pause at the end of each line with custom delay time
            time.sleep(custom_delay)  # Adjust delay between lines based on custom delay

            # Move to the next line
            print()  # Print a newline

# Call the function to print the lyrics character by character with adjusted timing
print_lyrics()
