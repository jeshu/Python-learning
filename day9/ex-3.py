import art

print(art)

print("Welcome to Silent Bids")


def check_highest_bid(bids):
    top_bidder = ''
    top_amount = 0
    for bid in bids:
        if(bid['amount'] > top_amount):
            top_bidder = bid['name']
            top_amount = bid['amount']

    print(f'Top bidder is {top_bidder} and amount {top_amount}')


def get_bids():
    bids = []
    name = input('Your name: ')
    amount = int(input('Your Bid: '))
    bids.append({"name": name, "amount": amount})

    cont = input('Add more bids? ')
    if cont == 'yes':
        get_bids()
    else:
        check_highest_bid(bids)


get_bids()
