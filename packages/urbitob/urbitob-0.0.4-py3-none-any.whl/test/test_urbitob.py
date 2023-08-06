import unittest
from urbitob.co import (
    patp,
    patq,
    clan,
    sein,
    hex_to_patp,
    hex_to_patq,
    patq_to_hex,
    patp_to_hex,
    patq_to_num,
    patp_to_num,
    eq_patq,
    is_valid_patp,
    is_valid_patq,
)


class TestPat(unittest.TestCase):
    def test_patp(self):
        self.assertEqual(patp(0), "~zod")
        self.assertEqual(patp(255), "~fes")
        self.assertEqual(patp(256), "~marzod")
        self.assertEqual(patp(65535), "~fipfes")
        self.assertEqual(patp(65536), "~dapnep-ronmyl")
        self.assertEqual(patp(14287616), "~rosmur-hobrem")
        self.assertEqual(patp(14287617), "~sallus-nodlut")
        self.assertEqual(patp(14287618), "~marder-mopdur")
        self.assertEqual(patp(14287619), "~laphec-savted")
        self.assertEqual(patp(4294967295), "~dostec-risfen")
        self.assertEqual(patp(4294967296), "~doznec-dozzod-dozzod")

    def test_patq(self):
        self.assertEqual(patq(0), "~zod")
        self.assertEqual(patq(255), "~fes")
        self.assertEqual(patq(256), "~marzod")
        self.assertEqual(patq(65535), "~fipfes")
        self.assertEqual(patq(65536), "~doznec-dozzod")
        self.assertEqual(patq(14287616), "~dozler-wanzod")
        self.assertEqual(patq(14287617), "~dozler-wannec")
        self.assertEqual(patq(14287618), "~dozler-wanbud")
        self.assertEqual(patq(14287619), "~dozler-wanwes")
        self.assertEqual(patq(4294967295), "~fipfes-fipfes")
        self.assertEqual(patq(4294967296), "~doznec-dozzod-dozzod")


class TestClan(unittest.TestCase):
    def test_clan(self):
        self.assertEqual(clan("~zod"), "galaxy")
        self.assertEqual(clan("~fes"), "galaxy")
        self.assertEqual(clan("~marzod"), "star")
        self.assertEqual(clan("~fipfes"), "star")
        self.assertEqual(clan("~dapnep-ronmyl"), "planet")
        self.assertEqual(clan("~rosmur-hobrem"), "planet")
        self.assertEqual(clan("~sallus-nodlut"), "planet")
        self.assertEqual(clan("~marder-mopdur"), "planet")
        self.assertEqual(clan("~laphec-savted"), "planet")
        self.assertEqual(clan("~dostec-risfen"), "planet")
        self.assertEqual(clan("~divrul-dalred-samhec-sidrex"), "moon")
        self.assertEqual(
            clan("~dotmec-niblyd-tocdys-ravryg--panper-hilsug-nidnev-marzod"), "comet"
        )
        self.assertRaisesRegex(ValueError, "Invalid @p", clan, "abcdefg")


class TestSein(unittest.TestCase):
    def test_sein(self):
        self.assertEqual(sein("~zod"), "~zod")
        self.assertEqual(sein("~fes"), "~fes")
        self.assertEqual(sein("~marzod"), "~zod")
        self.assertEqual(sein("~fipfes"), "~fes")
        self.assertEqual(sein("~dapnep-ronmyl"), "~zod")
        self.assertEqual(sein("~rosmur-hobrem"), "~wanzod")
        self.assertEqual(sein("~sallus-nodlut"), "~wannec")
        self.assertEqual(sein("~marder-mopdur"), "~wanbud")
        self.assertEqual(sein("~laphec-savted"), "~wanwes")
        self.assertEqual(sein("~dostec-risfen"), "~fipfes")
        self.assertEqual(sein("~divrul-dalred-samhec-sidrex"), "~samhec-sidrex")
        self.assertEqual(
            sein("~dotmec-niblyd-tocdys-ravryg--panper-hilsug-nidnev-marzod"), "~zod"
        )
        self.assertRaisesRegex(ValueError, "Invalid @p", sein, "abcdefg")


