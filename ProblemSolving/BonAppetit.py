def bonAppetit(bill, k, b):
    # Write your code here
    bactual = sum([bill[i] for i in range(len(bill)) if i != k])/2
    if b ==bactual:
        print("Bon Appetit")
    else:
        print(int(b-bactual))