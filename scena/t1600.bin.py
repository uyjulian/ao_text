from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1600.bin",                # FileName
        "t1600",                    # MapName
        "t1600",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1600",                  # 0
        "Badgeo",               # 1
        "Suzuku",                 # 2
        "Professor Seyland",         # 3
        "Dyson official",         # 4
        "Nurse Shillon",           # 5
        "Nurse machine",         # 6
        "Arios",               # 7
        "Sergei",               # 8
        "Ursula interchange",           # 9
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch05400.itc",                   # 01
        "chr/ch44800.itc",                   # 02
        "chr/ch20200.itc",                   # 03
        "chr/ch29900.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch05300.itc",                   # 06
    ))

    DeclNpc(4294945317, 6000,    18520,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4294963707, 7000,    11229,   225,  389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4039,    7000,    2160,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(3430,    7000,    4294958137, 180,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294940737, 6000,    14199,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294940737, 6000,    14199,   0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 29,  -13.5,                 20.0,                  5.5,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.75,                  -10.0,                 -1.100000023841858,    1.0])

    DeclActor(17500,   7000,    4294964296, 2000,    18000,   8000,    4294964296, 0x007C, 0,  22, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(712, 0)                                        # 0

    ScpFunction((
        "Function_0_2C8",          # 00, 0
        "Function_1_380",          # 01, 1
        "Function_2_512",          # 02, 2
        "Function_3_5DE",          # 03, 3
        "Function_4_690",          # 04, 4
        "Function_5_9B9",          # 05, 5
        "Function_6_D2E",          # 06, 6
        "Function_7_10C6",         # 07, 7
        "Function_8_1741",         # 08, 8
        "Function_9_1925",         # 09, 9
        "Function_10_1A65",        # 0A, 10
        "Function_11_1D50",        # 0B, 11
        "Function_12_2430",        # 0C, 12
        "Function_13_2ED5",        # 0D, 13
        "Function_14_2EFB",        # 0E, 14
        "Function_15_2F21",        # 0F, 15
        "Function_16_2F47",        # 10, 16
        "Function_17_2F6D",        # 11, 17
        "Function_18_2F93",        # 12, 18
        "Function_19_2FB9",        # 13, 19
        "Function_20_2FDF",        # 14, 20
        "Function_21_3005",        # 15, 21
        "Function_22_302B",        # 16, 22
        "Function_23_318D",        # 17, 23
        "Function_24_3600",        # 18, 24
        "Function_25_364B",        # 19, 25
        "Function_26_3696",        # 1A, 26
        "Function_27_36E1",        # 1B, 27
        "Function_28_372C",        # 1C, 28
        "Function_29_3777",        # 1D, 29
    ))


    def Function_0_2C8(): pass

    label("Function_0_2C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_308"),
        (1, "loc_314"),
        (2, "loc_320"),
        (3, "loc_32C"),
        (4, "loc_338"),
        (5, "loc_344"),
        (6, "loc_350"),
        (SWITCH_DEFAULT, "loc_35C"),
    )


    label("loc_308")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_314")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_320")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_32C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_338")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_344")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_350")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_35C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_368")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_37F")

    Return()

    # Function_0_2C8 end

    def Function_1_380(): pass

    label("Function_1_380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 8450, 7000, -13870, 135)
    Jump("loc_4EE")

    label("loc_3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3C8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 13730, 7000, -3100, 90)
    Jump("loc_4EE")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_411")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -26060, 6000, 14200, 0)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -27060, 6000, 14200, 0)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4EE")

    label("loc_411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_424")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_446")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441")
    SetChrFlags(0x9, 0x10)

    label("loc_441")

    Jump("loc_4EE")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_454")
    Jump("loc_4EE")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_4EE")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47F")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -22110, 6000, 16760, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -20450, 6000, 17030, 315)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4EE")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E0")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4EE")
    ClearChrFlags(0xB, 0x80)

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_502")
    ClearScenarioFlags(0x22, 0)
    Event(0, 23)
    Jump("loc_511")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_511")
    ClearScenarioFlags(0x22, 1)
    Event(0, 12)

    label("loc_511")

    Return()

    # Function_1_380 end

    def Function_2_512(): pass

    label("Function_2_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_524")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A8")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_5BF")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_5BF")

    label("loc_5BF")

    ClearMapObjFlags(0x5, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DD")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5DD")

    Return()

    # Function_2_512 end

    def Function_3_5DE(): pass

    label("Function_3_5DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_68C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FC")
    Call(0, 8)
    Jump("loc_68C")

    label("loc_5FC")


    ChrTalk(
        0x8,
        (
            "A nurse may be nice.\x01",
            "There is no man's nurse.\x01",
            "It will not be ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For my sister in the original bad name\x01",
            "I tried to consult but,\x01",
            "I feel like I've opened the way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68C")

    TalkEnd(0xFE)
    Return()

    # Function_3_5DE end

    def Function_4_690(): pass

    label("Function_4_690")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A5")
    Call(0, 11)
    Jump("loc_9B5")

    label("loc_6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94D")
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11200FBy the way, everyone.\x02\x03",
            "Three days ago Kia-chan\x01",
            "I was in the hospital, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh … that's right.\x01",
            "For a wedding of Shizuoka\x01",
            "Were you going?\x02\x03",
            "#00000FEr, Ka'aa\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11208FNo … … somewhat a bit,\x01",
            "It looked like she was strange\x01",
            "I feel it.\x02\x03",
            "#11203FI mean I'm thinking somewhere ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FKaoru … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FIn front of us,\x01",
            "Show me that swing\x01",
            "There was no ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F…… Ka'aa also,\x01",
            "Anxious about the situation of Crossbell\x01",
            "You may feel it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI see …\x01",
            "For us not to worry\x01",
            "Maybe they are hiding their feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FWell, whatever you care\x01",
            "It seems better to give them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 6)
    Jump("loc_9B5")

    label("loc_94D")


    ChrTalk(
        0x9,
        (
            "#11200FI think that everyone is serious,\x01",
            "Please do your best.\x02\x03",
            "I'll do the same here\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B5")

    TalkEnd(0xFE)
    Return()

    # Function_4_690 end

    def Function_5_9B9(): pass

    label("Function_5_9B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9CA")
    Jump("loc_D2A")

    label("loc_9CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE5")

    ChrTalk(
        0xA,
        (
            "Medical physicians and researchers are total,\x01",
            "The problem of the type of medicine shortage\x01",
            "We are proceeding with countermeasures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although it will not be complete,\x01",
            "I will do my best at any time\x01",
            "It is a duty as a doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As a professor of pharmacy and neurology\x01",
            "Bet on pride and prestige, surely\x01",
            "I swear to the goddess to do something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B93")

    label("loc_AE5")


    ChrTalk(
        0xA,
        (
            "Medical physicians and researchers are total,\x01",
            "The problem of the type of medicine shortage\x01",
            "We are proceeding with countermeasures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As a professor of pharmacy and neurology\x01",
            "Bet on pride and prestige, surely\x01",
            "I swear to the goddess to do something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B93")

    Jump("loc_D2A")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_BA6")
    Jump("loc_D2A")

    label("loc_BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_BB4")
    Jump("loc_D2A")

    label("loc_BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8F")

    ChrTalk(
        0xA,
        (
            "Suzuku\x01",
            "Her sight recovers\x01",
            "The chances are unlimitedly low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… However, as long as the patients do not give up,\x01",
            "I absolutely will not give up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In the name of Seyland ……\x01",
            "Someday, surely I will cure with this hand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D2A")

    label("loc_C8F")


    ChrTalk(
        0xA,
        (
            "Sizuk's vision recovery surgery\x01",
            "If it succeeds, it has similar obstacles\x01",
            "It will be patient's wishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In the name of Seyland ……\x01",
            "Someday, surely I will cure with this hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2A")

    TalkEnd(0xFE)
    Return()

    # Function_5_9B9 end

    def Function_6_D2E(): pass

    label("Function_6_D2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DB1")

    ChrTalk(
        0xB,
        (
            "That huge tree is amazing … …\x01",
            "I can see it from such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… The one-piece crossbell\x01",
            "What will happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C2")

    label("loc_DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_DBF")
    Jump("loc_10C2")

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_F5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC8")

    ChrTalk(
        0xB,
        (
            "In a lecture at a recent research building,\x01",
            "It seems almost impossible to do experiments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Samples can be taken on the highway,\x01",
            "Purchasing from Remiferia\x01",
            "It seems that it is an influence which can not be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As it is, the educational environment of the resident doctors is also\x01",
            "It seems to be getting worse from time to time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F56")

    label("loc_EC8")


    ChrTalk(
        0xB,
        (
            "In a lecture at a recent research building,\x01",
            "It seems almost impossible to do experiments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As it is, the educational environment of the resident doctors is also\x01",
            "It seems to be getting worse from time to time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F56")

    Jump("loc_10C2")

    label("loc_F5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_F69")
    Jump("loc_10C2")

    label("loc_F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104C")

    ChrTalk(
        0xB,
        (
            "While working around here,\x01",
            "Lunch time trainees\x01",
            "I hear rumor story, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Recently, exclusively\x01",
            "Rumors of Professor Seyland are many.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have not much contact with him … …\x01",
            "I wonder what kind of person actually is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_10C2")

    label("loc_104C")


    ChrTalk(
        0xB,
        (
            "Recently, among researchers\x01",
            "Professor Seyland is rumored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have not much contact with him … …\x01",
            "I wonder what kind of person actually is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C2")

    TalkEnd(0xFE)
    Return()

    # Function_6_D2E end

    def Function_7_10C6(): pass

    label("Function_7_10C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10D7")
    Jump("loc_173D")

    label("loc_10D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_10E5")
    Jump("loc_173D")

    label("loc_10E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1100")
    Call(0, 9)
    Jump("loc_113B")

    label("loc_1100")


    ChrTalk(
        0xC,
        (
            "Hey, after all, Meifa\x01",
            "I will depend on you ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113B")

    Jump("loc_173D")

    label("loc_1140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1337")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1282")

    ChrTalk(
        0xC,
        (
            "How to dry today's sheets\x01",
            "I came up to yesterday,\x01",
            "It is a deadly \"overlapping drying\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How, by stacking and stacking two\x01",
            "Simultaneously double sheets\x01",
            "I can dry it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "With this, I am off for today.\x01",
            "Meifa chan's also\x01",
            "It's a perfect cover! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… Anyone, but …\x01",
            "Perhaps it is not dry at all ….?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1332")

    label("loc_1282")


    ChrTalk(
        0xC,
        (
            "Wow, the deadly \"superheated dried\"\x01",
            "Sheets do not dry at all\x01",
            "I found out … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because Mayfa is closed,\x01",
            "I do not have enough for 2 people\x01",
            "I thought, but … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1332")

    Jump("loc_173D")

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1345")
    Jump("loc_173D")

    label("loc_1345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1353")
    Jump("loc_173D")

    label("loc_1353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1361")
    Jump("loc_173D")

    label("loc_1361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_14FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1460")

    ChrTalk(
        0xC,
        (
            "At the time of Miehail 's discharge from this time,\x01",
            "To Mayfa who was crying\x01",
            "I gave you my handkerchief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, suddenly stopped crying,\x01",
            "Ji-ti looks at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, what was it?\x01",
            "Afterwards I will not return handkerchief … ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_14F7")

    label("loc_1460")


    ChrTalk(
        0xC,
        (
            "Meifa, my handkerchief\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "After picking up in the dormitory room before,\x01",
            "Good touch and good design\x01",
            "You liked it ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F7")

    Jump("loc_173D")

    label("loc_14FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1517")
    Call(0, 8)
    Jump("loc_15EA")

    label("loc_1517")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        (
            "Oh, that's right!\x01",
            "Try wearing a nurse for a try?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "Hey, Meifa,\x01",
            "Let me take it off and lend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Or I will not lend! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(Well,\x01",
            "I have not changed my mind … …)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)

    label("loc_15EA")

    Jump("loc_173D")

    label("loc_15EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1734")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B6")

    ChrTalk(
        0xC,
        (
            "Heho, good weather today.\x01",
            "The laundry looks dry as well ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "… …., is not it?\x01",
            "This warmth …\x01",
            "I'm getting sleepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Also, borrow one sheet\x01",
            "I'm afraid I fall asleep.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_172F")

    label("loc_16B6")


    ChrTalk(
        0xC,
        (
            "If you get sunny here\x01",
            "I feel comfortable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Today is Mayfa-chan\x01",
            "I feel like I will not come … ….\x01",
            "Yeah, sleeping um ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172F")

    Jump("loc_173D")

    label("loc_1734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_173D")

    label("loc_173D")

    TalkEnd(0xFE)
    Return()

    # Function_7_10C6 end

    def Function_8_1741(): pass

    label("Function_8_1741")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "The researcher 's exam also fell down … …\x01",
            "Even at home, my shoulders are narrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hey, Shira-neechan.\x01",
            "From now on me, what should I do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "(Bagha … …\x01",
            "To consult Shiron or something,\x01",
            "You are very carefree. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm, that's right ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Same as your sister\x01",
            "Trying to become a nurse?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "Shi, Shiron\x01",
            "It is not Matsumo 's opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see, it's a male nurse ……\x01",
            "I wish it was a blind spot!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_8_1741 end

    def Function_9_1925(): pass

    label("Function_9_1925")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "Shillon, you are …\x01",
            "If you dry the sheets again\x01",
            "Even things dry will not dry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Altogether,\x01",
            "You for years this work\x01",
            "I'm doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Um, with Mefa-chan\x01",
            "Because I entered together, one, I …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Eh, in an unnecessary place\x01",
            "You do not have to answer honestly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Look, I will dry out quickly!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_1925 end

    def Function_10_1A65(): pass

    label("Function_10_1A65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A76")
    Jump("loc_1D4C")

    label("loc_1A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1A84")
    Jump("loc_1D4C")

    label("loc_1A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9F")
    Call(0, 9)
    Jump("loc_1B18")

    label("loc_1A9F")


    ChrTalk(
        0xD,
        (
            "If it is completely silky ……\x01",
            "About 1 sheets of sheets\x01",
            "I wonder if it can dry out properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "After all I had to watch\x01",
            "Not at all …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B18")

    Jump("loc_1D4C")

    label("loc_1B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1B2B")
    Jump("loc_1D4C")

    label("loc_1B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B39")
    Jump("loc_1D4C")

    label("loc_1B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1B47")
    Jump("loc_1D4C")

    label("loc_1B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C14")

    ChrTalk(
        0xD,
        (
            "Shiron 's guy, what is it today\x01",
            "It seems the principal is getting angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Because I usually make mistakes,\x01",
            "Sometimes it gets angry properly\x01",
            "It's important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "… Well, look at the dawn\x01",
            "Will you go for eaves?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1C92")

    label("loc_1C14")


    ChrTalk(
        0xD,
        (
            "Shiron 's guy, what is it today\x01",
            "It seems the principal is getting angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, why do not you go for eclipsing later.\x01",
            "…… I am too sweet to keep up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C92")

    Jump("loc_1D4C")

    label("loc_1C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CA5")
    Jump("loc_1D4C")

    label("loc_1CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC0")
    Call(0, 8)
    Jump("loc_1D30")

    label("loc_1CC0")


    ChrTalk(
        0xD,
        (
            "Shira, Tama ~~~~\x01",
            "You say Matmo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… Even with a laser beam tomorrow\x01",
            "I wonder if it falls.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D30")

    Jump("loc_1D4C")

    label("loc_1D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1D43")
    Jump("loc_1D4C")

    label("loc_1D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D4C")

    label("loc_1D4C")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A65 end

    def Function_11_1D50(): pass

    label("Function_11_1D50")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3510, 8300, 11470, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x104, -1400, 7000, 11230, 270)
    SetChrPos(0x102, -1990, 7000, 12030, 225)
    SetChrPos(0x101, -2790, 7000, 12830, 225)
    SetChrPos(0x103, -3590, 7000, 13630, 180)
    SetChrPos(0x109, -2590, 7000, 14030, 180)
    SetChrPos(0x105, -3400, 7000, 14840, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#00000FShizuku-chan,\x01",
            "Were you in such a place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#12P#11205FAh … maybe,\x01",
            "Everyone in the support department?\x02\x03",
            "#11200FToday, for someone's visit\x01",
            "Did you come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10108FYes, Fran is here\x02\x03",
            "#10100FPolice officers and others\x01",
            "Iria was also watching him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11208FOh really……\x01",
            "Mr. Cecil to Mr. Fran\x01",
            "I heard it … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#12P#11203FAfter all, the incident of the street attack\x01",
            "It sounds quite severe.\x02\x03",
            "#11208FCecils and teachers, too,\x01",
            "She seems to be busy forever ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FAh……\x01",
            "It certainly was such a feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FBy the way, Shizuku - chan,\x01",
            "Mr. Arios\x01",
            "Recently, have you come to visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11208FNo, after the raid incident\x01",
            "Even never ….\x02\x03",
            "#11200FThere was contact,\x01",
            "After all it seems that he is busy with various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00200FIs that so……\x01",
            "It is lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11200FNo, I'm fine\x02\x03",
            "#11203FMany people were sacrificed,\x01",
            "Many injured people also came out ……\x02\x03",
            "Meanwhile, only me is amenable\x01",
            "I can not afford it.\x02\x03",
            "#11208F…… I also wanted to do something,\x01",
            "Mr. Fran and other patients\x01",
            "I am encouraging ….\x02\x03",
            "#11203F…… But just to the invisible me\x01",
            "I can do it only ….\x01",
            "That is, indeed, frustrating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00300FNo I think it would be great\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIn your opinion,\x01",
            "Courage to stand up against adversity\x01",
            "I think that they are giving it to everyone.\x02\x03",
            "#00004FWe all have to try our best\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10302FHehe, that's right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11200FEr …\x01",
            "I think that everyone is serious,\x01",
            "Please do your best.\x02\x03",
            "#11203FI'll do the same here\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x9, 0x10)
    OP_93(0x9, 0x5A, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x18E, 5)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -2790, 7000, 12830, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_1D50 end

    def Function_12_2430(): pass

    label("Function_12_2430")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch02500.itc", 0x1F)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1900, 7000, 14600, 180)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1300, 7000, 15610, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -3100, 7000, 14600, 180)
    OP_68(-3510, 8400, 11470, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16160, 0)
    SetChrPos(0x104, -2100, 7000, 16800, 180)
    SetChrPos(0x102, -1900, 7000, 17810, 180)
    SetChrPos(0x101, -2310, 7000, 18610, 180)
    SetChrPos(0x103, -1700, 7000, 19600, 180)
    SetChrPos(0x109, -1910, 7000, 20600, 180)
    SetChrPos(0x105, -2120, 7000, 21590, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    BeginChrThread(0x9, 3, 0, 13)
    BeginChrThread(0xE, 3, 0, 14)
    BeginChrThread(0xF, 3, 0, 15)
    BeginChrThread(0x104, 3, 0, 16)
    BeginChrThread(0x102, 3, 0, 17)
    BeginChrThread(0x101, 3, 0, 18)
    BeginChrThread(0x103, 3, 0, 19)
    BeginChrThread(0x109, 3, 0, 20)
    BeginChrThread(0x105, 3, 0, 21)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x9, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0xE,
        "#01400FShizuku, watch your step.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11202FYes, thank you father.\x02\x03",
            "#11204FHuhu, good wind ……\x01",
            "Besides, the light of the day is bright,\x01",
            "Warm and pleasant … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FWell, that was good.\x02\x03",
            "#00003F…… That reminds me a while ago,\x01",
            "In order to feel ambient light\x01",
            "I told you I was getting … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#12P#11200FEven though\x01",
            "I do not know much so much.\x02\x03",
            "#11203FMoya which is completely blank on every side\x01",
            "As it took,\x01",
            "I can feel the brightness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108Fso……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FEven though I can feel the light,\x01",
            "I guess the level is visible\x01",
            "There seems to be no such thing ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01403F…………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x9,
        (
            "#6P#11202F……Let me see.\x01",
            "Everyone, so dark\x01",
            "Please do not.\x02\x03",
            "#11209FAs for the result of this surgery\x01",
            "I am very pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10305FOh … Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11203F…… Certainly at first,\x01",
            "To be unable to recover\x01",
            "It also plunged.\x02\x03",
            "#11208FAlready, absolutely\x01",
            "I guess it will not get over ……\x01",
            "I was about to give up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208FMr. Shizuku ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11202FBut, if you think about it,\x01",
            "So far as \"treatment advanced\"\x01",
            "This is my first time.\x02\x03",
            "#11204FSo my eyes are slow,\x01",
            "Surely it will get better …\x01",
            "I was able to think so once again.\x02\x03",
            "#11200FDad who supports me,\x01",
            "Hospital people, and\x01",
            "Even for Ka'a-chan ……\x02\x03",
            "#11209FWithout giving up\x01",
            "I think that I will continue treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10102FShizuoka … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F… … You are strong, really.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#6P#11205FEr, um … … I'm sorry,\x01",
            "You look great like running rocks.\x02\x03",
            "#11203FTreatment expenses for even my father\x01",
            "Have them take out, always\x01",
            "Even though I bother you ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01403F…… If you say that you will not give up,\x01",
            "I will just support it as usual.\x02\x03",
            "#01402FWithout thinking about extra things,\x01",
            "You should concentrate on regaining the light.\x02\x03",
            "#01404FSaya would also like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11203FDad … That's right.\x02\x03",
            "#11202FBeing a goddess\x01",
            "Even for mother ……\x01",
            "I'll keep going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01004FKuku, Arios.\x01",
            "You are still your child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, indeed.\x01",
            "The place where the strong core is conspicuous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01404F……surely,\x01",
            "mother#4RSaya#I guess it looked like.\x02\x03",
            "#01400F── It is about time for me to go out.\x01",
            "Shizuku, I will return to the sickroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#11205FOh … yes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FLet's suppose it's time to go back then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's\x01",
            "I enjoyed a temporary conversation in the hospital room of Shizuku.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)
    NewScene("t1550", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2430 end

    def Function_13_2ED5(): pass

    label("Function_13_2ED5")


    def lambda_2EDA():
        OP_95(0xFE, -3590, 7000, 11230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EDA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_13_2ED5 end

    def Function_14_2EFB(): pass

    label("Function_14_2EFB")


    def lambda_2F00():
        OP_95(0xFE, -2590, 7000, 11020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F00)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_14_2EFB end

    def Function_15_2F21(): pass

    label("Function_15_2F21")


    def lambda_2F26():
        OP_95(0xFE, -1500, 7000, 10030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F26)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_2F21 end

    def Function_16_2F47(): pass

    label("Function_16_2F47")


    def lambda_2F4C():
        OP_95(0xFE, -1400, 7000, 11230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F4C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_16_2F47 end

    def Function_17_2F6D(): pass

    label("Function_17_2F6D")


    def lambda_2F72():
        OP_95(0xFE, -1990, 7000, 12030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F72)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_17_2F6D end

    def Function_18_2F93(): pass

    label("Function_18_2F93")


    def lambda_2F98():
        OP_95(0xFE, -2790, 7000, 12830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F98)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_18_2F93 end

    def Function_19_2FB9(): pass

    label("Function_19_2FB9")


    def lambda_2FBE():
        OP_95(0xFE, -3590, 7000, 13630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FBE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_2FB9 end

    def Function_20_2FDF(): pass

    label("Function_20_2FDF")


    def lambda_2FE4():
        OP_95(0xFE, -2590, 7000, 14030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FE4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_20_2FDF end

    def Function_21_3005(): pass

    label("Function_21_3005")


    def lambda_300A():
        OP_95(0xFE, -3400, 7000, 14840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_300A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_3005 end

    def Function_22_302B(): pass

    label("Function_22_302B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3139")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere are you going?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【4F Pharmacology · Neurology Laboratory】\x01",      # 0
            "【quit】\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30E4"),
        (1, "loc_312D"),
        (SWITCH_DEFAULT, "loc_3134"),
    )


    label("loc_30E4")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311F")
    SetScenarioFlags(0x22, 0)
    NewScene("t1650", 100, 0, 0)
    IdleLoop()
    Jump("loc_3128")

    label("loc_311F")

    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_3128")

    Jump("loc_3134")

    label("loc_312D")

    EventEnd(0x3)
    Jump("loc_3134")

    label("loc_3134")

    Jump("loc_318C")

    label("loc_3139")

    EventBegin(0x2)
    ClearMapFlags(0x20)

    ChrTalk(
        0x101,
        (
            "#00000FIs this the research building?\x01",
            "I do not have any particular business,\x01",
            "Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)

    label("loc_318C")

    Return()

    # Function_22_302B end

    def Function_23_318D(): pass

    label("Function_23_318D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14750, 9400, -3400, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15860, 0)
    SetChrPos(0x101, 18740, 7000, -3160, 270)
    SetChrPos(0x102, 18740, 7000, -3160, 270)
    SetChrPos(0x109, 18740, 7000, -3160, 270)
    SetChrPos(0x105, 18740, 7000, -3160, 270)
    SetChrPos(0x104, 18740, 7000, -3160, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(14750, 8000, -3400, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x5)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 25)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 28)
    WaitChrThread(0x105, 3)
    Sound(107, 0, 100, 0)
    OP_71(0x5, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x104,
        (
            "#00301F…… I knew something like that,\x01",
            "I feel like the mystery has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FSomething is tough …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FYes, since Professor Joachim passed away,\x01",
            "Too few clues … …\x02\x03",
            "#00103FAt least the analysis of the cult's database\x01",
            "If it advances it may be able to understand something, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10300FWell, that area\x01",
            "Is it a future task?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FOh … … even ours\x01",
            "Let's not forget and let's care.\x02\x03",
            "#00003FTentatively,\x01",
            "This request is now achieved.\x02\x03",
            "#00000FOn the way back to Cecil's older sister\x01",
            "You might as well leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FOh, that's right!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Request of a new professor】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x70, 0x1, 0x6)
    OP_29(0x70, 0x1, 0x7)
    OP_29(0x70, 0x4, 0x10)
    OP_29(0xA3, 0x1, 0x5)
    OP_66(0x0, 0x1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 15500, 7000, -3000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapObjFlags(0x5, 0x10)
    EventEnd(0x5)
    Return()

    # Function_23_318D end

    def Function_24_3600(): pass

    label("Function_24_3600")


    def lambda_3605():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3605)

    def lambda_3616():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3616)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 13000, 7000, -3000, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_24_3600 end

    def Function_25_364B(): pass

    label("Function_25_364B")


    def lambda_3650():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3650)

    def lambda_3661():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3661)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 14160, 7000, -2240, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_25_364B end

    def Function_26_3696(): pass

    label("Function_26_3696")


    def lambda_369B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_369B)

    def lambda_36AC():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_36AC)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 15890, 7000, -3980, 2000, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_26_3696 end

    def Function_27_36E1(): pass

    label("Function_27_36E1")


    def lambda_36E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_36E6)

    def lambda_36F7():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_36F7)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 14180, 7000, -4310, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_27_36E1 end

    def Function_28_372C(): pass

    label("Function_28_372C")


    def lambda_3731():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3731)

    def lambda_3742():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3742)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 15840, 7000, -2650, 2000, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_28_372C end

    def Function_29_3777(): pass

    label("Function_29_3777")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FOops, without going to the reception desk\x01",
            "I can not afford to enter the ward.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -16059, 6000, 19210, 270)
    EventEnd(0x4)
    Return()

    # Function_29_3777 end

    SaveToFile()

Try(main)
