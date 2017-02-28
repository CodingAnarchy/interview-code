receipts = [['Matthew', 400, 'Car', 'Matthew', 'Varun', 'Bob', 'Alice'], ['Varun', 200, 'Groceries', 'Alice', 'Bob', 'Matthew']]

owes_dict = {}
for r in receipts:
    payee = r[0]
    payers = r[3:]
    amt = r[1] / len(payers)
    for p in payers:
        if not p == payee:
            if p not in owes_dict:
                owes_dict[p] = {}
            if payee not in owes_dict[p]:
                owes_dict[p][payee] = 0
            owes_dict[p][payee] += amt

print owes_dict

for k, v in owes_dict.items():
    for payer, payees in owes_dict.items():
        if k in payees:
            amt_owed = owes_dict[payer][k]
            payee_overlap = set(payees).intersection(set(v))
            if len(payee_overlap) != 0:
                owes_dict[payer][k] = 0
                amt_owed /= len(payee_overlap)
                for p in payee_overlap:
                    owes_dict[k][p] -= amt_owed
                    owes_dict[payer][p] += amt_owed

for k, v in owes_dict.items():
    for payee, amt in v.items():
        print "%s pays %s $%d" % (k, payee, amt)
