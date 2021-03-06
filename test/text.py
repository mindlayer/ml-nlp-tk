import unittest
from ml_nlp_tk.text import *


class TestText(unittest.TestCase):

    def test_clean_all(self):
        self.assertEqual("無聊得過此帖？！    \n \n \n認同。 \n \n改洋名，只是一個字號。", clean_all(
            "<br><br>http://news.IN1802020028.htm[quote]原帖由 [i]234282[/i] 於 2019-1-18 06:46 PM 發表 [url=https://www.discuss.com.hk/redirect.php?goto=findpost&amp;pid=493614969&amp;ptid=27981082][img]https://www.discuss.com.hk/images/common/back.gif[/img][/url]<br>\n無聊得過此帖？！:smile_42: [/quote]<br>\n<br>\n<br>\n認同。<br>\n<br>\n改洋名，只是一個字號。"))
        self.assertEqual("Phraseg - 一言：新詞發現工具包 今天天氣 晴朗", clean_all(
            "[i]234282[/i] <div class=""><p>Phraseg - 一言：新詞發現工具包http://news.IN1802020028.htm今天天氣http://news.we028.晴朗</p></div>"))

    def test_clean_unused_tag(self):
        self.assertEqual(clean_unused_tag(
            "[quote]原帖由 [i]234282[/i] 於 2019-1-18 06:46 PM 發表 [url=https://www.discuss.com.hk/redirect.php?goto=findpost&amp;pid=493614969&amp;ptid=27981082][img]https://www.discuss.com.hk/images/common/back.gif[/img][/url]<br>\n無聊得過此帖？！:smile_42: [/quote]<br>\n<br>\n<br>\n認同。<br>\n<br>\n改洋名，只是一個字號。"),
            "無聊得過此帖？！    \n \n \n認同。 \n \n改洋名，只是一個字號。")
        self.assertEqual(clean_unused_tag(
            "[quote]<br>\n無聊得過此帖？！:smile_42: [/quote]<br>\n<br>\n<br>\n認同。<br>\n<br>\n改洋名，只是一個字號。"),
            "無聊得過此帖？！    \n \n \n認同。 \n \n改洋名，只是一個字號。")

    def test_clean_htmlelement(self):
        self.assertEqual(clean_htmlelement("<div class=""><p>Phraseg - 一言：新詞發現工具包</p></div>"), "Phraseg - 一言：新詞發現工具包")

    def test_clean_httplink(self):
        self.assertEqual(clean_httplink("http://news.IN1802020028.htm 今天天氣http://news.we028.晴朗"), "今天天氣 晴朗")
        self.assertEqual(clean_httplink(" https://forum.gamer.com.tw/C.php?bsn=60076&amp;snA=2817750  "), "")

    def test_split_lines_by_punc(self):
        self.assertEqual(split_lines_by_punc(["你好啊.hello，me"]), ['你好啊', 'hello', 'me'])

    def test_split_sentence_to_ngram(self):
        self.assertEqual(split_sentence_to_ngram("加州旅館"),
                         ['加', '加州', "加州旅", "加州旅館", "州", "州旅", "州旅館", "旅", "旅館", "館"])

    def test_split_sentence_to_ngram_in_part(self):
        self.assertEqual(split_sentence_to_ngram_in_part("加州旅館"),
                         [['加', '加州', "加州旅", "加州旅館"], ["州", "州旅", "州旅館"], ["旅", "旅館"], ["館"]])

    def test_spilt_text_in_all_ways(self):
        self.assertEqual(spilt_text_in_all_ways("加州旅館"),
                         ['加 州 旅 館', '加 州 旅館', '加 州旅 館', '加 州旅館', '加州 旅館', '加州旅 館', '加州旅館'])

    def test_spilt_sentence_to_array(self):
        self.assertEqual(spilt_sentence_to_array('你好 are  u 可以'), ['你好', 'are', 'u', '可以'])
        self.assertEqual(spilt_sentence_to_array('你好 are  u 可以', True), ['你', '好', 'are', 'u', '可', '以'])

    def test_join_words_array_to_sentence(self):
        self.assertEqual(join_words_array_to_sentence(['你好', 'are', "可以"]), "你好are可以")

    def test_passage_into_chunk(self):
        self.assertEqual(passage_into_chunk("xxxxxxxx\noo\nyyzz\ngggggg\nkkkk\n", 10),
                         ['xxxxxxxx oo ', 'yyzz gggggg ', 'kkkk '])

    def test_is_all_english(self):
        self.assertTrue(is_all_english("1SGD"))
        self.assertFalse(is_all_english("1SG哦"))

    def test_is_contain_number(self):
        self.assertTrue(is_contain_number("1SGD"))
        self.assertFalse(is_contain_number("SG哦"))

    def test_is_contain_english(self):
        self.assertTrue(is_contain_english("1SGD"))
        self.assertFalse(is_contain_english("1哦"))

    def test_is_list_contain_string(self):
        self.assertFalse(is_list_contain_string("a", ['bdc', 'dcd']))
        self.assertTrue(is_list_contain_string("a", ['a', 'dcd']))
        self.assertTrue(is_list_contain_string("a", ['abcd', 'dcd']))

    def test_full2half(self):
        self.assertEqual(full2half("，,"), ",,")

    def test_half2full(self):
        self.assertEqual(half2full("，,"), "，，")

    if __name__ == '__main__':
        unittest.main()
