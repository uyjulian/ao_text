from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0510.bin",                # FileName
        "e0510",                    # MapName
        "e0510",                    # Location
        0x00A1,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0510",                  # 0
        "Elie",                   # 1
        "Noｱl",                  # 2
        "Randy",                  # 3
        "Crewman Salsa",          # 4
        "Citizen",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Melson",                 # 8
        "Rimah",                  # 9
        "Corona",                 # 10
        "Fran",                   # 11
        "Cecil",                  # 12
        "Ilya",                   # 13
        "Rixia",                  # 14
        "Sully",                  # 15
        "Mariabell",              # 16
        "Zeit",                   # 17
        "SE制御",                 # 18
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch02900.itc",                   # 01
        "chr/ch00302.itc",                   # 02
        "chr/ch28400.itc",                   # 03
        "chr/ch33002.itc",                   # 04
        "chr/ch20402.itc",                   # 05
        "chr/ch22102.itc",                   # 06
        "chr/ch26202.itc",                   # 07
        "chr/ch22702.itc",                   # 08
        "chr/ch20702.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    388,  0x0, 1,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(4294967196, 0,       4294951876, 0,    389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294964846, 150,     4294963497, 180,  453,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(4294964846, 150,     4294960847, 180,  453,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(4294963846, 150,     4294960847, 180,  453,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(4294964247, 150,     4294955946, 180,  389,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(4294963546, 150,     4294955946, 180,  389,  0x0, 0,   9,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4294965046, 150,     4294955946, 180,  389,  0x0, 0,   8,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(844, 0)                                        # 0

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_3FC",          # 01, 1
        "Function_2_4FF",          # 02, 2
        "Function_3_554",          # 03, 3
        "Function_4_910",          # 04, 4
        "Function_5_B8D",          # 05, 5
        "Function_6_F19",          # 06, 6
        "Function_7_10DB",         # 07, 7
        "Function_8_1221",         # 08, 8
        "Function_9_12CC",         # 09, 9
        "Function_10_1358",        # 0A, 10
        "Function_11_1544",        # 0B, 11
        "Function_12_1755",        # 0C, 12
        "Function_13_17C7",        # 0D, 13
        "Function_14_2C6D",        # 0E, 14
        "Function_15_3C0B",        # 0F, 15
        "Function_16_3C33",        # 10, 16
        "Function_17_3C5B",        # 11, 17
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_384"),
        (1, "loc_390"),
        (2, "loc_39C"),
        (3, "loc_3A8"),
        (4, "loc_3B4"),
        (5, "loc_3C0"),
        (6, "loc_3CC"),
        (SWITCH_DEFAULT, "loc_3D8"),
    )


    label("loc_384")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_390")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_39C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3FB")

    Return()

    # Function_0_34C end

    def Function_1_3FC(): pass

    label("Function_1_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    SetChrPos(0x8, 630, -1000, 9000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -620, -1000, 9000, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 3250, 150, -9100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrSubChip(0x10, 0x2)

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4FE")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)

    label("loc_4FE")

    Return()

    # Function_1_3FC end

    def Function_2_4FF(): pass

    label("Function_2_4FF")

    Sound(480, 1, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_533")
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553")
    SetChrSubChip(0xA, 0x1)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_553")

    Return()

    # Function_2_4FF end

    def Function_3_554(): pass

    label("Function_3_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B")
    Call(0, 13)
    Return()

    label("loc_56B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_57C")
    Jump("loc_90C")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_58A")
    Jump("loc_90C")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_598")
    Jump("loc_90C")

    label("loc_598")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5A8")
    Jump("loc_90C")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_5B6")
    Jump("loc_90C")

    label("loc_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5C4")
    Jump("loc_90C")

    label("loc_5C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_5D2")
    Jump("loc_90C")

    label("loc_5D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5E0")
    Jump("loc_90C")

    label("loc_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_90C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_90C")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_889")

    ChrTalk(
        0x8,
        (
            "#00100FWe finally got a vacation\x01",
            "so it would be a waste if\x01",
            "we didn't enjoy it.\x02\x03",
            "#00104FI think Bell said she had\x01",
            "a lot of surprises in\x01",
            "store for us as well...\x02\x03",
            "#00102F*giggle*, when I think\x01",
            "about that, I'm really\x01",
            "looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FSurprises, eh...? I'm a little\x01",
            "worried, though.\x02\x03",
            "#00003FIf she did something like have all\x01",
            "of Michelam welcome us, I'd want\x01",
            "to crawl into a hole or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00109FE-Even if Bell likes\x01",
            "showy things, something\x01",
            "like that would be...\x02\x03",
            "#00103F...Not impossible, I\x01",
            "think.\x02\x03",
            "#00102FL-Let's at least pray to\x01",
            "the Goddess that they\x01",
            "aren't weird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(N-Now I'm getting\x01",
            "worried...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_90C")

    label("loc_889")


    ChrTalk(
        0x8,
        (
            "#00103FHmm. Even so, I wonder what\x01",
            "kind of surprises Bell has\x01",
            "in store for us...\x02\x03",
            "#00111F...I hope they're not\x01",
            "weird, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90C")

    TalkEnd(0xFE)
    Return()

    # Function_3_554 end

    def Function_4_910(): pass

    label("Function_4_910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_927")
    Call(0, 13)
    Return()

    label("loc_927")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_938")
    Jump("loc_B89")

    label("loc_938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_946")
    Jump("loc_B89")

    label("loc_946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_954")
    Jump("loc_B89")

    label("loc_954")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_964")
    Jump("loc_B89")

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_972")
    Jump("loc_B89")

    label("loc_972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_980")
    Jump("loc_B89")

    label("loc_980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_98E")
    Jump("loc_B89")

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_99C")
    Jump("loc_B89")

    label("loc_99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_B89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B4")
    Jump("loc_B89")

    label("loc_9B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B01")

    ChrTalk(
        0x9,
        (
            "#10105FBy the way, it's a pity\x01",
            "that Chief Sergei\x01",
            "couldn't come with us.\x02\x03",
            "#10106FHe said to go have fun,\x01",
            "but I feel sorry for\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThe Chief is a very busy\x01",
            "man...\x02\x03",
            "#00002FHaha. Maybe he was simply\x01",
            "embarrassed and didn't want us\x01",
            "to see how he is in private...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10109FAhaha, that might be\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_B89")

    label("loc_B01")


    ChrTalk(
        0x9,
        (
            "#10103FIt's too bad Chief\x01",
            "Sergei couldn't come\x01",
            "with us, huh.\x02\x03",
            "#10102FI think he's smoking\x01",
            "alone at the Support\x01",
            "Section around now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B89")

    TalkEnd(0xFE)
    Return()

    # Function_4_910 end

    def Function_5_B8D(): pass

    label("Function_5_B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA4")
    Call(0, 14)
    Return()

    label("loc_BA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_BB5")
    Jump("loc_F15")

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BC3")
    Jump("loc_F15")

    label("loc_BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_BD1")
    Jump("loc_F15")

    label("loc_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_BDF")
    Jump("loc_F15")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BED")
    Jump("loc_F15")

    label("loc_BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_BFB")
    Jump("loc_F15")

    label("loc_BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C09")
    Jump("loc_F15")

    label("loc_C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C21")
    Jump("loc_F15")

    label("loc_C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6A")

    ChrTalk(
        0xA,
        (
            "#00303FAck, boring stuff really\x01",
            "isn't in my character.\x02\x03",
            "#00301FIn that case, I'm gonna\x01",
            "enjoy Michelam to the\x01",
            "fullest today!\x02\x03",
            "#00309FLloyd, you'll come with\x01",
            "me to pick up girls\x01",
            "tonight, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha, well if you're fine\x01",
            "with me leaving the picking\x01",
            "up entirely to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00306FWhat the, how unmotivated you are.\x02\x03",
            "#00309FYou're a diamond in the rough yourself, so\x01",
            "you might as well grow out that younger\x01",
            "brother character and get popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I don't get what you\x01",
            "mean...\x02\x03",
            "#00000F(...However, he seems to\x01",
            "have gone back to his\x01",
            "usual self.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_F0D")

    label("loc_E6A")


    ChrTalk(
        0xA,
        (
            "#00305FOh, right, I've gotta buy a\x01",
            "present for her too...\x02\x03",
            "#00304FShe was talkin' about a promotion,\x01",
            "so I guess I'll pick up a\x01",
            "congratulatory gift somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0D")

    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x1)
    Return()

    label("loc_F15")

    TalkEnd(0xFE)
    Return()

    # Function_5_B8D end

    def Function_6_F19(): pass

    label("Function_6_F19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_F2A")
    Jump("loc_10D7")

    label("loc_F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_F38")
    Jump("loc_10D7")

    label("loc_F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F46")
    Jump("loc_10D7")

    label("loc_F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_10D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1034")

    ChrTalk(
        0xB,
        (
            "Thank you very much for\x01",
            "using the water bus\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You are the people\x01",
            "invited by Lady\x01",
            "Mariabell, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It is just a short trip to\x01",
            "Michelam, so please enjoy a\x01",
            "relaxing trip lulled by the waves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10D7")

    label("loc_1034")


    ChrTalk(
        0xB,
        (
            "When you are seasick, gazing at\x01",
            "the distant scenery on the deck is\x01",
            "a good way to distract yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Rest assured, we also\x01",
            "have remedies for\x01",
            "seasickness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D7")

    TalkEnd(0xFE)
    Return()

    # Function_6_F19 end

    def Function_7_10DB(): pass

    label("Function_7_10DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_121D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B0")

    ChrTalk(
        0xC,
        (
            "I was really surprised by\x01",
            "the independence proposal\x01",
            "at the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wonder to what extent Mr. Dieter\x01",
            "intends to make that a reality...\x01",
            "I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_121D")

    label("loc_11B0")


    ChrTalk(
        0xC,
        (
            "I wonder to what extent Mr. Dieter\x01",
            "intends to make independence a\x01",
            "reality... I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121D")

    TalkEnd(0xFE)
    Return()

    # Function_7_10DB end

    def Function_8_1221(): pass

    label("Function_8_1221")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_12C8")

    ChrTalk(
        0xD,
        (
            "The trip to Crossbell I\x01",
            "dreamt of, the Michelam\x01",
            "Health Resort theme park!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Maaan, I can't wait. My\x01",
            "girlfriend and I will\x01",
            "enjoy it to the fullest!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C8")

    TalkEnd(0xFE)
    Return()

    # Function_8_1221 end

    def Function_9_12CC(): pass

    label("Function_9_12CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1354")

    ChrTalk(
        0xE,
        (
            "Personally, I'd like to\x01",
            "go to the restaurant and\x01",
            "the boutique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uhuhu, today I'll let my\x01",
            "boyfriend spoil me a\x01",
            "lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1354")

    TalkEnd(0xFE)
    Return()

    # Function_9_12CC end

    def Function_10_1358(): pass

    label("Function_10_1358")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1369")
    Jump("loc_1540")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1377")
    Jump("loc_1540")

    label("loc_1377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1385")
    Jump("loc_1540")

    label("loc_1385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1393")
    Jump("loc_1540")

    label("loc_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A0")

    ChrTalk(
        0xF,
        (
            "Crossbell independence... As\x01",
            "expected from Mr. Dieter, no\x01",
            "one else could've imagined it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It won't be easy, but...\x01",
            "There's a dream in those\x01",
            "words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The Mayor will make Crossbell\x01",
            "shine brightly for sure. I\x01",
            "just have that feeling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1540")

    label("loc_14A0")


    ChrTalk(
        0xF,
        (
            "Whoops, I've come to have fun with\x01",
            "my family, so maybe I shouldn't\x01",
            "talk about these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Today, I have to have a\x01",
            "lot of fun with Rimah\x01",
            "and Corona.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1540")

    TalkEnd(0xFE)
    Return()

    # Function_10_1358 end

    def Function_11_1544(): pass

    label("Function_11_1544")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1555")
    Jump("loc_1751")

    label("loc_1555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1563")
    Jump("loc_1751")

    label("loc_1563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1571")
    Jump("loc_1751")

    label("loc_1571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_157F")
    Jump("loc_1751")

    label("loc_157F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1751")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D2")

    ChrTalk(
        0x11,
        (
            "Since my husband received a bonus\x01",
            "after the completion of Orchis Tower,\x01",
            "we came here for a family trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I actually wanted to add it to our savings, but\x01",
            "in the end I was convinced by my husband who\x01",
            "wanted to treat the family every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "However, I'm really glad\x01",
            "we came. Rimah is so\x01",
            "happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1751")

    label("loc_16D2")


    ChrTalk(
        0x11,
        (
            "Since my husband received\x01",
            "a bonus, we came here for\x01",
            "a family trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Haha, I'm really glad we\x01",
            "came. Rimah is so happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1751")

    TalkEnd(0xFE)
    Return()

    # Function_11_1544 end

    def Function_12_1755(): pass

    label("Function_12_1755")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1766")
    Jump("loc_17C3")

    label("loc_1766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1774")
    Jump("loc_17C3")

    label("loc_1774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1782")
    Jump("loc_17C3")

    label("loc_1782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1790")
    Jump("loc_17C3")

    label("loc_1790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_17C3")

    ChrTalk(
        0x10,
        (
            "Papaaa, look, look! A\x01",
            "fishie jumped!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C3")

    TalkEnd(0xFE)
    Return()

    # Function_12_1755 end

    def Function_13_17C7(): pass

    label("Function_13_17C7")

    EventBegin(0x0)
    SoundLoad(3515)
    SoundLoad(3394)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    Fade(500)
    OP_68(700, 200, 8350, 0)
    MoveCamera(15, 33, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33390, 0)
    OP_64(0x8)
    OP_64(0x9)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x8, 500, -1000, 9000, 230)
    SetChrPos(0x9, -500, -1000, 9000, 80)
    SetChrPos(0x101, 1500, -1000, 8200, 315)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_18D5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18D5)
    Sleep(50)

    def lambda_18E5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_18E5)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x9,
        "#30W#3515VAh, Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x1, 0x80000000)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sound(2189, 255, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        "#30WYou went out on deck?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#12PYeah, to catch the\x01",
            "breeze.\x02\x03",
            "#00005FUhhm, did I disturb you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00108F#5PAh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10106F#5P...Umm, I wanted to talk to\x01",
            "you about what happened during\x01",
            "the trade conference...\x02\x03",
            "#10113FAnd about Mayor Dieter's\x01",
            "proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PProposal...\x01",
            ""Independence as a\x01",
            "state", you mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00106F#5PYes... To me, it's not\x01",
            "just someone else's\x01",
            "problem.\x02\x03",
            "#00108FI can't believe "uncle"\x01",
            "was thinking about\x01",
            "something like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10106F#5PMe too... Honestly, I\x01",
            "feel this isn't just\x01",
            "somebody else's problem.\x02\x03",
            "#10108FBecause it involves the\x01",
            "continued existence of\x01",
            "the CGF as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PI see... The Empire and Republic will\x01",
            "demand a reduction of the Crossbell\x01",
            "Guardian Force, won't they.\x02\x03",
            "#00013FIn exchange, they say they'll station\x01",
            "their own troops at Tangram and\x01",
            "Bellguard gates...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00103F#5PYes...\x02\x03",
            "#00108FNo matter how I look at it, I can only\x01",
            "regard it as a plot to extract even\x01",
            "more wealth from Crossbell.\x02\x03",
            "#00101FThen, if there's a chance, they'll aim\x01",
            "for each other's weaknesses, annex us\x01",
            "and have Crossbell all to themselves...\x02\x03",
            "#00106FI can only think it's in preparation\x01",
            "for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PIndeed...\x02\x03",
            "#00001F...Then, the Mayor's\x01",
            "proposal is an idea to\x01",
            "counter that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10103F#5PYes. With state independence, we could\x01",
            "improve the CGF's weapons, which have\x01",
            "been restricted by the major powers.\x02\x03",
            "#10101FNot just anti-personnel weapons, but\x01",
            "also tanks and military airships to\x01",
            "repel other nations' invasions.\x02\x03",
            "#10106F...Although, I feel a little bad to\x01",
            "think of it in those terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PNoｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00103F#5PHowever, I don't know if "uncle's"\x01",
            "proposal is realistic or now...\x02\x03",
            "#00108FThe Empire and Republic are\x01",
            "publishing statements in opposition\x01",
            "immediately.\x02\x03",
            "#00100FHowever, the proposal was received\x01",
            "favorably by Liberl, Remiferia, the\x01",
            "Holy Nation of Arteria and others...\x02\x03",
            "#00106FHonestly, it's a complicated\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10113F#5P...What do you make of\x01",
            "Mariabell's invitation\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#00106F#11PIf I had to say, she seems to\x01",
            "be focusing on the management\x01",
            "of IBC at present.\x02\x03",
            "#00108FIt seems like she didn't have\x01",
            "much to do with the proposal.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#10106F#6PI see...\x02\x03",
            "#10108F...We don't see her too\x01",
            "often, so I was thinking\x01",
            "of asking her about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00103F#11PIndeed... There are many\x01",
            "things I'd like to ask\x01",
            "Bell as well...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#12P─Say, you two.\x02\x03",
            "#00000FWe won't get many chances\x01",
            "like this. Shouldn't we\x01",
            "enjoy it to the fullest?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_241D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_241D)
    Sleep(50)

    def lambda_242D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_242D)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)

    ChrTalk(
        0x8,
        "#00105F#5PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10105F#5P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12POn a rare day off, we're\x01",
            "staying at the Michelam\x01",
            "hotel, right?\x02\x03",
            "And she said we can have\x01",
            "as much fun as we want\x01",
            "at the theme park.\x02\x03",
            "#00009FSurely we can empty our\x01",
            "minds for that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00106F#5P#30WB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10108F#5P#30W...After such a thing\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PPrecisely because it\x01",
            "happened.\x02\x03",
            "#00003FI don't know what's going\x01",
            "to happen to Crossbell in\x01",
            "the coming days...\x02\x03",
            "It's likely our job will\x01",
            "get a lot harder.\x02\x03",
            "#00002FThat's exactly why, how\x01",
            "to say it... I want to\x01",
            "make "memories".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#00112F#5PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10114F#5PD-Does that mean...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#12P(...Huh? Why are they\x01",
            "reacting that much?)\x02\x03",
            "#00012FHaha... I guess it was\x01",
            "too cheesy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10112F#5PRather than too\x01",
            "cheesy...\x02\x03",
            "#10108F(Elie... Is he doing it\x01",
            "on purpose?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00111F#5P(No... Most likely it's\x01",
            "natural...)\x02\x03",
            "#00113F─Umm, Lloyd?\x02\x03",
            "#00112FThose "memories"... They\x01",
            "don't have to do with anyone\x01",
            "in particular, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#12P? Of course not, but...\x02\x03",
            "#00000FI was just thinking we\x01",
            "don't have many chances to\x01",
            "take a day off together.\x02\x03",
            "#00012FHaha. Too bad about chief,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#00113F#5P*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10112F#5PR-Right. That's Lloyd\x01",
            "for you, I guess...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#12PHuh? Could I be missing\x01",
            "something?\x02\x03",
            "#00006FI saw you feeling down, so\x01",
            "I thought I'd cheer─#500W─\x01",
            "#30W#00011Oh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10102F#5PPfft...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        (
            "#00114F#5PAhaha!\x02\x03",
            "#00116FI-I don't know whether\x01",
            "to call you a natural or\x01",
            "just clumsy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10109F#5PHaha. What I was\x01",
            "worrying about does seem\x01",
            "silly now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#12P...Sorry. I'll leave you\x01",
            "alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00104F#5P*giggle*, don't pout.\x02\x03",
            "#00102F...I'm sorry. We\x01",
            "couldn't read the mood\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10102F#5PThat's right... If you're going\x01",
            "on a vacation, you've got to\x01",
            "enjoy it to the fullest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PYeah... (Mission\x01",
            "accomplished, I guess?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x8, 630, -1000, 9000, 270)
    SetChrPos(0x9, -620, -1000, 9000, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x0, 3000, -1000, 6500, 180)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x144, 2)
    EventEnd(0x5)
    Return()

    # Function_13_17C7 end

    def Function_14_2C6D(): pass

    label("Function_14_2C6D")

    EventBegin(0x0)
    Fade(500)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    OP_68(3170, 1300, -9560, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34500, 0)
    OP_64(0xA)
    SetChrPos(0x101, 800, 0, -9770, 90)
    SetCameraDistance(34000, 1500)
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    OP_0D()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(200)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    Sound(2756, 255, 100, 0)

    AnonymousTalk(
        0xA,
        (
            "#30W─Yo, Lloyd.\x02\x03",
            "#20WBut, Mariabell is pretty generous,\x01",
            "isn't she.\x02\x03",
            "We can enjoy the Michelam resort\x01",
            "hotel and the theme park all we\x01",
            "want.\x02\x03",
            "I mean, how generous can you get?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAC4)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#6P...Yeah.\x02\x03",
            "#00008F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00302F#5PHaha...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#00304F#5P─Say, Lloyd.\x02\x03",
            "#00300FLooks like you're\x01",
            "misunderstandin' something,\x01",
            "so I'll just say this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00303F#5PAbout that terrorist\x01",
            "killing...\x02\x03",
            "#00301FYou're thinkin' I'm in\x01",
            "shock because my family did\x01",
            "something like that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PW-Well...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Not quite.\x02\x03",
            "#00008FI feel like you've got\x01",
            "your own baggage, Randy.\x02\x03",
            "#00001FYou wouldn't obsess over\x01",
            "Sigmund and Shirley that\x01",
            "much, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)
    BeginChrThread(0x19, 1, 0, 15)

    ChrTalk(
        0xA,
        (
            "#00308F#5P...I see.\x02\x03",
            "#00303F#30W............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    SetChrSubChip(0xA, 0x0)
    Sleep(150)
    SetChrSubChip(0xA, 0x1)
    SetCameraDistance(33000, 20000)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#00304F#5P─I had a friend.\x02\x03",
            "One year younger than\x01",
            "me, he had puppy-like\x01",
            "eyes...\x02\x03",
            "#00300FYou could say he was the\x01",
            "first friend I had\x01",
            "outside the corps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00308F#5PStuff happened and he\x01",
            "died...\x02\x03",
            "Really, stuff happened\x01",
            "and I left the corps and\x01",
            "started wandering.\x02\x03",
            "#00303FThen, I came to\x01",
            "Crossbell, joined the\x01",
            "CGF... and met you all...\x02\x03",
            "#00302F...But, that isn't who I\x01",
            "really am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00312F#5P─It's like my uncle said. To me,\x01",
            "the killing of a few terrorists\x01",
            "isn't all that unusual.\x02\x03",
            "Indeed, extermination battles\x01",
            "like that were an everyday\x01",
            "occurrence on the battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00303F#5PI snapped then... Not out\x01",
            "of righteous indignation.\x02\x03",
            "Not even because I was mad\x01",
            "at my uncle, though I do\x01",
            "pity those terrorists.\x02\x03",
            "#00308F#30WI─ Even if two years 've\x01",
            "passed, I haven't changed\x01",
            "at all...\x02\x03",
            "I was only deeply shocked\x01",
            "that I'm nothing more than\x01",
            "a jaeger to the core.\x02\x03",
            "#00306FAnd so, to vent my anger,\x01",
            "I grabbed 'im and was\x01",
            "knocked down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PI see....\x02\x03",
            "#00006FThat was indeed lame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00302F#5PHaha, I know, right?\x02\x03",
            "#00306FHonestly. Me, a cool\x01",
            "dude, doin' such an\x01",
            "unsightly─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P...But, you know. I\x01",
            "guess I'm a little\x01",
            "happy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xA, 0x0)
    Sleep(120)
    SetChrSubChip(0xA, 0x2)
    Sleep(250)

    ChrTalk(
        0xA,
        "#00305F#5PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHow to say it, because you're all\x01",
            "adult and composed, I've been counting\x01",
            "on you this whole time, right?\x02\x03",
            "#00000FBut, it makes me a little happy to be\x01",
            "a friend you can expose yourself to\x01",
            "like that.\x02\x03",
            "And not just me either... Everyone\x01",
            "else too, probably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00305F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PAlso... Thinking you're a jaeger to the\x01",
            "core... Aren't you selling yourself\x01",
            "short?\x02\x03",
            "#00008FAt least to me, you don't seem the type\x01",
            "to undertake wars for mira.\x02\x03",
            "#00000FYou get carried away, like nightlife,\x01",
            "are a little belligerent, and often get\x01",
            "passionate, but you know when to quit...\x02\x03",
            "#00002FAnd, you're the senior member who's\x01",
            "always helping us juniors...\x02\x03",
            "#00009FThat's the Randy Orlando I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00305F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PThat's why you don't have to\x01",
            "be worried about showing us\x01",
            "a little of your lame side.\x02\x03",
            "#00000FRather, I, Elie and the\x01",
            "others would─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00303F#5P─I got it, don't finish.\x02\x03",
            "#00306FLooks like I didn't take\x01",
            "your potential\x01",
            "seriously...\x02\x03",
            "#00310FHow much of a ladies'\x01",
            "man are you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PL-Ladies' man?\x02\x03",
            "#00006FI don't get it, but did\x01",
            "I make you that upset?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x19, 1, 0, 16)

    ChrTalk(
        0xA,
        (
            "#00315F#5PAh, jeez, I'm feelin' stupid\x01",
            "for bein' depressed...\x02\x03",
            "#00306FIf that's how it's going to\x01",
            "be, I'm gonna live it up at\x01",
            "Michelam!\x02\x03",
            "#00301FI'll play all day in the\x01",
            "theme park and then flirt\x01",
            "with all the girls at night!\x02\x03",
            "#00307FAnd you're coming with me,\x01",
            "ya damn younger brother!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PR-Roger.\x02\x03",
            "#00002F(I don't really get it,\x01",
            "but... I guess I cheered\x01",
            "him up?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 980, 0, -10170, 270)
    SetChrSubChip(0xA, 0x1)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x144, 3)
    EventEnd(0x5)
    Return()

    # Function_14_2C6D end

    def Function_15_3C0B(): pass

    label("Function_15_3C0B")

    OP_25(0x1E0, 0x5A)
    Sleep(200)
    OP_25(0x1E0, 0x50)
    Sleep(200)
    OP_25(0x1E0, 0x46)
    Sleep(200)
    OP_25(0x1E0, 0x3C)
    Sleep(200)
    OP_25(0x1E0, 0x32)
    Sleep(200)
    OP_25(0x1E0, 0x28)
    Return()

    # Function_15_3C0B end

    def Function_16_3C33(): pass

    label("Function_16_3C33")

    OP_25(0x1E0, 0x32)
    Sleep(200)
    OP_25(0x1E0, 0x3C)
    Sleep(200)
    OP_25(0x1E0, 0x46)
    Sleep(200)
    OP_25(0x1E0, 0x50)
    Sleep(200)
    OP_25(0x1E0, 0x5A)
    Sleep(200)
    OP_25(0x1E0, 0x64)
    Return()

    # Function_16_3C33 end

    def Function_17_3C5B(): pass

    label("Function_17_3C5B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08502.itc", 0x1E)
    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    LoadChrToIndex("chr/ch05102.itc", 0x20)
    LoadChrToIndex("chr/ch07502.itc", 0x21)
    LoadChrToIndex("chr/ch10002.itc", 0x22)
    LoadChrToIndex("chr/ch05502.itc", 0x23)
    LoadChrToIndex("chr/ch05602.itc", 0x24)
    LoadChrToIndex("chr/ch00102.itc", 0x25)
    LoadChrToIndex("chr/ch00202.itc", 0x26)
    LoadChrToIndex("chr/ch02902.itc", 0x28)
    LoadChrToIndex("chr/ch03002.itc", 0x29)
    LoadChrToIndex("chr/ch02702.itc", 0x2A)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x26)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x2)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x1)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x18, 1, 0, 0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x2)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrFlags(0x101, 0x8)
    SetChrPos(0x102, 1000, -800, 7350, 0)
    SetChrPos(0x17, 0, -800, 7350, 0)
    SetChrPos(0x103, -2200, 150, -13850, 180)
    SetChrPos(0x18, -1200, 0, -14850, 270)
    SetChrPos(0x104, -3550, 150, -3850, 180)
    SetChrPos(0x105, -2350, 150, -3850, 180)
    SetChrPos(0x109, 2100, 150, -11350, 180)
    SetChrPos(0x12, 3250, 150, -11350, 180)
    SetChrPos(0x15, -3550, 150, -8850, 180)
    SetChrPos(0x16, -2350, 150, -8850, 180)
    SetChrPos(0x14, 2100, 150, -8850, 180)
    SetChrPos(0x13, 3250, 150, -8850, 180)
    OP_68(0, 1000, -15000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, 10000, 20000)
    Sleep(14000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3C5B end

    SaveToFile()

Try(main)
