from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        expected_search_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('soccer'), expected_search_soccer_results)

    def test_search(self):
        expected_results =  [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Arabic music', 'RussBot', 1209417864, 25114], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]

        self.assertEqual(search("barn"),[])
        self.assertEqual(search("Rock"),expected_results)
        self.assertEqual(search(""),[])

    def test_article_length(self):
        rock_related =  [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Arabic music', 'RussBot', 1209417864, 25114], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        less50thous = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['Arabic music', 'RussBot', 1209417864, 25114], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['2007 in music', 'Bearcat', 1169248845, 45652]]
        self.assertEqual(article_length( 1000000000, rock_related),rock_related)
        self.assertEqual(article_length(50000, rock_related),less50thous)
        self.assertEqual(article_length(50, rock_related),[])

    def test_unique_name(self):
        rock_related =  [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Arabic music', 'RussBot', 1209417864, 25114], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        uniques1 =[['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023],['2009 in music', 'RussBot', 1235133583, 69451],['Rock music', 'Mack Johnson', 1258069053, 119498],['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458]]
        self.assertEqual(unique_authors(4, rock_related),uniques1)
        # test that is will resulnt in all uniqes printed 
        uniques2 = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419]]
        self.assertEqual(unique_authors(15, rock_related),uniques2)
        bulldogs = [['2007 Bulldogs RLFC season', 'Burna Boy', 1177410119, 11116], ['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718]]
        self.assertEqual(unique_authors(0, bulldogs), [])
        result = [['2007 Bulldogs RLFC season', 'Burna Boy', 1177410119, 11116]]
        self.assertEqual(unique_authors(1, bulldogs),result)

    def test_recent(self):
        rock_related =  [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Arabic music', 'RussBot', 1209417864, 25114], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        self.assertEqual(most_recent_article(rock_related),['Rock music', 'Mack Johnson', 1258069053, 119498])
        
        game = [['2007 Bulldogs RLFC season', 'Burna Boy', 1177410119, 11116], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718], ['Lua (programming language)', 'Burna Boy', 1113957128, 0], ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413]]
        self.assertEqual(most_recent_article(game),['2007 Bulldogs RLFC season', 'Burna Boy', 1177410119, 11116])
        
        blue = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Dalmatian (dog)', 'Mr Jake', 1207793294, 26582]]
        self.assertEqual(most_recent_article(blue), ['Dalmatian (dog)', 'Mr Jake', 1207793294, 26582])

    def test_redefined(self):
        rock_related =  [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Arabic music', 'RussBot', 1209417864, 25114], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        canadians = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023],
                    ['2009 in music', 'RussBot', 1235133583, 69451],
                    ['2007 in music', 'Bearcat', 1169248845, 45652],
                    ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        self.assertEqual(refine_search("Canadian", rock_related), canadians)
        set2 =  [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
          ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
          ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]
        self.assertEqual(refine_search("find",set2), [])
        blues = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        self.assertEqual(refine_search("", blues), [])

    def test_fave(self):
        music =  [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], ['1936 in music', 'RussBot', 1243745950, 23417], ['1962 in country music', 'Mack Johnson', 1249862464, 7954], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['1996 in music', 'Nihonjoe', 1148585201, 21688], ['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['Texture (music)', 'Bearcat', 1161070178, 3626], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        self.assertEqual(favorite_author("Michael Jackson ", music),False)
        self.assertEqual(favorite_author("jack johnson", music),True)
        self.assertEqual(favorite_author("", music),False)

    def test_title_and_article(self):
        set1 = [['Black dog (ghost)', 'Pegship', 1220471117, 14746], ['Mexican dog-faced bat', 'Mack Johnson', 1255316429, 1138], ['Dalmatian (dog)', 'Mr Jake', 1207793294, 26582],['Guide dog', 'Jack Johnson', 1165601603, 7339], ['Sun dog', 'Mr Jake', 1208969289, 18050]]
        result1 = [('Black dog (ghost)', 'Pegship'),('Mexican dog-faced bat', 'Mack Johnson'),('Dalmatian (dog)', 'Mr Jake'),('Guide dog', 'Jack Johnson'),('Sun dog', 'Mr Jake')]
        self.assertEqual(title_and_author(set1),result1)
        self.assertEqual(title_and_author([]),[])
        four = [['Rock music', 'Mack Johnson', 1258069053, 119498], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Indian classical music', 'Burna Boy', 1222543238, 9503]]
        four1 = [('Rock music', 'Mack Johnson'), ('List of dystopian music, TV programs, and games', 'Bearcat'), ('Indian classical music', 'Burna Boy')]
        self.assertEqual(title_and_author(four),four1)

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_origonalexample_IaccidentlyEdited_integration_test(self, input_mock):
        keyword = 'music'
        advanced_option = 1
        advanced_response = 3000
        # accidently edited this one, could not remeber what is was orgonal 
        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)
        
    #my main test 
    @patch('builtins.input')
    def test_length_integration_test(self, input_mock):
        keyword = 'rock'
        advanced_option = 1
        advanced_response = 4000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_unique_integration_test(self, input_mock):
        keyword = 'program'
        advanced_option = 2
        advanced_response = 6

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['C Sharp (programming language)', 'Burna Boy', 1232492672, 52364], ['Fisk University', 'RussBot', 1263393671, 16246]]\n"
        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_recent_integration_test(self, input_mock):
        keyword = 'games'
        advanced_option = 3
        #advanced_response = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413]\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_favorite_author_integration_test(self, input_mock):
        keyword = 'blues'
        advanced_option = 4
        advanced_response = ""

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['2008 in music', 'Burna Boy', 1217641857, 107605]]\n"+ "Your favorite author is not in the returned articles!\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_titles_and_author_integration_test(self, input_mock):
        keyword = 'Fire'
        advanced_option = 5

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: [('Dalmatian (dog)', 'Mr Jake'), ('Steve Perry (musician)', 'Nihonjoe')]\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_refine_integration_test(self, input_mock):
        keyword = 'music'
        advanced_option = 6
        advanced_response = "Jazz"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['1986 in music', 'jack johnson', 1048918054, 6632], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Arabic music', 'RussBot', 1209417864, 25114], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]\n"
        self.assertEqual(output, expected)
    

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
