number = int(input())
regular = set()
vip = set()
for _ in range(number):
    code = input()
    first_sign = code[0]
    if first_sign.isdigit():
        vip.add(code)
    else:
        regular.add(code)
guest_came = input()
while guest_came != "END":
    if guest_came in vip:
        vip.remove(guest_came)
    elif guest_came in regular:
        regular.remove(guest_came)
    guest_came = input()
result = len(vip) + len(regular)
print(result)
left_codes = vip.union(regular)
print("\n".join(sorted(left_codes)))