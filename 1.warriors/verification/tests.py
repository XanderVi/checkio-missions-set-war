init_code = """
if not "Warrior" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Warrior'?")

Warrior = USER_GLOBAL['Warrior']

fight = USER_GLOBAL['fight']
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
                ]
}
