from listener import wait_for_wake_word, listen_for_command
from responder import respond_to_command

def main():
    print("Aura is ready. Say 'Aura' to wake her up.")
    while True:
        if wait_for_wake_word():
            command = listen_for_command()
            if command:
                respond_to_command(command)

if __name__ == "__main__":
    main()