class TestPatToNum(unittest.TestCase):
    def test_patq_to_num(self):
        self.assertEqual(patq_to_num("~zod"), 0)
        self.assertEqual(patq_to_num("~fes"), 255)
        self.assertEqual(patq_to_num("~marzod"), 256)
        self.assertEqual(patq_to_num("~fipfes"), 65535)
        self.assertEqual(patq_to_num("~doznec-dozzod"), 65536)
        self.assertEqual(patq_to_num("~dozler-wanzod"), 14287616)
        self.assertEqual(patq_to_num("~dozler-wannec"), 14287617)
        self.assertEqual(patq_to_num("~dozler-wanbud"), 14287618)
        self.assertEqual(patq_to_num("~dozler-wanwes"), 14287619)
        self.assertEqual(patq_to_num("~fipfes-fipfes"), 4294967295)
        self.assertEqual(patq_to_num("~doznec-dozzod-dozzod"), 4294967296)
        self.assertRaisesRegex(ValueError, "Invalid @p", patq_to_num, "abcdefg")

    def test_patp_to_num(self):
        self.assertEqual(patp_to_num("~zod"), 0)
        self.assertEqual(patp_to_num("~fes"), 255)
        self.assertEqual(patp_to_num("~marzod"), 256)
        self.assertEqual(patp_to_num("~fipfes"), 65535)
        self.assertEqual(patp_to_num("~dapnep-ronmyl"), 65536)
        self.assertEqual(patp_to_num("~rosmur-hobrem"), 14287616)
        self.assertEqual(patp_to_num("~sallus-nodlut"), 14287617)
        self.assertEqual(patp_to_num("~marder-mopdur"), 14287618)
        self.assertEqual(patp_to_num("~laphec-savted"), 14287619)
        self.assertEqual(patp_to_num("~dostec-risfen"), 4294967295)
        self.assertEqual(patp_to_num("~doznec-dozzod-dozzod"), 4294967296)
        self.assertRaisesRegex(ValueError, "Invalid @p", patp_to_num, "abcdefg")


class TestPatToHex(unittest.TestCase):
    def test_patp_to_hex(self):
        self.assertEqual(patp_to_hex("~zod"), "00")
        self.assertEqual(patp_to_hex("~fes"), "ff")
        self.assertEqual(patp_to_hex("~marzod"), "0100")
        self.assertEqual(patp_to_hex("~fipfes"), "ffff")
        self.assertEqual(patp_to_hex("~dapnep-ronmyl"), "010000")
        self.assertEqual(patp_to_hex("~rosmur-hobrem"), "da0300")
        self.assertEqual(patp_to_hex("~sallus-nodlut"), "da0301")
        self.assertEqual(patp_to_hex("~marder-mopdur"), "da0302")
        self.assertEqual(patp_to_hex("~laphec-savted"), "da0303")
        self.assertEqual(patp_to_hex("~dostec-risfen"), "ffffffff")
        self.assertEqual(patp_to_hex("~doznec-dozzod-dozzod"), "0100000000")
        self.assertRaisesRegex(ValueError, "Invalid @p", patp_to_hex, "abcdefg")

    def test_patq_to_hex(self):
        self.assertEqual(patq_to_hex("~zod"), "00")
        self.assertEqual(patq_to_hex("~fes"), "ff")
        self.assertEqual(patq_to_hex("~marzod"), "0100")
        self.assertEqual(patq_to_hex("~fipfes"), "ffff")
        self.assertEqual(patq_to_hex("~doznec-dozzod"), "00010000")
        self.assertEqual(patq_to_hex("~dozler-wanzod"), "00da0300")
        self.assertEqual(patq_to_hex("~dozler-wannec"), "00da0301")
        self.assertEqual(patq_to_hex("~dozler-wanbud"), "00da0302")
        self.assertEqual(patq_to_hex("~dozler-wanwes"), "00da0303")
        self.assertEqual(patq_to_hex("~fipfes-fipfes"), "ffffffff")
        self.assertEqual(patq_to_hex("~doznec-dozzod-dozzod"), "000100000000")
        self.assertRaisesRegex(ValueError, "Invalid @p", patq_to_hex, "abcdefg")


