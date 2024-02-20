






bidders= {"names":[],"bid_value":[]}
values=[]
names=[]
while True:
    name=input("enter your name")
    bid_value=float(input("enter your bid amount"))
    bidders["names"].append(name)
    bidders["bid_value"].append(bid_value)
    prompt=input("wanna add bidder yes or no?")
    if not prompt=="yes":
        maximum=max(bidders["bid_value"])
        index=bidders["bid_value"].index(maximum)
        winner_name=bidders["names"][index]
        print(f"winner is {winner_name} with bid amount ${maximum}")
        break


