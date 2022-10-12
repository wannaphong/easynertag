# -*- coding: utf-8 -*-
import unittest

from easynertag import Engine


def simple_pos(data):
    _temp = []
    for w in data:
        if w in ["เรา", "เวลา"]:
            _temp.append((w,"N"))
        elif w in ["ไป", "นอน"]:
            _temp.append((w,"V"))
        else:
            _temp.append((w,"N"))
    return _temp


class TestTagPackage(unittest.TestCase):
    def test_Engine(self):
        self.e = Engine(pos_tag=simple_pos)
        self.simple_data="""เรา ไป เวลา [time]10.04 น.[/time]
        [time]สี่ ทุ่ม ครึ่ง[/time] ได้ เวลา นอน""".splitlines()
        self.assertEqual(
            self.e.text2conll2002(self.simple_data[0],pos=True),
            'เรา\tN\tO\nไป\tV\tO\nเวลา\tN\tO\n\tN\tO\n10.04\tN\tB-time\nน.\tN\tI-time'
        )
        self.assertEqual(
            self.e.text2conll2002(self.simple_data[1],pos=True),
            '\tN\tO\n\tN\tO\n\tN\tO\n\tN\tO\n\tN\tO\n\tN\tO\n\tN\tO\n\tN\tO\n\tN\tO\nสี่\tN\tB-time\nทุ่ม\tN\tI-time\nครึ่ง\tN\tI-time\n\tN\tO\nได้\tN\tO\nเวลา\tN\tO\nนอน\tV\tO'
        )
