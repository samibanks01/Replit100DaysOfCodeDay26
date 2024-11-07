import os
import time
import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load the sound file
sound = pygame.mixer.Sound('audio.wav')

# Function to pause the music
def pause():
  pygame.mixer.pause()

# Function to play the music
def play():
  # Unpause the music
  pygame.mixer.unpause()

  # Keep playing until the user presses 2
  while True:
    # Ask the user to press 2 to stop
    stop_playback = int(input("Press 2 anytime to pause playback and go back to the menu: "))

    # If the user pressed 2, pause the music and return to the menu
    if stop_playback == 2:
      pause()
      return  # Return to the main menu

    # If the user pressed anything else, continue playing
    else:
      continue

# Main loop
while True:
  # Clear the screen
  os.system("clear")

  # Print the menu
  print("🎵 MyPOD Music Player ")
  time.sleep(1)
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print("Press anything else to see the menu again")

  # Get the user's input
  userInput = int(input())

  # If the user pressed 1, play the music
  if userInput == 1:
    print("Playing some proper tunes!")
    play()

  # If the user pressed 2, exit the program
  elif userInput == 2:
    exit()

  # If the user pressed anything else, show the menu again
  else:
    continue
