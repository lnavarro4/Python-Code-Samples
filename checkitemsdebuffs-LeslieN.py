
#Leslie N
#3/08/25

#Problem 5
#Check items needed and any debuffs


def check_task(character_items, character_debuffs):

    task1_items = ["rope", "coat", "first aid kit"]
    task1_debuffs = ["slow"]

    task2_items = ["pan", "groceries"]
    task2_debuffs = ["small"]

    task3_items = ["pen", "paper", "idea"]
    task3_debuffs = ["confusion"]

    def check_task_1():
        missing_items = [item for item in task1_items if item not in character_items]
        has_debuff = any(debuff in character_debuffs for debuff in task1_debuffs)
        if not missing_items and not has_debuff:
            print("Congratulations! You successfully climbed the mountain.")
        else:
            if missing_items:
                print("Cannot climb mountain. Missing items.")
            if has_debuff:
                print("Cannot climb mountain. Debuff.'slow' in effect.")

    def check_task_2():
        missing_items = [item for item in task2_items if item not in character_items]
        has_debuff = any(debuff in character_debuffs for debuff in task2_debuffs)
        if not missing_items and not has_debuff:
            print("Congratulations! You successfully cooked a meal.")
        else:
            if missing_items:
                print("Cannot cook meal. Missing items.")
            if has_debuff:
                print("Cannot cook meal. Debuff 'small' in effect.")

    def check_task_3():
        missing_items = [item for item in task3_items if item not in character_items]
        has_debuff = any(debuff in character_debuffs for debuff in task3_debuffs)
        if not missing_items and not has_debuff:
            print("Congragulations! You successfully wrote a book.")
        else:
            if missing_items:
                print("Cannot write book. Missing items.")
            if has_debuff:
                print("Cannot write book. Debuff 'confusion' in effect.")

