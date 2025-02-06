import re

class SRPar:

    def __init__(self):
       
        self.SRParGrammar_id = {
            "E": [["E", "+", "T"], ["T"]],
            "T": [["T", "*", "F"], ["F"]],
            "F": [["(", "E", ")"], ["id"]]
        }

        
        self.Parsing_Table = {
            (0, "id"): "S5", (0, "("): "S4", (0, "E"): 1, (0, "T"): 2, (0, "F"): 3,
            (1, "+"): "S6", (1, "$"): "accept",
            (2, "+"): "R2", (2, "*"): "S7", (2, ")"): "R2", (2, "$"): "R2",
            (3, "+"): "R4", (3, "*"): "R4", (3, ")"): "R4", (3, "$"): "R4",
            (4, "id"): "S5", (4, "("): "S4", (4, "E"): 8, (4, "T"): 2, (4, "F"): 3,
            (5, "+"): "R6", (5, "*"): "R6", (5, ")"): "R6", (5, "$"): "R6",
            (6, "id"): "S5", (6, "("): "S4", (6, "T"): 9, (6, "F"): 3,
            (7, "id"): "S5", (7, "("): "S4", (7, "F"): 10,
            (8, "+"): "S6", (8, ")"): "S11",
            (9, "+"): "R1", (9, "*"): "S7", (9, ")"): "R1", (9, "$"): "R1",
            (10, "+"): "R3", (10, "*"): "R3", (10, ")"): "R3", (10, "$"): "R3",
            (11, "+"): "R5", (11, "*"): "R5", (11, ")"): "R5", (11, "$"): "R5"
        }

       
        self.s_r_p_reductions = {
            "R1": ("E", ["E", "+", "T"]),
            "R2": ("E", ["T"]),
            "R3": ("T", ["T", "*", "F"]),
            "R4": ("T", ["F"]),
            "R5": ("F", ["(", "E", ")"]),
            "R6": ("F", ["id"])
        }

    def s_r_p_tokenize_(self, input_string):
       
        return re.findall(r'id|[+*()$]', input_string)

    def s_r_p_parse(self, input_string):
     
        stack = [0]
        input_list = self.s_r_p_tokenize_(input_string) + ["$"]

        while True:
            state = stack[-1]
            symbol = input_list[0]
            action = self.Parsing_Table.get((state, symbol))

            if action is None:
                print("INVALID string entered. SYNTAX ERROR!")
                return False

            if action.startswith("S"):
                
                stack.append(int(action[1:]))
                input_list.pop(0)
            elif action.startswith("R"):
              
                head, body = self.s_r_p_reductions[action]
                for _ in range(len(body)):
                    stack.pop()
                goto_state = self.Parsing_Table.get((stack[-1], head))
                if goto_state is None:
                    print("INVALID string entered. SYNTAX ERROR!")
                    return False
                stack.append(goto_state)
            elif action == "accept":
                print("VALID string entered. ACCEPTED!")
                return True
            else:
                print("INVALID string entered. SYNTAX ERROR!")
                return False


if __name__ == "__main__":
    parser = SRPar()
    user_input = input("Enter your string: ")
    parser.s_r_p_parse(user_input)

