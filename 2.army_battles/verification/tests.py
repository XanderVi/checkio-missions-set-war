init_code = """
if not "Army" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Army'?")

Army = USER_GLOBAL['Army']

if not "Warrior" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Warrior'?")

Warrior = USER_GLOBAL['Warrior']

fight = USER_GLOBAL['fight']

battle = USER_GLOBAL['battle']
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. Fight": [
        prepare_test(middle_code='''carl = Warrior(20, 1)
jim = Warrior(10, 2)''',
                     test="fight(carl, jim)",
                     answer="Both died...")
                ],

    "2. Fight": [
        prepare_test(middle_code='''ramon = Warrior(67, 4)
slevin = Warrior(99, 3)''',
                     test="fight(ramon, slevin)",
                     answer="Second warrior wins!")
                ],
    "3. Fight": [
        prepare_test(middle_code='''bob = Warrior(13, 3)
mars = Warrior(30, 1)''',
                     test="fight(bob, mars)",
                     answer="First warrior wins!")
                ],
    "4. Fight": [
        prepare_test(middle_code='''zeus = Warrior(9999, 2)
godkiller = Warrior(202, 99)''',
                     test="fight(zeus, godkiller)",
                     answer="Both died...")
                ],
    "5. Fight": [
        prepare_test(middle_code='''husband = Warrior(50, 2)
wife = Warrior(25, 3)''',
                     test="fight(husband, wife)",
                     answer="First warrior wins!")
                ],
    "6. Fight": [
        prepare_test(middle_code='''dragon = Warrior(666, 3)
knight = Warrior(99, 25)''',
                     test="fight(dragon, knight)",
                     answer="Second warrior wins!")
                ],
    "1. Battle": [
        prepare_test(middle_code='''unit_1 = Warrior(20, 1)
unit_2 = Warrior(30, 2)
unit_3 = Warrior(25, 3)
unit_4 = Warrior(60, 1)
unit_5 = Warrior(10, 10)
army_1 = Army()
army_2 = Army()
army_1.add_unit(unit_1)
army_1.add_unit(unit_3)
army_1.add_unit(unit_5)
army_2.add_unit(unit_2)
army_2.add_unit(unit_4)''',
                     test="battle(army_1, army_2)",
                     answer="First army wins!")
                ],

    "2. Battle": [
        prepare_test(middle_code='''unit_1 = Warrior(90, 1)
unit_2 = Warrior(60, 5)
unit_3 = Warrior(20, 8)
unit_4 = Warrior(40, 2)
unit_5 = Warrior(55, 5)
army_1 = Army()
army_2 = Army()
army_1.add_unit(unit_1)
army_1.add_unit(unit_2)
army_1.add_unit(unit_3)
army_2.add_unit(unit_5)
army_2.add_unit(unit_4)''',
                     test="battle(army_1, army_2)",
                     answer="First army wins!")
                ],
    "3. Battle": [
        prepare_test(middle_code='''unit_1 = Warrior(25, 2)
unit_2 = Warrior(30, 1)
unit_3 = Warrior(70, 5)
unit_4 = Warrior(20, 11)
unit_5 = Warrior(29, 10)
army_1 = Army()
army_2 = Army()
army_1.add_unit(unit_1)
army_1.add_unit(unit_2)
army_2.add_unit(unit_5)
army_2.add_unit(unit_3)
army_2.add_unit(unit_4)''',
                     test="battle(army_1, army_2)",
                     answer="Second army wins!")
                ],
    "4. Battle": [
        prepare_test(middle_code='''unit_1 = Warrior(2000, 1)
unit_2 = Warrior(200, 5)
unit_3 = Warrior(200, 4)
unit_4 = Warrior(150, 6)
unit_5 = Warrior(180, 2)
army_1 = Army()
army_2 = Army()
army_1.add_unit(unit_1)
army_2.add_unit(unit_2)
army_2.add_unit(unit_3)
army_2.add_unit(unit_4)
army_2.add_unit(unit_5)''',
                     test="battle(army_1, army_2)",
                     answer="Second army wins!")
                ],
    "5. Battle": [
        prepare_test(middle_code='''unit_1 = Warrior(200, 2)
unit_2 = Warrior(100, 1)
unit_3 = Warrior(100, 1)
unit_4 = Warrior(100, 1)
unit_5 = Warrior(100, 1)
army_1 = Army()
army_2 = Army()
army_1.add_unit(unit_2)
army_1.add_unit(unit_3)
army_1.add_unit(unit_4)
army_1.add_unit(unit_5)
army_2.add_unit(unit_1)''',
                     test="battle(army_1, army_2)",
                     answer="All died...")
                ],
    "6. Battle": [
        prepare_test(middle_code='''unit_1 = Warrior(1000, 5)
unit_2 = Warrior(2000, 4)
unit_3 = Warrior(800, 6)
unit_4 = Warrior(1200, 3)
unit_5 = Warrior(1650, 2)
army_1 = Army()
army_2 = Army()
army_1.add_unit(unit_1)
army_1.add_unit(unit_3)
army_1.add_unit(unit_5)
army_2.add_unit(unit_2)
army_2.add_unit(unit_4)''',
                     test="battle(army_1, army_2)",
                     answer="First army wins!")
                ]
}
