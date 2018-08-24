from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Baggio",                 # 1
        "Shizuku",                # 2
        "Professor Seiland",      # 3
        "Janitor Dyson",          # 4
        "Nurse Xilun",            # 5
        "Nurse Meihua",           # 6
        "Arios",                  # 7
        "Sergei",                 # 8
        "St. Ursula Byroad",      # 9
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

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(712, 0)                                        # 0

    ScpFunction((
        "Function_0_2C8",          # 00, 0
        "Function_1_380",          # 01, 1
        "Function_2_512",          # 02, 2
        "Function_3_5DE",          # 03, 3
        "Function_4_6C2",          # 04, 4
        "Function_5_9CF",          # 05, 5
        "Function_6_E05",          # 06, 6
        "Function_7_1263",         # 07, 7
        "Function_8_192F",         # 08, 8
        "Function_9_1B1F",         # 09, 9
        "Function_10_1C4E",        # 0A, 10
        "Function_11_1FA8",        # 0B, 11
        "Function_12_26A2",        # 0C, 12
        "Function_13_31EA",        # 0D, 13
        "Function_14_3210",        # 0E, 14
        "Function_15_3236",        # 0F, 15
        "Function_16_325C",        # 10, 16
        "Function_17_3282",        # 11, 17
        "Function_18_32A8",        # 12, 18
        "Function_19_32CE",        # 13, 19
        "Function_20_32F4",        # 14, 20
        "Function_21_331A",        # 15, 21
        "Function_22_3340",        # 16, 22
        "Function_23_34D4",        # 17, 23
        "Function_24_3986",        # 18, 24
        "Function_25_39D1",        # 19, 25
        "Function_26_3A1C",        # 1A, 26
        "Function_27_3A67",        # 1B, 27
        "Function_28_3AB2",        # 1C, 28
        "Function_29_3AFD",        # 1D, 29
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FC")
    Call(0, 8)
    Jump("loc_6BE")

    label("loc_5FC")


    ChrTalk(
        0x8,
        (
            "A nurse might be nice. It's\x01",
            "not the case that there\x01",
            "aren't any male nurses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I had nothing to lose so I tried\x01",
            "asking sis for advice, but somehow I\x01",
            "feel that a path has opened for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE")

    TalkEnd(0xFE)
    Return()

    # Function_3_5DE end

    def Function_4_6C2(): pass

    label("Function_4_6C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D7")
    Call(0, 11)
    Jump("loc_9CB")

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_960")
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11200FBy the way, everyone.\x02\x03",
            "KeA came to the hospital\x01",
            "three days ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYeah... Now that you\x01",
            "mention it, she did come\x01",
            "to visit you.\x02\x03",
            "#00000FUmm, did something\x01",
            "happen with KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11208FWell... I felt like she\x01",
            "was a little strange\x01",
            "somehow.\x02\x03",
            "#11203FLike she was brooding\x01",
            "over something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FKeA was...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FShe didn't act that way\x01",
            "in front of us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F...Maybe KeA is uneasy\x01",
            "about the situation in\x01",
            "Crossbell too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FRight... Maybe she was\x01",
            "hiding her feelings so\x01",
            "as not to worry us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FWell anyway, I think\x01",
            "it's best if we keep\x01",
            "this in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 6)
    Jump("loc_9CB")

    label("loc_960")


    ChrTalk(
        0x9,
        (
            "#11200FI think things are hard\x01",
            "for you too, but please,\x01",
            "do your best.\x02\x03",
            "I'll cheer you on from\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CB")

    TalkEnd(0xFE)
    Return()

    # Function_4_6C2 end

    def Function_5_9CF(): pass

    label("Function_5_9CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9E0")
    Jump("loc_E01")

    label("loc_9E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B37")

    ChrTalk(
        0xA,
        (
            "The physicians and interns\x01",
            "are all dealing with the\x01",
            "types of medicines we lack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It probably won't be perfect,\x01",
            "but doing one's very best at all\x01",
            "times is the duty of a doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On my pride and dignity as a pharmacology\x01",
            "and neurology professor, I swear upon the\x01",
            "Goddess that I'll do something about them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_C10")

    label("loc_B37")


    ChrTalk(
        0xA,
        (
            "The physicians and interns\x01",
            "are all dealing with the\x01",
            "types of medicines we lack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On my pride and dignity as a pharmacology\x01",
            "and neurology professor, I swear upon the\x01",
            "Goddess that I'll do something about them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C10")

    Jump("loc_E01")

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_C23")
    Jump("loc_E01")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C31")
    Jump("loc_E01")

    label("loc_C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3D")

    ChrTalk(
        0xA,
        (
            "Shizuku... The possibility\x01",
            "she can recover her\x01",
            "eyesight is low as can be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...However, as long as the\x01",
            "patient doesn't give up, I\x01",
            "won't give up either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In the name of Seiland...\x01",
            "One day, I swear I'll cure\x01",
            "her with my own hands.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E01")

    label("loc_D3D")


    ChrTalk(
        0xA,
        (
            "If Shizuku's eyesight recovery surgery\x01",
            "succeeds, it'll become hope for other\x01",
            "patients with the same handicap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In the name of Seiland...\x01",
            "One day, I swear I'll cure\x01",
            "her with my own hands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E01")

    TalkEnd(0xFE)
    Return()

    # Function_5_9CF end

    def Function_6_E05(): pass

    label("Function_6_E05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E8D")

    ChrTalk(
        0xB,
        (
            "That huge tree is\x01",
            "amazing... You can even\x01",
            "see it from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...I wonder what's going\x01",
            "to happen to Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_E9B")
    Jump("loc_125F")

    label("loc_E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_10A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE2")

    ChrTalk(
        0xB,
        (
            "In lectures at the research lab\x01",
            "these days, it seems that they\x01",
            "almost can't do experiments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's the effect of collecting samples\x01",
            "on the highways and not being able to\x01",
            "stock up from Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At this rate, it seems that the\x01",
            "interns' study environment will\x01",
            "end up gradually worsening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_10A4")

    label("loc_FE2")


    ChrTalk(
        0xB,
        (
            "In lectures at the research lab\x01",
            "these days, it seems that they\x01",
            "almost can't do experiments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At this rate, it seems that the\x01",
            "interns' study environment will\x01",
            "end up gradually worsening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A4")

    Jump("loc_125F")

    label("loc_10A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_10B7")
    Jump("loc_125F")

    label("loc_10B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_125F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C3")

    ChrTalk(
        0xB,
        (
            "When I work around here,\x01",
            "I pick up gossip from the\x01",
            "interns on lunch break...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Lately there's been a\x01",
            "lot of gossip regarding\x01",
            "Professor Seiland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have nothing to do with\x01",
            "her, but... I actually wonder\x01",
            "what kind of person she is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_125F")

    label("loc_11C3")


    ChrTalk(
        0xB,
        (
            "Recently, Professor\x01",
            "Seiland is a hot topic\x01",
            "among the interns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I have nothing to do with\x01",
            "her, but... I actually wonder\x01",
            "what kind of person she is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125F")

    TalkEnd(0xFE)
    Return()

    # Function_6_E05 end

    def Function_7_1263(): pass

    label("Function_7_1263")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1274")
    Jump("loc_192B")

    label("loc_1274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1282")
    Jump("loc_192B")

    label("loc_1282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_12C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D")
    Call(0, 9)
    Jump("loc_12C4")

    label("loc_129D")


    ChrTalk(
        0xC,
        (
            "Ehehe, Meihua is really\x01",
            "reliable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C4")

    Jump("loc_192B")

    label("loc_12C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_14DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1420")

    ChrTalk(
        0xC,
        (
            "Today's sheet drying method is the\x01",
            "special "pile-dryer" technique I\x01",
            "came up with yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Goodness, by pile-drying\x01",
            "two sheets, the number\x01",
            "you can dry doubles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "With this, I can perfectly\x01",
            "cover today's share for Meihua,\x01",
            "who has the day off, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...O-Oh, but... What if\x01",
            "they don't dry at\x01",
            "all...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_14DA")

    label("loc_1420")


    ChrTalk(
        0xC,
        (
            "Ooh, I discovered that the\x01",
            ""pile-drying" special technique\x01",
            "doesn't dry the sheets at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Since Meihua has the day off,\x01",
            "I was thinking of working\x01",
            "hard enough for two, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DA")

    Jump("loc_192B")

    label("loc_14DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_14ED")
    Jump("loc_192B")

    label("loc_14ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14FB")
    Jump("loc_192B")

    label("loc_14FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1509")
    Jump("loc_192B")

    label("loc_1509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162D")

    ChrTalk(
        0xC,
        (
            "The other day, when Mihail was\x01",
            "discharged, I gave my handkerchief\x01",
            "to Meihua who was crying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, she suddenly stopped\x01",
            "crying for some reason and\x01",
            "staaared at me with her eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm? What was that for?\x01",
            "And she didn't even give\x01",
            "the handkerchief back...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_16DC")

    label("loc_162D")


    ChrTalk(
        0xC,
        (
            "I wonder what Meihua did\x01",
            "with my handkerchief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I found it in the dorm room before. I\x01",
            "liked it because it was pleasant to the\x01",
            "touch and had a nice design, and yet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DC")

    Jump("loc_192B")

    label("loc_16E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FC")
    Call(0, 8)
    Jump("loc_17CE")

    label("loc_16FC")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        (
            "Ah, I see! Why don't you\x01",
            "try on a nurse's\x01",
            "uniform?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "Come on Meihua, take\x01",
            "that off and lend them\x01",
            "to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I-I won't!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(H-Hmm, she's the same\x01",
            "as always...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)

    label("loc_17CE")

    Jump("loc_192B")

    label("loc_17D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A9")

    ChrTalk(
        0xC,
        (
            "Haha, what nice weather\x01",
            "today. The laundry will\x01",
            "dry nicely♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...*sigh*, this warm\x01",
            "weather... makes me\x01",
            "sleepy for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Maybe I'll get a sheet\x01",
            "and sleep in it again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_191D")

    label("loc_18A9")


    ChrTalk(
        0xC,
        (
            "Basking in the sun here\x01",
            "is pleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I get the feeling Meihua\x01",
            "won't be coming today...\x01",
            "Yeah, I'll sleep☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191D")

    Jump("loc_192B")

    label("loc_1922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_192B")

    label("loc_192B")

    TalkEnd(0xFE)
    Return()

    # Function_7_1263 end

    def Function_8_192F(): pass

    label("Function_8_192F")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "I failed the intern entrance\x01",
            "exam... I'm feeling more and\x01",
            "more ashamed at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Say, Xilun. What should\x01",
            "I do from now on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "(Baggio... To be asking\x01",
            "Xilun for advice, he must\x01",
            "really be at wits end.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm, let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, why don't you try\x01",
            "becoming a nurse like\x01",
            "me, your sister?\x02",
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
            "I-Isn't that a proper\x01",
            "opinion coming from you,\x01",
            "Xilun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see, a male nurse... I\x01",
            "didn't think of that!\x02",
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

    # Function_8_192F end

    def Function_9_1B1F(): pass

    label("Function_9_1B1F")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "Xilun, you... If you pile\x01",
            "the sheets on top of each\x01",
            "other, they won't dry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Honestly, how many years\x01",
            "have you been doing\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Umm, we've been together\x01",
            "one, two...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Enough, you don't have\x01",
            "to honestly reply to\x01",
            "pointless things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Here, dry these again!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_1B1F end

    def Function_10_1C4E(): pass

    label("Function_10_1C4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C5F")
    Jump("loc_1FA4")

    label("loc_1C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1C6D")
    Jump("loc_1FA4")

    label("loc_1C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C88")
    Call(0, 9)
    Jump("loc_1D1B")

    label("loc_1C88")


    ChrTalk(
        0xD,
        (
            "Honestly, that Xilun...\x01",
            "Can't she even properly\x01",
            "dry the sheets by herself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Really, if I don't watch\x01",
            "her she doesn't do\x01",
            "anything right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1B")

    Jump("loc_1FA4")

    label("loc_1D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1D2E")
    Jump("loc_1FA4")

    label("loc_1D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D3C")
    Jump("loc_1FA4")

    label("loc_1D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1D4A")
    Jump("loc_1FA4")

    label("loc_1D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1EDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E52")

    ChrTalk(
        0xD,
        (
            "That Xilun, it seems\x01",
            "that she was scolded by\x01",
            "the head nurse today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "She usually makes tons of mistakes,\x01",
            "so it's important for her to be\x01",
            "scolded every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Well, I'll go stick\x01",
            "up for her at the\x01",
            "appropriate time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1ED8")

    label("loc_1E52")


    ChrTalk(
        0xD,
        (
            "That Xilun, it seems\x01",
            "that she was scolded by\x01",
            "the head nurse today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, I'll go stick up\x01",
            "for her later. ...I'm\x01",
            "quite soft.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED8")

    Jump("loc_1FA4")

    label("loc_1EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EEB")
    Jump("loc_1FA4")

    label("loc_1EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F06")
    Call(0, 8)
    Jump("loc_1F88")

    label("loc_1F06")


    ChrTalk(
        0xD,
        (
            "Xilun... She says\x01",
            "something proper once in\x01",
            "a loooooong while, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...I think it's going to\x01",
            "snow or something\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F88")

    Jump("loc_1FA4")

    label("loc_1F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F9B")
    Jump("loc_1FA4")

    label("loc_1F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FA4")

    label("loc_1FA4")

    TalkEnd(0xFE)
    Return()

    # Function_10_1C4E end

    def Function_11_1FA8(): pass

    label("Function_11_1FA8")

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
            "#5P#00000FShizuku, so this is\x01",
            "where you were.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#12P#11205FAh... Could you be the\x01",
            "Support Section?\x02\x03",
            "#11200FDid you come to visit\x01",
            "someone today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10108FYes, Fran is\x01",
            "hospitalized here.\x02\x03",
            "#10100FThen we visited the\x01",
            "police inspector and\x01",
            "Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11208FI see... I heard about\x01",
            "Fran from Cecil and...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#12P#11203FAs I suspected, the attack\x01",
            "on the city seems to have\x01",
            "been quite heavy...\x02\x03",
            "#11208FIt seems that Cecil and the\x01",
            "other nurses and doctors\x01",
            "have been so busy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah... It does seem\x01",
            "that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FBy the way, Shizuku.\x01",
            "Have you seen your dad\x01",
            "recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11208FNo, I haven't even seen\x01",
            "him once since the\x01",
            "attack...\x02\x03",
            "#11200FHe called, but he seems\x01",
            "rather busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00200FI see... You must be\x01",
            "lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11200F...No, I'm fine.\x02\x03",
            "#11203FA lot of people were\x01",
            "sacrificed, and there are a\x01",
            "lot of injured too...\x02\x03",
            "Among them, I can't be the\x01",
            "only one who gets all their\x01",
            "attention.\x02\x03",
            "#11208F...I want to do something too,\x01",
            "like encouraging Fran and the\x01",
            "other patients, but...\x02\x03",
            "#11203F...It's just that this is all\x01",
            "I, who can't see, can do...\x01",
            "That's really frustrating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00300F...No, I think that's\x01",
            "more than enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI think that you, in your condition,\x01",
            "are giving courage to everyone to\x01",
            "fight in the face of adversity.\x02\x03",
            "#00004F...We have to do our best too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10302FHehe... Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11200FUmm... I think things are\x01",
            "hard for you too, but\x01",
            "please, do your best.\x02\x03",
            "#11203FI'll cheer you on from\x01",
            "here...\x02",
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

    # Function_11_1FA8 end

    def Function_12_26A2(): pass

    label("Function_12_26A2")

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
        (
            "#01400FWatch your step,\x01",
            "Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11202FYes, thank you father.\x02\x03",
            "#11204FHaha, what a nice breeze...\x01",
            "And the sunlight is bright,\x01",
            "warm and pleasant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, that's great.\x02\x03",
            "#00003F...By the way, Arios said\x01",
            "you became able to perceive\x01",
            "the light around you...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#12P#11200FYes, although I don't see it\x01",
            "in a very detailed way.\x02\x03",
            "#11203FIt's like there's a pure\x01",
            "white haze all around me and\x01",
            "I can feel the brightness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FAlthough you feel the light,\x01",
            "it seems it's not to a\x01",
            "degree that you can see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#01403F............\x02",
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
            "#6P#11202F...U-Umm, everyone?\x01",
            "Please don't feel so\x01",
            "depressed.\x02\x03",
            "#11209FI'm very pleased with\x01",
            "the results of this\x01",
            "surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10305FHuh... Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11203F...It's true that I felt\x01",
            "down at first since it\x01",
            "wasn't a full recovery.\x02\x03",
            "#11208FI thought I'll never be\x01",
            "able to recover... I\x01",
            "almost gave up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208FShizuku...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11202FBut thinking about it, this is the\x01",
            "first time time my "treatment has\x01",
            "progressed" this much.\x02\x03",
            "#11204FThat's why my eyes, though slowly,\x01",
            "will surely get better... I became\x01",
            "able to believe that again.\x02\x03",
            "#11200FFor father who supports me and\x01",
            "everyone in the hospital and KeA\x01",
            "too, I won't...\x02\x03",
            "#11209FI'll never give up and am thinking\x01",
            "of continuing the treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10102FShizuku...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F...You sure are strong.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#6P#11205FU-Umm... I'm sorry, that\x01",
            "must have sounded\x01",
            "conceited.\x02\x03",
            "#11203FI'm always causing\x01",
            "trouble for father who\x01",
            "pays my doctors' bills...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01403F...If you say you won't give\x01",
            "up, then I'll support you as\x01",
            "I have until now.\x02\x03",
            "#01402FDon't think about unnecessary\x01",
            "things and focus on getting\x01",
            "your eyesight back.\x02\x03",
            "#01404FI'm sure that's what Saya\x01",
            "would have wanted, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#11203FFather... You're right.\x02\x03",
            "#11202FFor mother who is with the\x01",
            "Goddess as well... I'll keep\x01",
            "doing my best from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01004FHehe, how 'bout that,\x01",
            "Arios? She's your kid\x01",
            "after all, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, true. The strength\x01",
            "of her heart's the same\x01",
            "as yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#01404F...I'm sure she got that\x01",
            "from her mother.\x02\x03",
            "#01400F─Shizuku, it's about time\x01",
            "your outing was over. We're\x01",
            "going back to your room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#11205FAh... Yes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThen, let's head back.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the\x01",
            "others enjoyed chatting for a\x01",
            "short while in Shizuku's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)
    NewScene("t1550", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_26A2 end

    def Function_13_31EA(): pass

    label("Function_13_31EA")


    def lambda_31EF():
        OP_95(0xFE, -3590, 7000, 11230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31EF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_13_31EA end

    def Function_14_3210(): pass

    label("Function_14_3210")


    def lambda_3215():
        OP_95(0xFE, -2590, 7000, 11020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3215)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_14_3210 end

    def Function_15_3236(): pass

    label("Function_15_3236")


    def lambda_323B():
        OP_95(0xFE, -1500, 7000, 10030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_323B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_3236 end

    def Function_16_325C(): pass

    label("Function_16_325C")


    def lambda_3261():
        OP_95(0xFE, -1400, 7000, 11230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3261)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_16_325C end

    def Function_17_3282(): pass

    label("Function_17_3282")


    def lambda_3287():
        OP_95(0xFE, -1990, 7000, 12030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3287)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_17_3282 end

    def Function_18_32A8(): pass

    label("Function_18_32A8")


    def lambda_32AD():
        OP_95(0xFE, -2790, 7000, 12830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32AD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_18_32A8 end

    def Function_19_32CE(): pass

    label("Function_19_32CE")


    def lambda_32D3():
        OP_95(0xFE, -3590, 7000, 13630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32D3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_32CE end

    def Function_20_32F4(): pass

    label("Function_20_32F4")


    def lambda_32F9():
        OP_95(0xFE, -2590, 7000, 14030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32F9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_20_32F4 end

    def Function_21_331A(): pass

    label("Function_21_331A")


    def lambda_331F():
        OP_95(0xFE, -3400, 7000, 14840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_331F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_331A end

    def Function_22_3340(): pass

    label("Function_22_3340")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3452")
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
            "#1KWhere to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[4F - Pharmacology/Neurology Research Lab]\x01",      # 0
            "[Cancel]\x01",                                        # 1
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
        (0, "loc_33FD"),
        (1, "loc_3446"),
        (SWITCH_DEFAULT, "loc_344D"),
    )


    label("loc_33FD")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3438")
    SetScenarioFlags(0x22, 0)
    NewScene("t1650", 100, 0, 0)
    IdleLoop()
    Jump("loc_3441")

    label("loc_3438")

    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_3441")

    Jump("loc_344D")

    label("loc_3446")

    EventEnd(0x3)
    Jump("loc_344D")

    label("loc_344D")

    Jump("loc_34D3")

    label("loc_3452")

    EventBegin(0x2)
    ClearMapFlags(0x20)

    ChrTalk(
        0x101,
        (
            "#00000FThe research laboratory is this way,\x01",
            "huh? We don't have any particular\x01",
            "business there, so let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)

    label("loc_34D3")

    Return()

    # Function_22_3340 end

    def Function_23_34D4(): pass

    label("Function_23_34D4")

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
            "#00301F...We learned various things, but I\x01",
            "feel like the number of things we\x01",
            "don't know has somehow also increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FIt's really\x01",
            "irritating...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FYes, now that Dr. Joachim has\x01",
            "passed away, we don't have many\x01",
            "clues left...\x02\x03",
            "#00103FWe might learn something\x01",
            "depending on the progress of the\x01",
            "Cult database analysis, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10300FWell, I guess that's a\x01",
            "future issue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FYeah... Let's not forget\x01",
            "about it.\x02\x03",
            "#00003F...At any rate, this\x01",
            "request is now\x01",
            "completed.\x02\x03",
            "#00000FMaybe we should see\x01",
            "Cecil on our way out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FYeah, let's do it!\x02",
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
            "Quest [New Professor's\x01",
            "Request]\x07\x00",
            " completed!\x02",
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

    # Function_23_34D4 end

    def Function_24_3986(): pass

    label("Function_24_3986")


    def lambda_398B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_398B)

    def lambda_399C():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_399C)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 13000, 7000, -3000, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_24_3986 end

    def Function_25_39D1(): pass

    label("Function_25_39D1")


    def lambda_39D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_39D6)

    def lambda_39E7():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39E7)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 14160, 7000, -2240, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_25_39D1 end

    def Function_26_3A1C(): pass

    label("Function_26_3A1C")


    def lambda_3A21():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A21)

    def lambda_3A32():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A32)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 15890, 7000, -3980, 2000, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_26_3A1C end

    def Function_27_3A67(): pass

    label("Function_27_3A67")


    def lambda_3A6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A6C)

    def lambda_3A7D():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3A7D)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 14180, 7000, -4310, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_27_3A67 end

    def Function_28_3AB2(): pass

    label("Function_28_3AB2")


    def lambda_3AB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3AB7)

    def lambda_3AC8():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3AC8)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 15840, 7000, -2650, 2000, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_28_3AB2 end

    def Function_29_3AFD(): pass

    label("Function_29_3AFD")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FOops, we can't enter the\x01",
            "hospital ward without going\x01",
            "to the reception desk.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -16059, 6000, 19210, 270)
    EventEnd(0x4)
    Return()

    # Function_29_3AFD end

    SaveToFile()

Try(main)
