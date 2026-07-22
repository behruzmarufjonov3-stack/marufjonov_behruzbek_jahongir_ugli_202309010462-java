from ticket import create_ticket
from display import show_ticket

def main():
    ticket = create_ticket()

    if ticket:
        show_ticket(ticket)

if __name__ == "__main__":
    main()