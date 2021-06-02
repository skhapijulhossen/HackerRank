import re

if __name__ == "__main__":
    uids = ["".join(sorted(input())) for t in range(int(input()))]
    
    for uid in uids:
        if re.search(r"[A-Z]{2}", uid) and re.search(r"\d{3}", uid) and not re.search(r"[^A-Za-z0-9]", uid):
            
            if not re.search(r"(\w)\1", uid):
                print(re.search(r"(\w)\1", uid))
        else:
            print("Invalid")
            re.search
    
        
