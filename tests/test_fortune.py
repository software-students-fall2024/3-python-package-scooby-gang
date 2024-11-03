import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.fortune.FortuneCookie import quoteGetter, customFortuneCookie, addQuote, fortuneCookie, randomFortuneCookie, cookieScript

class Tests:

    @pytest.fixture
    def example_fixture(self):
        """
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        """

        # place any setup you want to do before any test function that uses this fixture is run

        yield  # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    #
    # Test functions
    #

    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_quoteGetter(self, capsys):
        fortunes = quoteGetter(4)
        captured = capsys.readouterr()

        assert "A fresh start will put you on your way." in captured.out or "All your hard work will soon pay off." in captured.out
        assert "Don't look now, but I'm pretty sure that guy just took a piece of your hair." in captured.out or "Great news! Tyler Perry just signed on to do the new Batman trilogy!" in captured.out
        assert len(fortunes) == 4, "Expected four fortunes to be retrieved"

    def test_customFortuneCookie(self, capsys):
        """
        Verify customFortuneCookie() function and make sure it returns a non-empty string.
        Note that for example purposes, we have not used the example_fixture in this test function.
        """

        for i in range(100):
            test_outputImage = f"""                                                                                                    
                                                                                                        
                                                                                                        
                                                                                                        
                                .@@*#@+%#...........                                                 
                            ..@*+=========####*++@@@..                                                
                            .@@==--===+==--===#=======+++.                                              
                        .@+==------==*@=---=@#===----==+@.                                            
                        .@===-:::::--==+%%=---==+==------==+@.                           =@@-=#@        
                    @-==--::---:-===+#*=---=====---:---==++.              .:@=@%=...........%.       
                    +@===---------=====@*=-----==----::--====%....... @@:.=++:................@.       
                    @===---------======*@*=----------:::@--====@@%#=%.........................:@        
                .@===--------==@=====@%@=---------::::---====@%@..........................:+=*        
                =#===-------=========+#*@=-------:::::---=====+*+....An exciting opportunity lies ahead of you......#.        
                :@==--------==========%%@=----------::----====+@#=...........................=@.        
                @==-------====*======@%@==--------:::----=====+@#...........................-*-.        
                @==-------==+%#===-==+##@=-------::::---======+*%=..........==###%@%##-..==#@@@..        
                @==-------==+#*#=====#@@@=@-----:::::---==-====@@@..........==@@@*=*@@=...........        
                @==-----====+#+=====#@@=*=----::-::---======++@#+%@%@+........                            
                %+==----===#+#=====##@..%=------::----======+=@%..                                         
                #+=========#@*==+@@@....=----:::::---=======+@@...                                         
                .@*++========%+++@%......@=--::::::-@====@=++@@..                                            
                %+++######+++@@...     .+=--::::--=======+%@@...                                            
                @+#@@##++@@.           .@-::----======+++-#@..                                              
                .*+#@#@   ..           @=#@--=======@+#=@+%...                                              
                                    @=@=======+++@@@#@:.                                                 
                                    @+===+%=+++#%@@+@..                                                  
                                    ++=====##@#@#@@@..                                                   
                                    .#+++##@@%%@@@....                                                   
                                    .##%@@@@@@#@...                                                      
                                    .:+@*@@@+@.                                                          
                                    .. %@@@...                                                           
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        """
            customFortuneCookie("An exciting opportunity lies ahead of you.")
            actual_captured = capsys.readouterr()
            assert (".@@*#@+%#" in actual_captured.out), f"Expected the text printed by customFortuneCookie() contain an ASCII image."
            assert ("An exciting opportunity lies ahead of you." in actual_captured.out), f"Expected the text printed by customFortuneCookie() to contain the input quote: 'An exciting opportunity lies ahead of you.'"

    def test_addQuote(self):

        quotes = [
            "The best way to predict the future is to create it.",
            "Happiness is not something ready-made. It comes from your own actions.",
            "You will find great success in your endeavors.",
            "Your hard work will soon pay off.",
            "Adventure awaits you around the corner.",
            "Believe you can and you're halfway there.",
            "A friend is someone who knows all about you and still loves you.",
            "The only limit to our realization of tomorrow is our doubts of today.",
            "You will make a change for the better.",
            "Your talents will be recognized and suitably rewarded."
        ]

        """
        Verify addQuote() function and make sure it returns a non-empty string.
        Note that for example purposes, we have not used the example_fixture in this test function.
        """
        
        for i in range(10):
            addQuote(quotes[i], "g")
            f = open("GoodFortune.txt", "r")
            content = f.read()
            assert (quotes[i] in content), f"Expected the new quote in GoodFortune text file."

    @pytest.mark.parametrize("fortuneAmount, expected_output, expected_return", [
        (3, 3, True),  # Test case for valid amount: print 3 fortunes, return True
        (6, "fortune amount exceeds 5", False),  # Test case for exceeding amount: print warning and return False
        (0, "", True)  # Test case for zero amount: no output, return True
    ])
    def test_randomFortuneCookie(self, fortuneAmount, expected_output, expected_return, capsys):

        result = randomFortuneCookie(fortuneAmount)
        captured = capsys.readouterr()
        assert result == expected_return, f"Expected {expected_return} for fortuneAmount={fortuneAmount}, got {result}"

        if isinstance(expected_output, int):
            printed_fortunes = captured.out.strip().split("\n")
            assert len(printed_fortunes) == expected_output, f"Expected {expected_output} fortunes printed, got {len(printed_fortunes)} for fortuneAmount={fortuneAmount}"
        else:
            assert expected_output in captured.out, f"Expected warning message '{expected_output}' in output for fortuneAmount={fortuneAmount}"

    @pytest.mark.parametrize("fortuneCustom, inputs, expected_outputs", [
        # Test case for creating a custom fortune with "c"
        ("c", ["A custom fortune message."], [
            "Welcome to Scooby's Fortunes!",
            "A custom fortune message.",
            "Goodbye!"
        ]),

        # Test case for purchasing fortunes within the limit with "p"
        ("p", ["3", "yes"], [
            "Welcome to Scooby's Fortunes!",
            "Goodbye!"
        ]),

        # Test case for purchasing zero fortunes (should exit)
        ("p", ["0"], [
            "Welcome to Scooby's Fortunes!",
            "Sad to see you go.",
            "Goodbye!"
        ]),

        # Test case for exceeding the limit and retrying a valid number
        ("p", ["11", "3", "no"], [
            "Welcome to Scooby's Fortunes!",
            "Inavlid Fortune amount, try again.",
            "Goodbye!"
        ]),
    ])
    def test_cookieScript(self, fortuneCustom, inputs, expected_outputs, capsys):
        """
        Test cookieScript function with different input scenarios.
        """

        input_sequence = iter(inputs)

        def mock_input(prompt):
            return next(input_sequence)

        with pytest.monkeypatch.context() as m:
            m.setattr("builtins.input", mock_input)
            cookieScript(fortuneCustom)
            captured = capsys.readouterr()

        for expected_output in expected_outputs:
            assert expected_output in captured.out, f"Expected '{expected_output}' in output, but it was not found." 
                   
    #def test_1(self):
    #    assert True  # Replace with actual tests