class TestHexToPat(unittest.TestCase):
    def test_hex_to_patq(self):
        self.assertEqual(hex_to_patq("00"), "~zod")
        self.assertEqual(hex_to_patq("ff"), "~fes")
        self.assertEqual(hex_to_patq("0100"), "~marzod")
        self.assertEqual(hex_to_patq("ffff"), "~fipfes")
        self.assertEqual(hex_to_patq("00010000"), "~doznec-dozzod")
        self.assertEqual(hex_to_patq("00da0300"), "~dozler-wanzod")
        self.assertEqual(hex_to_patq("00da0301"), "~dozler-wannec")
        self.assertEqual(hex_to_patq("00da0302"), "~dozler-wanbud")
        self.assertEqual(hex_to_patq("00da0303"), "~dozler-wanwes")
        self.assertEqual(hex_to_patq("ffffffff"), "~fipfes-fipfes")
        self.assertEqual(hex_to_patq("000100000000"), "~doznec-dozzod-dozzod")
        self.assertEqual(
            hex_to_patq("01010101010101010102"), "~marnec-marnec-marnec-marnec-marbud"
        )
        self.assertEqual(
            hex_to_patq(
                "6d7920617765736f6d65207572626974207469636b65742c206920616d20736f206c75636b79"
            ),
            "~tastud-holruc-sidwet-salpel-taswet-holdeg-paddec-davdut-holdut-davwex-balwet-divwen-holdet-holruc"
            "-taslun-salpel-holtux-dacwex-baltud",
        )

    def test_hex_to_patp(self):
        self.assertEqual(hex_to_patp("00"), "~zod")
        self.assertEqual(hex_to_patp("ff"), "~fes")
        self.assertEqual(hex_to_patp("0100"), "~marzod")
        self.assertEqual(hex_to_patp("ffff"), "~fipfes")
        self.assertEqual(hex_to_patp("010000"), "~dapnep-ronmyl")
        self.assertEqual(hex_to_patp("da0300"), "~rosmur-hobrem")
        self.assertEqual(hex_to_patp("da0301"), "~sallus-nodlut")
        self.assertEqual(hex_to_patp("da0302"), "~marder-mopdur")
        self.assertEqual(hex_to_patp("da0303"), "~laphec-savted")
        self.assertEqual(hex_to_patp("ffffffff"), "~dostec-risfen")
        self.assertEqual(hex_to_patp("0100000000"), "~doznec-dozzod-dozzod")
        self.assertEqual(
            hex_to_patp(
                "7468697320697320736f6d6520766572792068696768207175616c69747920656e74726f7079"
            ),
            "~divmes-davset-holdet--sallun-salpel-taswet-holtex--watmeb-tarlun-picdet-magmes--holter-dacruc-timdet"
            "-divtud--holwet-maldut-padpel-sivtud",
        )


class TestEqPat(unittest.TestCase):
    def test_eq_patq(self):
        self.assertEqual(eq_patq("~dozzod-dozzod", "~zod"), True)
        self.assertEqual(eq_patq("~dozzod-mardun", "~mardun"), True)
        self.assertEqual(eq_patq("~dozzod-mardun", "~mardun-dozzod"), False)
        self.assertRaisesRegex(ValueError, "Invalid @p", eq_patq, "~zod", "abcdefg")


class TestIsValidPat(unittest.TestCase):
    def test_is_valid_patp(self):
        self.assertEqual(is_valid_patp("~zod"), True)
        self.assertEqual(is_valid_patp("~marzod"), True)
        self.assertEqual(is_valid_patp("~nidsut-tomdun"), True)
        self.assertEqual(is_valid_patp(""), False)
        self.assertEqual(is_valid_patp("~"), False)
        self.assertEqual(is_valid_patp("~hu"), False)
        self.assertEqual(is_valid_patp("~what"), False)
        self.assertEqual(is_valid_patp("sudnit-duntom"), False)

    def test_is_valid_patq(self):
        self.assertEqual(is_valid_patq("~zod"), True)
        self.assertEqual(is_valid_patq("~marzod"), True)
        self.assertEqual(is_valid_patq("~nidsut-tomdun"), True)
        self.assertEqual(is_valid_patq("~dozzod-binwes-nidsut-tomdun"), True)
        self.assertEqual(is_valid_patq(""), False)
        self.assertEqual(is_valid_patq("~"), False)
        self.assertEqual(is_valid_patq("~hu"), False)
        self.assertEqual(is_valid_patq("~what"), False)
        self.assertEqual(is_valid_patq("sudnit-duntom"), False)


# TODO is there a better way to do this
class TestReverse(unittest.TestCase):
    def test_patq_reverse(self):
        for i in range(0x9000, 0x12000, 7):
            self.assertEqual(patq_to_num(patq(i)), i)

    def test_patp_reverse(self):
        for i in range(0x9000, 0x12000, 7):
            self.assertEqual(patp_to_num(patp(i)), i)


if __name__ == "__main__":
    unittest.main()
