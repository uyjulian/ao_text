from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0100_1.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 7, 0, 8],
    )

    BuildStringList((
        "c0100_1",                # 0
    ))

    ChipFrameInfo(256, 0)                                        # 0

    ScpFunction((
        "Function_0_100",          # 00, 0
        "Function_1_1005",         # 01, 1
        "Function_2_2575",         # 02, 2
        "Function_3_3514",         # 03, 3
        "Function_4_3C34",         # 04, 4
        "Function_5_48BA",         # 05, 5
        "Function_6_4ACB",         # 06, 6
        "Function_7_4DC6",         # 07, 7
        "Function_8_55D2",         # 08, 8
        "Function_9_56F9",         # 09, 9
        "Function_10_5FA0",        # 0A, 10
        "Function_11_6B70",        # 0B, 11
        "Function_12_6E49",        # 0C, 12
        "Function_13_7D6D",        # 0D, 13
        "Function_14_7ED7",        # 0E, 14
        "Function_15_804B",        # 0F, 15
        "Function_16_81C9",        # 10, 16
        "Function_17_8276",        # 11, 17
        "Function_18_82EA",        # 12, 18
        "Function_19_8368",        # 13, 19
        "Function_20_8497",        # 14, 20
        "Function_21_9D6B",        # 15, 21
        "Function_22_A379",        # 16, 22
        "Function_23_A53A",        # 17, 23
        "Function_24_AAB4",        # 18, 24
        "Function_25_AC80",        # 19, 25
        "Function_26_B1F5",        # 1A, 26
    ))


    def Function_0_100(): pass

    label("Function_0_100")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C0")

    ChrTalk(
        0xFE,
        (
            "And just when I thought it was\x01",
            "safe to come out... What the heck\x01",
            "is that tree floating in the air?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It won't fall somewhere,\x01",
            "will it? ...This anxiety\x01",
            "will never end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_1C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1CE")
    Jump("loc_1001")

    label("loc_1CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_402")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_321")

    ChrTalk(
        0xFE,
        (
            "He said accidents that have occurred in\x01",
            "the past are the result of a "secret\x01",
            "feud" between the major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Does he mean they're the result\x01",
            "of those countries' spies\x01",
            "fighting against each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I honestly didn't think too\x01",
            "deeply about it, but if it's really\x01",
            "true, then that's unforgivable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3FD")

    label("loc_321")


    ChrTalk(
        0xFE,
        (
            "He said accidents that have occurred in\x01",
            "the past are the result of a "secret\x01",
            "feud" between the major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I honestly didn't think too\x01",
            "deeply about it, but if it's really\x01",
            "true, then that's unforgivable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD")

    Jump("loc_1001")

    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_57E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E0")

    ChrTalk(
        0xFE,
        (
            "Rumor has it that the\x01",
            "Imperial government hired\x01",
            "that armed group...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In that sense, we don't\x01",
            "know where they'll\x01",
            "strike next, do we.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get terribly anxious\x01",
            "just thinking about\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_579")

    label("loc_4E0")


    ChrTalk(
        0xFE,
        (
            "Rumor has it that the\x01",
            "Imperial government hired\x01",
            "that armed group...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I think they could\x01",
            "come to attack us again,\x01",
            "I get terribly anxious...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_579")

    Jump("loc_1001")

    label("loc_57E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_61E")

    ChrTalk(
        0xFE,
        (
            "I'm sure the people of\x01",
            "Mainz are having a hard\x01",
            "time right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Armed people suddenly\x01",
            "marching in... I get scared\x01",
            "just imagining it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_696")

    ChrTalk(
        0xFE,
        (
            "Today mama asked me to\x01",
            "do an errand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...She said to go buy\x01",
            "buckets because the roof\x01",
            "is leaking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6FB")

    ChrTalk(
        0xFE,
        (
            "So many ambulances were\x01",
            "mobilized... It seems a rather\x01",
            "serious accident occurred.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_6FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_77F")

    ChrTalk(
        0xFE,
        (
            "...Do I really want to\x01",
            "live alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really want to do it,\x01",
            "but I feel living alone\x01",
            "would be quite lonely...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_92D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D6")

    ChrTalk(
        0xFE,
        (
            "Side job, side job... If I want\x01",
            "to be somewhere safe, maybe\x01",
            "being a waitress would do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, if I want to earn a\x01",
            "lot, there's also the option\x01",
            "of being a hostess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No no no, dear me,\x01",
            "what on earth am I\x01",
            "thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how good the pay,\x01",
            "being a drinking partner\x01",
            "for old men is a big no.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_928")

    label("loc_8D6")


    ChrTalk(
        0xFE,
        (
            "If I want to live alone, I\x01",
            "have to work... What kind\x01",
            "of job am I suited for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_928")

    Jump("loc_1001")

    label("loc_92D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA8")

    ChrTalk(
        0xFE,
        (
            "For living alone, I personally\x01",
            "think the West Street area is\x01",
            "the best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But thinking realistically about\x01",
            "rent and stuff, I settled on the\x01",
            "East Street area in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Downtown would be even\x01",
            "better, but I'm worried about\x01",
            "public safety most of all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wait, if I want to be\x01",
            "independent, I have to first\x01",
            "find a job. ...*sigh*.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B42")

    label("loc_AA8")


    ChrTalk(
        0xFE,
        (
            "For living alone, I personally\x01",
            "think the West Street area is\x01",
            "the best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wait, if I want to be\x01",
            "independent, I have to\x01",
            "first find a job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B42")

    Jump("loc_1001")

    label("loc_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_BA1")

    ChrTalk(
        0xFE,
        (
            "My, it's already this\x01",
            "late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to hurry home and\x01",
            "help my mom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C6D")

    ChrTalk(
        0xFE,
        (
            "I watched the heads of state\x01",
            "arrive in Crossbell and it\x01",
            "was over in a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were all riding in cars and it\x01",
            "wasn't really clear, but... I got\x01",
            "the feeling they were all VIPs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D36")

    ChrTalk(
        0xFE,
        (
            "Because the trade\x01",
            "conference starts tomorrow,\x01",
            "security is rather tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Earlier, I was stopped by a\x01",
            "patrol officer and got the first\x01",
            "police questioning of my life.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DBA")

    label("loc_D36")


    ChrTalk(
        0xFE,
        (
            "It was my first police\x01",
            "questioning, but I guess\x01",
            "it was rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who would want to be\x01",
            "called "maid" out\x01",
            "loud... How shameful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBA")

    Jump("loc_1001")

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_E4A")

    ChrTalk(
        0xFE,
        (
            "I hate staying put at\x01",
            "home just because it\x01",
            "rains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I just grab my\x01",
            "favorite umbrella, it's\x01",
            "time for a walk, see♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED9")

    ChrTalk(
        0xFE,
        (
            "So many patrol cars\x01",
            "appeared and I was\x01",
            "shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I guess they\x01",
            "were cool, being police\x01",
            "and all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA3")

    ChrTalk(
        0xFE,
        (
            "Honestly, that papa of\x01",
            "mine! Why does he loiter\x01",
            "around naked at home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lack of concern towards\x01",
            "a girl my age... That\x01",
            "ought to be a crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I want to live\x01",
            "alooone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1001")

    label("loc_FA3")


    ChrTalk(
        0xFE,
        (
            "*sigh*, I want to live\x01",
            "alooone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I wonder if there's\x01",
            "a nice property\x01",
            "somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1001")

    TalkEnd(0xFE)
    Return()

    # Function_0_100 end

    def Function_1_1005(): pass

    label("Function_1_1005")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1136")

    ChrTalk(
        0xFE,
        (
            "I don't know the details,\x01",
            "but it seems we've lost\x01",
            "those Aion weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Setting aside how he did it... I'm\x01",
            "positive President Dieter prepared\x01",
            "them to protect Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although he brought great chaos\x01",
            "on all of us as a result of his\x01",
            "actions, I do not blame him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11FE")

    label("loc_1136")


    ChrTalk(
        0xFE,
        (
            "Setting aside how he did it... I'm\x01",
            "positive President Dieter prepared\x01",
            "them to protect Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although he brought great chaos\x01",
            "on all of us as a result of his\x01",
            "actions, I do not blame him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FE")

    Jump("loc_2571")

    label("loc_1203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1211")
    Jump("loc_2571")

    label("loc_1211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_13A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1305")

    ChrTalk(
        0xFE,
        (
            "Hmm... Declaration of an\x01",
            "asset freeze, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I never thought Mayor\x01",
            "Dieter would've resorted to\x01",
            "such a drastic measure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, like he says, we\x01",
            "may not have another chance\x01",
            "to stand up aside from now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_139F")

    label("loc_1305")


    ChrTalk(
        0xFE,
        (
            "I never thought Mayor\x01",
            "Dieter would've resorted to\x01",
            "such a drastic measure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, we may not have\x01",
            "another chance to stand\x01",
            "up aside from now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_139F")

    Jump("loc_2571")

    label("loc_13A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1576")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CE")

    ChrTalk(
        0xFE,
        (
            "The attack the other\x01",
            "day... It's certainly\x01",
            "the Empire's doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately they have pretended to be\x01",
            "amicable, but in truth, they'll do\x01",
            "anything to achieve their goals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They employed foul play and plan\x01",
            "to invade if chances permit...\x01",
            "That's what Erebonia is!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1571")

    label("loc_14CE")


    ChrTalk(
        0xFE,
        (
            "The attack the other\x01",
            "day... It's certainly\x01",
            "the Empire's doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They employed foul play and plan\x01",
            "to invade if chances permit...\x01",
            "That's what Erebonia is!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1571")

    Jump("loc_2571")

    label("loc_1576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1627")

    ChrTalk(
        0xFE,
        (
            "The Empire could be\x01",
            "behind this incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hmm. In that case, we probably won't\x01",
            "be able to protect Crossbell just by\x01",
            "obeying like we have until now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2571")

    label("loc_1627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1635")
    Jump("loc_2571")

    label("loc_1635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1726")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D9")

    ChrTalk(
        0xFE,
        (
            "It appears that some\x01",
            "kind of incident\x01",
            "happened to the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Absit omen... O Aidios,\x01",
            "Goddess of the Sky,\x01",
            "please protect us all!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1721")

    label("loc_16D9")


    ChrTalk(
        0xFE,
        (
            "Absit omen... O Aidios,\x01",
            "Goddess of the Sky,\x01",
            "please protect us all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1721")

    Jump("loc_2571")

    label("loc_1726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_188E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1814")

    ChrTalk(
        0xFE,
        (
            "I can't say it across the\x01",
            "board, but it seems many young\x01",
            "people approve of independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A generation that knows no strife,\x01",
            "huh... I'm worried that they may not\x01",
            "understand the seriousness of all this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1889")

    label("loc_1814")


    ChrTalk(
        0xFE,
        (
            "A generation that knows no strife,\x01",
            "huh... I'm worried that they may not\x01",
            "understand the seriousness of all this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1889")

    Jump("loc_2571")

    label("loc_188E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_19C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196E")

    ChrTalk(
        0xFE,
        (
            "Hmm. Honestly, I'd never\x01",
            "thought I'd hear the word\x01",
            ""independence" at my age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Independence, independence, huh... It's\x01",
            "like a dream come true, but I don't\x01",
            "think it'll go well in the end...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19BC")

    label("loc_196E")


    ChrTalk(
        0xFE,
        (
            "Independence, independence,\x01",
            "huh... Could it really be a\x01",
            "dream come true?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BC")

    Jump("loc_2571")

    label("loc_19C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1C37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B70")

    ChrTalk(
        0xFE,
        (
            "We can't attend the trade\x01",
            "conference, and it won't be\x01",
            "relayed via orbal communications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, the only way we\x01",
            "have to hear its result is through\x01",
            "the city's PR and the press.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Needless to say, from\x01",
            "the very popular\x01",
            "Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their articles have\x01",
            "credibility, balance and\x01",
            "speed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Take your pick. There isn't\x01",
            "a news outlet that can match\x01",
            "them in any of those areas.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C32")

    label("loc_1B70")


    ChrTalk(
        0xFE,
        (
            "We can't attend the trade\x01",
            "conference, and it won't be\x01",
            "relayed via orbal communications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, the only way we\x01",
            "have to hear its result is through\x01",
            "the city's PR and the press.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C32")

    Jump("loc_2571")

    label("loc_1C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D25")

    ChrTalk(
        0xFE,
        (
            "Oh, wouldn't you know it.\x01",
            "It's grown completely\x01",
            "dark, hasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho. Could I have been\x01",
            "too absorbed by the trade\x01",
            "conference's atmosphere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must hurry home so as\x01",
            "not to make my old woman\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DA8")

    label("loc_1D25")


    ChrTalk(
        0xFE,
        (
            "Oh, wouldn't you know it.\x01",
            "It's grown completely\x01",
            "dark, hasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must hurry home so as\x01",
            "not to make my old woman\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA8")

    Jump("loc_2571")

    label("loc_1DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E5F")

    ChrTalk(
        0xFE,
        (
            "Some time ago, a young\x01",
            "woman with an eastern air\x01",
            "entered that restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She was a beautiful\x01",
            "young woman with an\x01",
            "intellectual's face.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2110")

    label("loc_1E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2051")

    ChrTalk(
        0xFE,
        (
            "Hmm, so the new City\x01",
            "Hall was finally\x01",
            "revealed, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Five years have passed since its construction\x01",
            "was announced. According to rumor, it would be\x01",
            "at least another year until completion, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just after Mayor Crois was\x01",
            "elected, he decided to\x01",
            "invest IBC capital in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, construction proceeded quickly\x01",
            "without being influenced by stupid rights battles,\x01",
            "and it was finally completed the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho, Mayor Crois really\x01",
            "did us a favor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2110")

    label("loc_2051")


    ChrTalk(
        0xFE,
        (
            "Five years have passed since its construction\x01",
            "was announced. According to rumor, it would be\x01",
            "at least another year until completion, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho, Mayor Crois really\x01",
            "did us a favor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2110")

    Jump("loc_2571")

    label("loc_2115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2288")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FA")

    ChrTalk(
        0xFE,
        (
            "Hmm, the trade conference\x01",
            "finally starts tomorrow,\x01",
            "does it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor Crois, who proposed\x01",
            "it, is both mayor and\x01",
            "president of that IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He'll need to display\x01",
            "his leadership at the\x01",
            "conference.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2283")

    label("loc_21FA")


    ChrTalk(
        0xFE,
        (
            "Hmm, the trade conference\x01",
            "finally starts tomorrow,\x01",
            "does it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor Crois will need to\x01",
            "display his leadership\x01",
            "at the conference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2283")

    Jump("loc_2571")

    label("loc_2288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2296")
    Jump("loc_2571")

    label("loc_2296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2571")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2321")

    ChrTalk(
        0xFE,
        (
            "Even from here I could\x01",
            "see that dramatic arrest\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The police are doing\x01",
            "their best too, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2571")

    label("loc_2321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249B")

    ChrTalk(
        0xFE,
        (
            "With the corrupt Imperial and Republican faction\x01",
            "congressmen involved in the cult incident gone, even\x01",
            "that Revache & Co. disappeared from the underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And yet, the status quo of Imperial\x01",
            "faction congressmen occupying more\x01",
            "seats hasn't changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hear about his efforts to speed\x01",
            "up legal reforms, but... Mayor\x01",
            "Crois has to do much, much more.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2571")

    label("loc_249B")


    ChrTalk(
        0xFE,
        (
            "...I believe they were\x01",
            "Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumor has it that they've\x01",
            "started to throw their weight\x01",
            "around with Revache gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Making laws so the citizens\x01",
            "can live safely... Mayor Crois\x01",
            "has to do much, much more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2571")

    TalkEnd(0xFE)
    Return()

    # Function_1_1005 end

    def Function_2_2575(): pass

    label("Function_2_2575")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2617")

    ChrTalk(
        0xFE,
        (
            "Well then, I guess I'll\x01",
            "return to Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "City Hall is probably in chaos\x01",
            "too, but anyhow, nothing will\x01",
            "start if I don't show up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2625")
    Jump("loc_3510")

    label("loc_2625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2633")
    Jump("loc_3510")

    label("loc_2633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_278F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2705")

    ChrTalk(
        0xFE,
        (
            "Haha. Mimi is so\x01",
            "innocent and cute, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But even so, why did the\x01",
            "armed group take\x01",
            "Crossbell's bell with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't see it as being\x01",
            "something worth\x01",
            "stealing, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_278A")

    label("loc_2705")


    ChrTalk(
        0xFE,
        (
            "Even so, why did the armed\x01",
            "group take Crossbell's\x01",
            "bell with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't see it as being\x01",
            "something worth\x01",
            "stealing, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_278A")

    Jump("loc_3510")

    label("loc_278F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27FB")

    ChrTalk(
        0xFE,
        (
            "I'm worried about the people\x01",
            "of Mainz... There are probably\x01",
            "kids Mimi's age there too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_27FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2853")

    ChrTalk(
        0xFE,
        "Hey, Mimi, look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Snail is going to\x01",
            "and fro on the handrail.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2916")

    ChrTalk(
        0xFE,
        (
            "It's only natural,\x01",
            "but... The ambulances\x01",
            "were quite in a rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although emergency vehicles like them\x01",
            "have no speed restrictions, watching\x01",
            "them makes you a little nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A33")

    ChrTalk(
        0xFE,
        (
            "Hmm, orbal vehicles\x01",
            "really are nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But unfortunately, their\x01",
            "price is still high and the\x01",
            "masses can't afford them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If half of them were to drop in price by just\x01",
            "20%, they would become easier to afford,\x01",
            "although it would still be difficult.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2AB6")

    label("loc_2A33")


    ChrTalk(
        0xFE,
        (
            "Hmm, orbal vehicles\x01",
            "really are nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's impossible right now, but\x01",
            "I'd like to get one before I\x01",
            "reach retirement age.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB6")

    Jump("loc_3510")

    label("loc_2ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C53")

    ChrTalk(
        0xFE,
        (
            "Lately, it seems society is\x01",
            "paying attention to nothing\x01",
            "but talk of independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just wish the government\x01",
            "wouldn't forget the traffic basic\x01",
            "law announced the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the legal reform, in addition\x01",
            "to the current penalty system, a\x01",
            ""suspension of license" was added.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that with this, orbal\x01",
            "vehicle accidents will decrease,\x01",
            "even if only by a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D3D")

    label("loc_2C53")


    ChrTalk(
        0xFE,
        (
            "From now on, if you commit certain infractions,\x01",
            "your driving license will be suspended for a\x01",
            "period... In other words, you can't drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that with this, orbal\x01",
            "vehicle accidents will decrease,\x01",
            "even if only by a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3D")

    Jump("loc_3510")

    label("loc_2D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D50")
    Jump("loc_3510")

    label("loc_2D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2DAB")

    ChrTalk(
        0xFE,
        (
            "Well then, sorry to have\x01",
            "kept you waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Then, let's go at once.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2DB9")
    Jump("loc_3510")

    label("loc_2DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E6B")

    ChrTalk(
        0xFE,
        (
            "As a consequence of the City Hall\x01",
            "transfer, it was decided that I'll be\x01",
            "working at Orchis Tower for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, it looks like\x01",
            "I'll be quite busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_2E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_329D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3207")

    ChrTalk(
        0xFE,
        (
            "I saw you yesterday... It looked\x01",
            "like you were boarding quite the\x01",
            "rare orbal car, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, it's actually ZCF's\x01",
            "latest model.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    ChrTalk(
        0xFE,
        (
            "What, an orbal car by\x01",
            "that ZCF!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "B-By any chance, do you\x01",
            "know its top speed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FWell, we haven't tested\x01",
            "it yet, but it's around\x01",
            "1500 selge per hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "G-Goodness!! To think that model\x01",
            "has that kind of speed! The ZCF\x01",
            "must have been at it for a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I don't know what to say. With\x01",
            "this, I guess we've entered an era\x01",
            "with three major automakers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. If that's the case, then\x01",
            "things are going to get more\x01",
            "interesting from now on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FI know, right~!\x02\x03",
            "Competition is going to heat up,\x01",
            "and more terrific cuties are\x01",
            "going to steadily begin to...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#00012FS-She's quite fired up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*. You really do\x01",
            "like them, don't you\x01",
            "Noｱl.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 0)
    Jump("loc_3298")

    label("loc_3207")


    ChrTalk(
        0xFE,
        (
            "Who would've thought ZCF\x01",
            "was developing orbal\x01",
            "cars!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmhm. Well from now, on I\x01",
            "won't be able to keep my eyes\x01",
            "off each company's trends!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3298")

    Jump("loc_3510")

    label("loc_329D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3510")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3320")

    ChrTalk(
        0xFE,
        (
            "The traffic laws are in\x01",
            "urgent need of\x01",
            "adjustment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd afraid to let Mimi\x01",
            "play by herself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3510")

    label("loc_3320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3437")

    ChrTalk(
        0xFE,
        (
            "Earlier, I saw an orbal car\x01",
            "driving through Central Square\x01",
            "at an incredible speed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it was clearly a\x01",
            "dangerous speed, I immediately\x01",
            "reported it to the police, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if they caught\x01",
            "them. ...I'm worried that\x01",
            "they'll show up again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3510")

    label("loc_3437")


    ChrTalk(
        0xFE,
        (
            "Although, with the current traffic basic\x01",
            "laws, even if caught for reckless\x01",
            "driving, they'd get off with just a fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, Congress has been\x01",
            "strengthening penalties lately,\x01",
            "so I have hope for the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3510")

    TalkEnd(0xFE)
    Return()

    # Function_2_2575 end

    def Function_3_3514(): pass

    label("Function_3_3514")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_360B")

    ChrTalk(
        0xFE,
        (
            "Since my husband says he's\x01",
            "going back to City Hall, I\x01",
            "think we'll return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a lot of things to worry about going\x01",
            "forward, but... I feel that if we stay together\x01",
            "as a family, there's nothing we can't overcome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C30")

    label("loc_360B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3619")
    Jump("loc_3C30")

    label("loc_3619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_36B6")

    ChrTalk(
        0xFE,
        (
            "We can't do anything about\x01",
            "it, but... I saw almost no\x01",
            "tourists last week...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wonder what will\x01",
            "become of Crossbell from\x01",
            "now on...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C30")

    label("loc_36B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_378B")

    ChrTalk(
        0xFE,
        (
            "Since I'm on vacation from my job\x01",
            "as a tour guide, we three are\x01",
            "spending time together as family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about many things in\x01",
            "the future, but... This child's\x01",
            "smile is a relief for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C30")

    label("loc_378B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3799")
    Jump("loc_3C30")

    label("loc_3799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_37A7")
    Jump("loc_3C30")

    label("loc_37A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_37B5")
    Jump("loc_3C30")

    label("loc_37B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_37C3")
    Jump("loc_3C30")

    label("loc_37C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_37D1")
    Jump("loc_3C30")

    label("loc_37D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_39CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390E")

    ChrTalk(
        0xFE,
        "Umm, ahem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Behind me to your right,\x01",
            "everyone, you can see\x01",
            "the Orbal Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its name, Genten, is famous\x01",
            "throughout the continent as a\x01",
            "store where orbal goods gather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's this era's cutting edge store\x01",
            "that is of course popular with the\x01",
            "citizens, but also among tourists.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39C9")

    label("loc_390E")


    ChrTalk(
        0xFE,
        (
            "Umm, behind me to your\x01",
            "right, everyone, you can\x01",
            "see Orbal Store Genten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's this era's cutting edge store\x01",
            "that is of course popular with the\x01",
            "citizens, but also among tourists.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C9")

    Jump("loc_3C30")

    label("loc_39CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3A0C")

    ChrTalk(
        0xFE,
        (
            "Yes, let's hurry. Mimi\x01",
            "and I are starving.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C30")

    label("loc_3A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A27")
    Call(1, 6)
    Jump("loc_3C06")

    label("loc_3A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B67")

    ChrTalk(
        0xFE,
        "Umm, ahem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To your right everyone,\x01",
            "you can see the\x01",
            "Crossbell Bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is said to have been created\x01",
            "more than 500 years ago during\x01",
            "Crossbell's middle ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After its excavation in year 1185 of the\x01",
            "Septian Calendar, it is now a fitting symbol\x01",
            "of the city that the citizens know well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C06")

    label("loc_3B67")


    ChrTalk(
        0xFE,
        (
            "Umm, to your right\x01",
            "everyone, you can see\x01",
            "the Crossbell Bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is said to have been created\x01",
            "more than 500 years ago during\x01",
            "Crossbell's middle ages.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C06")

    Jump("loc_3C30")

    label("loc_3C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C19")
    Jump("loc_3C30")

    label("loc_3C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3C27")
    Jump("loc_3C30")

    label("loc_3C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3C30")

    label("loc_3C30")

    TalkEnd(0xFE)
    Return()

    # Function_3_3514 end

    def Function_4_3C34(): pass

    label("Function_4_3C34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0B")

    ChrTalk(
        0xFE,
        (
            "Papa says that he's\x01",
            "going to work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, you're\x01",
            "always working, right\x01",
            "Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mimi is always cheering\x01",
            "for you you know, so do\x01",
            "your best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D78")

    label("loc_3D0B")


    ChrTalk(
        0xFE,
        (
            "Papa and you guys are\x01",
            "always doing your best\x01",
            "with work, aren't you~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mimi will be rooting for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D78")

    Jump("loc_48B6")

    label("loc_3D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3D8B")
    Jump("loc_48B6")

    label("loc_3D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF3")

    ChrTalk(
        0xFE,
        (
            "That orbal car with the\x01",
            "screen was cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Father seems to be\x01",
            "happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E55")

    label("loc_3DF3")


    ChrTalk(
        0xFE,
        (
            "Father says he's busy\x01",
            "with his City Hall job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My tour guide mom is on\x01",
            "vacation, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E55")

    Jump("loc_48B6")

    label("loc_3E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE3")

    ChrTalk(
        0xFE,
        (
            "Umm, to your right,\x01",
            "everyone, you can see\x01",
            "the Crossbell Beeell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Oh, what? Where did\x01",
            "the bell go?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F13")

    label("loc_3EE3")


    ChrTalk(
        0xFE,
        (
            "I wonder where Crossbell\x01",
            "Bell has gone...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F13")

    Jump("loc_48B6")

    label("loc_3F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_409F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4021")

    ChrTalk(
        0xFE,
        (
            "There's a lot of people\x01",
            "with pained expressions\x01",
            "today for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, you guys too...\x01",
            "That's no good, you have\x01",
            "to cheer up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAh, yes, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThank you, Mimi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No. You're welcome, you\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_409A")

    label("loc_4021")


    ChrTalk(
        0xFE,
        (
            "There's a lot of people\x01",
            "with pained expressions\x01",
            "today for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Sun smiles upon\x01",
            "everyone, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_409A")

    Jump("loc_48B6")

    label("loc_409F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_40DB")

    ChrTalk(
        0xFE,
        "Waah, it's true!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is he lost, maybe?\x02",
    )

    CloseMessageWindow()
    Jump("loc_48B6")

    label("loc_40DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_414C")

    ChrTalk(
        0xFE,
        (
            "When an ambulance passes\x01",
            "through, you have to\x01",
            "make way, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's a traffic rule.\x02",
    )

    CloseMessageWindow()
    Jump("loc_48B6")

    label("loc_414C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_420A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41CE")

    ChrTalk(
        0xFE,
        "*sweep, sweep*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like father is\x01",
            "thinking about cars\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He really likes them.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4205")

    label("loc_41CE")


    ChrTalk(
        0xFE,
        "*sweep, sweep*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The passenger seat is\x01",
            "Mimi's.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4205")

    Jump("loc_48B6")

    label("loc_420A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_42F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_428F")

    ChrTalk(
        0xFE,
        (
            "Umm, to your right,\x01",
            "everyone, you can see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhhm, your right... is\x01",
            "your right, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_42EE")

    label("loc_428F")


    ChrTalk(
        0xFE,
        (
            "Uhhm, what was mother\x01",
            "saying again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What you can see to your\x01",
            "right is... your right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42EE")

    Jump("loc_48B6")

    label("loc_42F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_434E")

    ChrTalk(
        0xFE,
        "Hmhm, I see I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to go buy some\x01",
            "presents. *flash flash*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B6")

    label("loc_434E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_43D8")

    ChrTalk(
        0xFE,
        (
            "Eating out, eating out,\x01",
            "today I'm eating out♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mimi, you know, wants to\x01",
            "eat the "eastern\x01",
            "cuisine" of East Street.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B6")

    label("loc_43D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_443F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F3")
    Call(1, 6)
    Jump("loc_443A")

    label("loc_43F3")


    ChrTalk(
        0xFE,
        "Hmhm, I see I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've gotta photograph\x01",
            "this. *flash flash*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_443A")

    Jump("loc_48B6")

    label("loc_443F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_473A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4632")
    TurnDirection(0xB, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Ah, there's a kid I\x01",
            "don't know with you\x01",
            "guys, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ehehe, those clothes are\x01",
            "cool. They're Eastern,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "Oh, you noticed the\x01",
            "quality of these\x01",
            "clothes... How promising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hehe. These are a set of\x01",
            "unique, order-made\x01",
            "clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Older maid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ohh, so those are a\x01",
            "maid's clothes...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "No, that's not it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Haha. That exchange was\x01",
            "pretty funny.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DC, 6)
    Jump("loc_46B7")

    label("loc_4632")

    TurnDirection(0xB, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "A maid, huh? Wait, could\x01",
            "you actually be a girl?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "I already told you,\x01",
            "that's not it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B7")

    Jump("loc_4735")

    label("loc_46BC")


    ChrTalk(
        0xFE,
        (
            "Daddy says that he won't\x01",
            "be able to play with\x01",
            "Mimi for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, since it's\x01",
            "work, I'll have to\x01",
            "endure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4735")

    Jump("loc_48B6")

    label("loc_473A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4755")
    Call(1, 5)
    Jump("loc_47E9")

    label("loc_4755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B3")

    ChrTalk(
        0xFE,
        (
            "Splish splash, splish\x01",
            "splash♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's raining today~,\x01",
            "just raining.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_47E9")

    label("loc_47B3")


    ChrTalk(
        0xFE,
        (
            "Mimi's dad is extremely\x01",
            "fond of cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah!\x02",
    )

    CloseMessageWindow()

    label("loc_47E9")

    Jump("loc_48B6")

    label("loc_47EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_48B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4853")

    ChrTalk(
        0xFE,
        (
            "Let's ride in cars\x01",
            "following the rules!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mimi knows them too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_48B6")

    label("loc_4853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4865")
    Call(1, 5)
    Jump("loc_48B6")

    label("loc_4865")


    ChrTalk(
        0xFE,
        (
            "Everyone of the New Special\x01",
            "Support Section, do your\x01",
            "best with work, okay~?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B6")

    TalkEnd(0xFE)
    Return()

    # Function_4_3C34 end

    def Function_5_48BA(): pass

    label("Function_5_48BA")


    ChrTalk(
        0xB,
        (
            "Ah, Lloyd and Elie!\x01",
            "And...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "What? Where are Tio and\x01",
            "Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Is the Special Support\x01",
            "Section still on break\x01",
            "for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FNo, that's not the case,\x01",
            "but...\x02\x03",
            "#00000FThose two have other\x01",
            "things they need to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, and also, these two\x01",
            "are our new members.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "Wow, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Then, you guys are the\x01",
            "New Special Support\x01",
            "Section, yeah?♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, what precise\x01",
            "naming, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHaha, nice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yes, nice to meet you!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 1)
    Return()

    # Function_5_48BA end

    def Function_6_4ACB(): pass

    label("Function_6_4ACB")

    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0xF, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "Ah, it's Lloyd and\x01",
            "friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'll introduce you to\x01",
            "Mimi's mom. She's a tour\x01",
            "guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*giggle*, pleased to\x01",
            "meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Thank you. I hear you're\x01",
            "always looking after my\x01",
            "daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUm, it's actually no big\x01",
            "deal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat aside, it must be\x01",
            "nice to be a tour guide.\x02\x03",
            "Are you working today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "No, I'm on vacation for\x01",
            "the duration of the\x01",
            "trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "And so, I plan to spend\x01",
            "this time with my\x01",
            "daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHmm. And yet, you're\x01",
            "wearing your uniform?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Eh, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Mimi begged her to wear\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We're going to play Miss\x01",
            "Guide make-believe now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHaha, I see. Aren't you\x01",
            "happy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yup, I am!♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Stay safe, everyone. See\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xB, 0x0, 0x0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x14A, 2)
    Return()

    # Function_6_4ACB end

    def Function_7_4DC6(): pass

    label("Function_7_4DC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4E12")

    ChrTalk(
        0xFE,
        (
            "What's with that huge\x01",
            "tree? Isn't it...\x01",
            "unbelievable?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_4E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4E20")
    Jump("loc_55CE")

    label("loc_4E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4E49")

    ChrTalk(
        0xFE,
        "Arios was super cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_4E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4EC4")

    ChrTalk(
        0xFE,
        (
            "I heard they're doing a\x01",
            "charity event in\x01",
            "Governmental DIstrict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't we go take a\x01",
            "quick look?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_4EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4F8E")

    ChrTalk(
        0xFE,
        (
            "A mysterious armed group, it's too scary!\x01",
            "Papa says we have to be independent just\x01",
            "so those guys don't make fools of us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A referendum, huh? If\x01",
            "we'd been 18, we\x01",
            "could've voted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_4F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4F9C")
    Jump("loc_55CE")

    label("loc_4F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_500E")

    ChrTalk(
        0xFE,
        (
            "Those ambulances were really\x01",
            "moving. ...I hope they don't get\x01",
            "into an accident in their hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_500E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_50A9")

    ChrTalk(
        0xFE,
        (
            "Huh, you're stopping\x01",
            "your diet!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "J-J-Just because you have strangely\x01",
            "pretty face... it doesn't mean I\x01",
            "can't be like you, you know!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_50A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5103")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...All things\x01",
            "considered, should I\x01",
            "exercise or diet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_5103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_51A2")

    ChrTalk(
        0xFE,
        (
            "Hey, they say that Arios\x01",
            "and Archduke Albert are\x01",
            "really good friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How nice! If I could,\x01",
            "I'd like to be good\x01",
            "friends with them too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_51A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51C2")
    Call(1, 8)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_5211")

    label("loc_51C2")


    ChrTalk(
        0xFE,
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(...Judging by her\x01",
            "reaction, she isn't\x01",
            "doing it at all.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5211")

    Jump("loc_55CE")

    label("loc_5216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_52E2")

    ChrTalk(
        0xFE,
        (
            "Did you see Archduke\x01",
            "Albert!? Isn't his goatee\x01",
            "just the dreamiest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Chancellor Osborne is cool\x01",
            "too, but I guess he'd be\x01",
            "harder to approach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, they both have a\x01",
            "nice beard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_52E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_53A5")

    ChrTalk(
        0xFE,
        (
            "It goes without saying\x01",
            "that Arios is dreamy,\x01",
            "but Mayor Dieter is too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, rather than a lover, he seems\x01",
            "like the ideal father. I wonder if\x01",
            "I could get myself adopted...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_53A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_53B3")
    Jump("loc_55CE")

    label("loc_53B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_55CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_541D")

    ChrTalk(
        0xFE,
        (
            "...Yes? Do you need\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm a little busy at the\x01",
            "moment...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CE")

    label("loc_541D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5556")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F0")

    ChrTalk(
        0xFE,
        (
            "Moments ago, a weird\x01",
            "redhead hit on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was quite cool, but when I told him\x01",
            "he wasn't my type, he said "You aren't\x01",
            "mine either, don't sweat it☆"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "G-GRRRRRR!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5551")

    label("loc_54F0")


    ChrTalk(
        0xFE,
        (
            "I mean, if he's hitting\x01",
            "on me, what does he mean\x01",
            "by "You aren't my type"!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "G-GRRRRRR!!\x02",
    )

    CloseMessageWindow()

    label("loc_5551")

    Jump("loc_55CE")

    label("loc_5556")


    ChrTalk(
        0xFE,
        (
            "Homework? I don't have\x01",
            "time for that kind of\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, by the way... It\x01",
            "seems Arios is away\x01",
            "again, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55CE")

    TalkEnd(0xFE)
    Return()

    # Function_7_4DC6 end

    def Function_8_55D2(): pass

    label("Function_8_55D2")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "By the way, Lenalee, are\x01",
            "you keeping up with your\x01",
            "jogging?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Eh, oh, yes... Well,\x01",
            "more or less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think forced dieting\x01",
            "isn't good, so lately I do\x01",
            "it when I feel like it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm. Is that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "(...Judging by her\x01",
            "reaction, she isn't\x01",
            "doing it at all.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_8_55D2 end

    def Function_9_56F9(): pass

    label("Function_9_56F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5775")

    ChrTalk(
        0xFE,
        (
            "Yes, it emits a pretty\x01",
            "pale light, but... It's\x01",
            "super weird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if something\x01",
            "will happen...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_5775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5783")
    Jump("loc_5F9C")

    label("loc_5783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_582A")

    ChrTalk(
        0xFE,
        (
            "Yes, yes, and that white\x01",
            "military uniform looked\x01",
            "amazing on him too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as Arios is around,\x01",
            "I think we'll be fine no\x01",
            "matter what happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_582A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_58BC")

    ChrTalk(
        0xFE,
        (
            "You're right. His taking\x01",
            "part in something like that\x01",
            "must have some meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, let's go\x01",
            "invite the others too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_58BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_594A")

    ChrTalk(
        0xFE,
        "We're still 15, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, I don't get the pros and\x01",
            "cons of independence... Honestly,\x01",
            "it's a relief I can't vote.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_594A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5958")
    Jump("loc_5F9C")

    label("loc_5958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5999")

    ChrTalk(
        0xFE,
        (
            "Geez Pluna, don't say\x01",
            "such disturbing things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_5999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A06")

    ChrTalk(
        0xFE,
        "...I've made up my mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll quit dieting and\x01",
            "find a boy who likes me\x01",
            "for how I am.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_5A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5AA0")

    ChrTalk(
        0xFE,
        (
            "*sigh*, isn't there a way\x01",
            "that doesn't involve exercise\x01",
            "or dietary restrictions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll do anything, so\x01",
            "someone, please tell\x01",
            "meee!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_5AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B38")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, Arios was\x01",
            "awarded a decoration from the\x01",
            "Principality of Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was that when those two\x01",
            "became friends?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_5B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B58")
    Call(1, 8)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_5BD4")

    label("loc_5B58")


    ChrTalk(
        0xFE,
        (
            "E-Even if you say "feel\x01",
            "inclined", you have to\x01",
            "keep at it, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see, then today\x01",
            "I'll run and then go\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BD4")

    Jump("loc_5F9C")

    label("loc_5BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5DB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CED")

    ChrTalk(
        0xFE,
        (
            "Beard beard beard... You\x01",
            "like them too, eh,\x01",
            "Pluna?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even better, I think that tall\x01",
            "soldier who was standing near\x01",
            "Prince Olivert is my type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love to be carried in the arms\x01",
            "of a man with a physique like\x01",
            "that, even if it's just once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5DAE")

    label("loc_5CED")


    ChrTalk(
        0xFE,
        (
            "Even better, I think that tall\x01",
            "soldier who was standing near\x01",
            "Prince Olivert is my type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love to be carried in the arms\x01",
            "of a man with a physique like\x01",
            "that, even if it's just once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DAE")

    Jump("loc_5F9C")

    label("loc_5DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E2B")

    ChrTalk(
        0xFE,
        (
            "Indeed, Mayor Crois\x01",
            "might be the ideal\x01",
            "father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, he doesn't\x01",
            "look old like my father.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_5E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5E39")
    Jump("loc_5F9C")

    label("loc_5E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5F9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E9E")

    ChrTalk(
        0xFE,
        (
            "Dangerous driving?\x01",
            "Dunnooo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We were too focused on\x01",
            "chatting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_5E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F22")

    ChrTalk(
        0xFE,
        (
            "...That redhead was\x01",
            "weird somehow, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He went inside the\x01",
            "department store... Who\x01",
            "was he, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9C")

    label("loc_5F22")


    ChrTalk(
        0xFE,
        (
            "Aah, now that I think\x01",
            "about it, I have Sunday\x01",
            "School this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pluna, did you do the\x01",
            "homework they gave us?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F9C")

    TalkEnd(0xFE)
    Return()

    # Function_9_56F9 end

    def Function_10_5FA0(): pass

    label("Function_10_5FA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6048")

    ChrTalk(
        0xFE,
        (
            "W-Why is such a huge tree\x01",
            "is floating in the air?\x01",
            "It's physically impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, is it alright for\x01",
            "me to be here giving\x01",
            "away balloons...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6C")

    label("loc_6048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6056")
    Jump("loc_6B6C")

    label("loc_6056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6136")

    ChrTalk(
        0xFE,
        (
            "Crossbell independence,\x01",
            "eh...? Things really got\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if it's not a festive atmosphere, for the\x01",
            "time being I guess I'll make original balloons\x01",
            "as if it was the Founding Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6C")

    label("loc_6136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6144")
    Jump("loc_6B6C")

    label("loc_6144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_620D")

    ChrTalk(
        0xFE,
        (
            "I don't know if they're an armed\x01",
            "group or not, but still, they did\x01",
            "some totally terrible things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I want to tell\x01",
            "them, "I'll give you a\x01",
            "balloon, so go away at once."\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6C")

    label("loc_620D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_621B")
    Jump("loc_6B6C")

    label("loc_621B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_62AD")

    ChrTalk(
        0xFE,
        (
            "Do you want a balloooon?\x01",
            "...I feel it's not the\x01",
            "time to say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, an accident, they\x01",
            "say. What on earth has\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6C")

    label("loc_62AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_63EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6376")

    ChrTalk(
        0xFE,
        "Do you want a balloooon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Adults are welcome too,\x01",
            "don't be shy now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't you sometimes want to\x01",
            "forget about complex things and\x01",
            "relive your childish innocence?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_63E6")

    label("loc_6376")


    ChrTalk(
        0xFE,
        (
            "Adults are welcome too,\x01",
            "don't be shy now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't you sometimes want\x01",
            "to relive your childish\x01",
            "innocence?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63E6")

    Jump("loc_6B6C")

    label("loc_63EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6568")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64FE")

    ChrTalk(
        0xFE,
        (
            "Some time ago I was asked\x01",
            "by a tourist child this:\x01",
            ""Why do balloons float?"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, without a moment's\x01",
            "delay I replied: "Because\x01",
            "they're filled with dreams"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Children these days are\x01",
            "cruel. As soon as I said\x01",
            "that, he sneered at me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6563")

    label("loc_64FE")


    ChrTalk(
        0xFE,
        (
            "Have more dreams,\x01",
            "children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A gas lighter than air?\x01",
            "Nope, balloons are\x01",
            "filled with dreams.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6563")

    Jump("loc_6B6C")

    label("loc_6568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6601")

    ChrTalk(
        0xFE,
        "Do you want a balloooon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I have balloons with crests of\x01",
            "the countries participating in the\x01",
            "trade conference printed on them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6C")

    label("loc_6601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_66AE")

    ChrTalk(
        0xFE,
        (
            "Well then, I guess I'll\x01",
            "make my way back home\x01",
            "for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank goodness. Many people\x01",
            "passed by today and I was able\x01",
            "to hand out a lot of balloons.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6C")

    label("loc_66AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6765")

    ChrTalk(
        0xFE,
        (
            "Well, I was really\x01",
            "nervous when the\x01",
            "limousines passed by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say it... It's a different\x01",
            "kind of enthusiasm than that of\x01",
            "the Founding Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6C")

    label("loc_6765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_69B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D1")
    TurnDirection(0xE, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "Oh, you there, little boy. Say,\x01",
            "do you want a balloon? It's fun,\x01",
            "it floats lightly and gently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "...I don't wanna. It'd\x01",
            "just be in my way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Alright, then, what color\x01",
            "do you w...wait, what? In\x01",
            "the way, you said?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Haha. It seems Shing\x01",
            "doesn't like childish\x01",
            "things.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1DD, 1)
    Jump("loc_6950")

    label("loc_68D1")


    ChrTalk(
        0xE,
        (
            "Yes, there are kids who aren't\x01",
            "interested in balloons, but...\x01",
            "To refuse it so bluntly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "That's a little\x01",
            "depressing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6950")

    Jump("loc_69B0")

    label("loc_6955")


    ChrTalk(
        0xFE,
        "Do you want a balloooon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Red, blue, yellow and\x01",
            "green. I have different\x01",
            "colooors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69B0")

    Jump("loc_6B6C")

    label("loc_69B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_69C3")
    Jump("loc_6B6C")

    label("loc_69C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6B6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A4F")

    ChrTalk(
        0xFE,
        (
            "That car back there\x01",
            "scared me and I let go\x01",
            "of some balloons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, what a waste...\x01",
            "Come baaack...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6C")

    label("loc_6A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AF7")

    ChrTalk(
        0xFE,
        (
            "Do you want a balloooon?\x01",
            "Please take one with you while\x01",
            "sightseeing in Crossbeeell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I assure you, it'll put\x01",
            "you in a happy and good\x01",
            "mooood!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6B6C")

    label("loc_6AF7")


    ChrTalk(
        0xFE,
        (
            "I give balloons also to\x01",
            "people who aren't\x01",
            "tourists~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please let me know if\x01",
            "there's someone who\x01",
            "wants one~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B6C")

    TalkEnd(0xFE)
    Return()

    # Function_10_5FA0 end

    def Function_11_6B70(): pass

    label("Function_11_6B70")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_6B81")
    Jump("loc_6E45")

    label("loc_6B81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6C45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C24")

    ChrTalk(
        0x11,
        "#01203FGrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha. When you're here\x01",
            "like this, it makes you\x01",
            "look like a guard dog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6C40")

    label("loc_6C24")


    ChrTalk(
        0x11,
        "#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_6C40")

    Jump("loc_6E45")

    label("loc_6C45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6C56")
    Jump("loc_6E45")

    label("loc_6C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C64")
    Jump("loc_6E45")

    label("loc_6C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C85")
    Call(1, 23)
    Return()

    label("loc_6C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E26")

    ChrTalk(
        0x11,
        "#01203FGrrrowl......\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DA8")

    ChrTalk(
        0x101,
        "#00005FUhm? Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        (
            "#01100F"Nope, nothing at all",\x01",
            "he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I see.\x02\x03",
            "#00000FWell, please watch the\x01",
            "house today too, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        (
            "#01109FZeit, see you later,\x01",
            "ok!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200FWoof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E1E")

    label("loc_6DA8")


    ChrTalk(
        0x101,
        (
            "#00003F(Looks like he still had something\x01",
            "he wanted to say... If Tio or KeA\x01",
            "were here, we could understand him.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E1E")

    SetScenarioFlags(0x1, 1)
    Jump("loc_6E40")

    label("loc_6E26")


    ChrTalk(
        0x11,
        "#01203FGrrrowl......\x02",
    )

    CloseMessageWindow()

    label("loc_6E40")

    Jump("loc_6E45")

    label("loc_6E45")

    TalkEnd(0xFE)
    Return()

    # Function_11_6B70 end

    def Function_12_6E49(): pass

    label("Function_12_6E49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7021")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F74")

    ChrTalk(
        0xFE,
        (
            "Things have gotten\x01",
            "serious, but don't be\x01",
            "discouraged, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all the hardships you guys\x01",
            "went through, I'm sure you'll be\x01",
            "able to solve this incident too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guarantee it. So have\x01",
            "some confidence in\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... Thanks, Officer\x01",
            "Kate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_701C")

    label("loc_6F74")


    ChrTalk(
        0xFE,
        (
            "I'm sure that you and the\x01",
            "others will be able to\x01",
            "solve this incident too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Have some confidence in\x01",
            "yourself! We from the Patrol\x01",
            "Division will do our best too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_701C")

    Jump("loc_7D69")

    label("loc_7021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_702F")
    Jump("loc_7D69")

    label("loc_702F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_703D")
    Jump("loc_7D69")

    label("loc_703D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_704B")
    Jump("loc_7D69")

    label("loc_704B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_72C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F2")

    ChrTalk(
        0xFE,
        (
            "There's of course a lot of\x01",
            "citizens shocked by the\x01",
            "Mainz occupation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also get the feeling there\x01",
            "are many who think it's none\x01",
            "of their business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, I get the feeling there's been\x01",
            "an increase in state independence\x01",
            "supporters due to the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, we need to pay attention not only\x01",
            "to people's needs but also their anxieties,\x01",
            "so that disturbances don't occur.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_72C0")

    label("loc_71F2")


    ChrTalk(
        0xFE,
        (
            "It appears all kinds of\x01",
            "thoughts are spreading\x01",
            "amongst the citizens, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, we need to pay attention not only\x01",
            "to people's needs but also their anxieties,\x01",
            "so that disturbances don't occur.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72C0")

    Jump("loc_7D69")

    label("loc_72C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7388")

    ChrTalk(
        0xFE,
        (
            "I felt relieved after hearing that\x01",
            "transcontinental rail service was\x01",
            "restored this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think things would've been\x01",
            "hard in this rain if we\x01",
            "couldn't use the railway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D69")

    label("loc_7388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7455")

    ChrTalk(
        0xFE,
        (
            "A derailment... Another\x01",
            "difficult situation has\x01",
            "arisen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, the volume of orbal vehicle traffic\x01",
            "will probably be elevated for a while. I've\x01",
            "got to do my best to direct traffic!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D69")

    label("loc_7455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75EB")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "*tweet tweet, tweet\x01",
            "tweet*!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please go slow with your orbal\x01",
            "vehicles. Please cooperate to\x01",
            "keep the city saaafe!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "Could this be an effect of the independence\x01",
            "proposal...? I get the feeling that incoming orbal\x01",
            "vehicle traffic from abroad has decreased somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, while that may be true,\x01",
            "we need to continue to be on\x01",
            "guard against accidents.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_766B")

    label("loc_75EB")

    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "*tweet tweet, tweet\x01",
            "tweet*!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please go slow with your orbal\x01",
            "vehicles. Please cooperate to\x01",
            "keep the city saaafe!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_766B")

    Jump("loc_7D69")

    label("loc_7670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7962")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7885")

    ChrTalk(
        0xFE,
        (
            "There seems to be more and more\x01",
            "people who don't respect orbal\x01",
            "vehicle traffic rules lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Traffic rules" are just words;\x01",
            "drivers' morals and manners are\x01",
            "most important of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Disrespecting the morals everyone should've\x01",
            "been taught at Sunday School when they\x01",
            "become adults... That's really sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys too. When you get behind\x01",
            "the wheel, always be aware of the\x01",
            "people around you, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, that goes without\x01",
            "saying!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Certainly. We'll keep\x01",
            "that in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_795D")

    label("loc_7885")


    ChrTalk(
        0xFE,
        (
            ""Traffic rules" are just words;\x01",
            "drivers' morals and manners are\x01",
            "most important of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Disrespecting the morals everyone should've\x01",
            "been taught at Sunday School when they\x01",
            "become adults... That's really sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_795D")

    Jump("loc_7D69")

    label("loc_7962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_79F8")

    ChrTalk(
        0xFE,
        (
            "Terrorists will likely\x01",
            "show up... I can't let\x01",
            "my guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must pay the utmost\x01",
            "attention to suspicious\x01",
            "people and things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D69")

    label("loc_79F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7AC2")

    ChrTalk(
        0xFE,
        (
            "They had me direct the limousines\x01",
            "the VIPs came in on... That was\x01",
            "really quite nerve-wracking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How should I say it... I\x01",
            "could feel their aura, even\x01",
            "though they were inside cars.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D69")

    label("loc_7AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7BB1")

    ChrTalk(
        0xFE,
        (
            "With the number of patrols starting\x01",
            "today, the number of illegally\x01",
            "parked cars has dropped sharply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be nice if it was like this all the\x01",
            "time, but... Well for now it's a good\x01",
            "thing, so I guess I can't complain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D69")

    label("loc_7BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CC2")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "*tweet tweet, tweet tweet*!\x01",
            "Please go slow with your\x01",
            "orbal vehicleees!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "On rainy days, traffic\x01",
            "volume is somewhat more\x01",
            "than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The road surface is easy to\x01",
            "slip on too, so more attention\x01",
            "than usual is required.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7D5B")

    label("loc_7CC2")


    ChrTalk(
        0xFE,
        (
            "On rainy days, traffic\x01",
            "volume is somewhat more\x01",
            "than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The road surface is easy to\x01",
            "slip on too, so more attention\x01",
            "than usual is required.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D5B")

    Jump("loc_7D69")

    label("loc_7D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7D69")

    label("loc_7D69")

    TalkEnd(0xFE)
    Return()

    # Function_12_6E49 end

    def Function_13_7D6D(): pass

    label("Function_13_7D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ED6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DA9")
    Call(0, 104)
    Jump("loc_7E48")

    label("loc_7DA9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "A black transport? One\x01",
            "passed by not long ago and\x01",
            "went towards East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're going after\x01",
            "it, it's best if you use\x01",
            "your orbal car, no?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_7E48")

    Return()

    label("loc_7E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E57")
    Call(1, 26)
    Return()

    label("loc_7E57")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Damn jaegers... Why'd\x01",
            "they steal the Crossbell\x01",
            "Bell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, thinking about\x01",
            "it now won't do any\x01",
            "good, though.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_7ED6")

    Return()

    # Function_13_7D6D end

    def Function_14_7ED7(): pass

    label("Function_14_7ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_804A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F13")
    Call(0, 104)
    Jump("loc_7F90")

    label("loc_7F13")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The transport that passed\x01",
            "by earlier will arrive at\x01",
            "Tangram Gate shortly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray for your success,\x01",
            "everyone!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_7F90")

    Return()

    label("loc_7F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F9F")
    Call(1, 26)
    Return()

    label("loc_7F9F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "For the current CGF, the state of\x01",
            "tension between the major powers\x01",
            "is the biggest concern of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're looking for the\x01",
            ""bell", but patrols take\x01",
            "priority.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_804A")

    Return()

    # Function_14_7ED7 end

    def Function_15_804B(): pass

    label("Function_15_804B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_80B7")

    ChrTalk(
        0xFE,
        (
            "The trade conference is finally\x01",
            "at its climax. I have to\x01",
            "increase my focus even more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81C5")

    label("loc_80B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_814D")

    ChrTalk(
        0xFE,
        (
            "At last, the heads of\x01",
            "state have arrived in\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'm relieved that\x01",
            "the unveiling ceremony\x01",
            "was without incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81C5")

    label("loc_814D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_81C5")

    ChrTalk(
        0xFE,
        (
            "City patrols are scheduled\x01",
            "to take place until the\x01",
            "last day of the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to do my best!\x02",
    )

    CloseMessageWindow()

    label("loc_81C5")

    TalkEnd(0xFE)
    Return()

    # Function_15_804B end

    def Function_16_81C9(): pass

    label("Function_16_81C9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The "State Guard" is not\x01",
            "a force to "fight" but\x01",
            "one to "protect".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're different from those\x01",
            "Imperial and Republican army\x01",
            "savages. So, please, don't worry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_81C9 end

    def Function_17_8276(): pass

    label("Function_17_8276")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Stealing the symbol of\x01",
            "the city... What kind of\x01",
            "harassment is this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They ruined a well known\x01",
            "spot.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_8276 end

    def Function_18_82EA(): pass

    label("Function_18_82EA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The rumor that the bell\x01",
            "vanished was really\x01",
            "true!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An armed group, huh...?\x01",
            "Their true objective is\x01",
            "a mystery.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_82EA end

    def Function_19_8368(): pass

    label("Function_19_8368")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_845D")

    ChrTalk(
        0x12,
        "#01111F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F...KeA? What's wrong?\x01",
            "You're spacing out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#01105FAh... No, it's nothing.\x02\x03",
            "#01109FEveryone, do your best\x01",
            "at work today, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F...?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x159, 1)
    SetScenarioFlags(0x151, 6)
    Jump("loc_8493")

    label("loc_845D")


    ChrTalk(
        0x12,
        (
            "#01109FEveryone, do your best\x01",
            "at work today, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8493")

    TalkEnd(0xFE)
    Return()

    # Function_19_8368 end

    def Function_20_8497(): pass

    label("Function_20_8497")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84B1")
    Call(1, 23)
    Return()

    label("loc_84B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8620")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8620")

    ChrTalk(
        0x104,
        (
            "#00302FHeiya, Koppe, how'ya\x01",
            "been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Nyaa~~ [I'm hungry]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIt looks like he's\x01",
            "hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FOh, I want to try\x01",
            "feeding him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FKoppe will eat with joy\x01",
            "the fish we catch or Cat\x01",
            "Food, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, do we have any\x01",
            "right now...?\x02\x03",
            "#00000FAt any rate, we mustn't\x01",
            "forget to feed him every\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 3)
    TalkEnd(0xFE)
    Return()

    label("loc_8620")

    ClearScenarioFlags(0x1, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_862F")
    Call(1, 22)

    label("loc_862F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86B5")

    ChrTalk(
        0x101,
        (
            "#00005F(Now that I think about\x01",
            "it... Haven't we caught\x01",
            "some fish?)\x02\x03",
            "#00004F(Maybe we should give\x01",
            "one to Koppe.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13A, 0)

    label("loc_86B5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_86E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 1)), scpexpr(EXPR_END)), "loc_86DB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86DB")

    Jump("loc_87E3")

    label("loc_86E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8701")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 0)), scpexpr(EXPR_END)), "loc_86FC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86FC")

    Jump("loc_87E3")

    label("loc_8701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 7)), scpexpr(EXPR_END)), "loc_871D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_871D")

    Jump("loc_87E3")

    label("loc_8722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 6)), scpexpr(EXPR_END)), "loc_873E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_873E")

    Jump("loc_87E3")

    label("loc_8743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8764")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 5)), scpexpr(EXPR_END)), "loc_875F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_875F")

    Jump("loc_87E3")

    label("loc_8764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 4)), scpexpr(EXPR_END)), "loc_8780")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8780")

    Jump("loc_87E3")

    label("loc_8785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_87A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 3)), scpexpr(EXPR_END)), "loc_87A1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87A1")

    Jump("loc_87E3")

    label("loc_87A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_87C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 2)), scpexpr(EXPR_END)), "loc_87C2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87C2")

    Jump("loc_87E3")

    label("loc_87C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_87E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 1)), scpexpr(EXPR_END)), "loc_87E3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D64")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8800")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5F")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "Talk")
    MenuCmd(1, 1, "Give Food")
    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_886D")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_886D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D2A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_88A9")
    MenuCmd(1, 1, "Fighter")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_88CB")
    MenuCmd(1, 1, "Snow Crab")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_88EE")
    MenuCmd(1, 1, "Angel Fish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_890E")
    MenuCmd(1, 1, "Kasagin")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_890E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_8934")
    MenuCmd(1, 1, "Armorica Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8934")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_8955")
    MenuCmd(1, 1, "Tortoise")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8955")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_897C")
    MenuCmd(1, 1, "Tiger Rockfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_897C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_899E")
    MenuCmd(1, 1, "Rockeater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_899E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_89C4")
    MenuCmd(1, 1, "Rainbow Trout")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_89E4")
    MenuCmd(1, 1, "Piranha")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_8A01")
    MenuCmd(1, 1, "Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_8A29")
    MenuCmd(1, 1, "Gluttonous Bass")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_8A47")
    MenuCmd(1, 1, "Trout")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_8A69")
    MenuCmd(1, 1, "Gladiator")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_8A89")
    MenuCmd(1, 1, "Walleye")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A89")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_8AAC")
    MenuCmd(1, 1, "Salamander")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_8ACB")
    MenuCmd(1, 1, "Salmon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8ACB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_8AEB")
    MenuCmd(1, 1, "Arowana")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_8B07")
    MenuCmd(1, 1, "Eel")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_8B2B")
    MenuCmd(1, 1, "Adamantoise")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_8B4E")
    MenuCmd(1, 1, "Queen Crab")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_8B6F")
    MenuCmd(1, 1, "Pirarucu")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_8B8F")
    MenuCmd(1, 1, "Catfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_8BB3")
    MenuCmd(1, 1, "Gold Salmon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_END)), "loc_8BDB")
    MenuCmd(1, 1, "Pale Salamander")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_END)), "loc_8BFE")
    MenuCmd(1, 1, "Noble Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_END)), "loc_8C1F")
    MenuCmd(1, 1, "Emeraude")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_END)), "loc_8C47")
    MenuCmd(1, 1, "Tiger Rockeater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_END)), "loc_8C6D")
    MenuCmd(1, 1, "Crimson Eater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_END)), "loc_8C91")
    MenuCmd(1, 1, "Bull Dragon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C91")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_END)), "loc_8CB8")
    MenuCmd(1, 1, "Giant Pirarucu")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_8CD9")
    MenuCmd(1, 1, "Cat Food")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CD9")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D23")
    Jump("loc_9D1B")

    label("loc_8D23")

    TalkEnd(0xFE)
    EventBegin(0x1)
    OP_4B(0x10, 0xFF)
    Fade(500)
    SetChrPos(0x10, -21980, 1300, -19300, 270)
    SetChrPos(0x0, -23900, 1300, -19070, 89)
    SetChrPos(0x1, -23540, 1300, -20210, 89)
    SetChrPos(0x2, -25020, 1300, -19860, 89)
    SetChrPos(0x3, -25130, 1300, -18930, 89)
    SetChrPos(0x4, -26200, 1300, -19870, 89)
    SetChrPos(0x5, -26790, 1300, -19180, 89)
    OP_68(-23130, 3900, -19610, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        "Nyannyan......㈱\x02",
    )

    CloseMessageWindow()

    def lambda_8DF2():

        label("loc_8DF2")

        TurnDirection(0x0, 0x10, 0)
        Yield()
        Jump("loc_8DF2")

    QueueWorkItem2(0x0, 1, lambda_8DF2)

    def lambda_8E04():

        label("loc_8E04")

        TurnDirection(0x1, 0x10, 0)
        Yield()
        Jump("loc_8E04")

    QueueWorkItem2(0x1, 1, lambda_8E04)

    def lambda_8E16():

        label("loc_8E16")

        TurnDirection(0x2, 0x10, 0)
        Yield()
        Jump("loc_8E16")

    QueueWorkItem2(0x2, 1, lambda_8E16)

    def lambda_8E28():

        label("loc_8E28")

        TurnDirection(0x3, 0x10, 0)
        Yield()
        Jump("loc_8E28")

    QueueWorkItem2(0x3, 1, lambda_8E28)

    def lambda_8E3A():

        label("loc_8E3A")

        TurnDirection(0x4, 0x10, 0)
        Yield()
        Jump("loc_8E3A")

    QueueWorkItem2(0x4, 1, lambda_8E3A)

    def lambda_8E4C():

        label("loc_8E4C")

        TurnDirection(0x5, 0x10, 0)
        Yield()
        Jump("loc_8E4C")

    QueueWorkItem2(0x5, 1, lambda_8E4C)
    SetChrFlags(0x10, 0x8000)
    OP_93(0x10, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x10, 0x1)
    Sound(809, 0, 80, 0)

    def lambda_8E78():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8E78)
    WaitChrThread(0x10, 1)
    Sound(809, 0, 80, 0)

    def lambda_8E9F():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8E9F)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 80, 0)

    def lambda_8EC6():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8EC6)
    WaitChrThread(0x10, 1)
    Sleep(2000)
    OP_93(0x10, 0xB4, 0x1F4)
    Sound(809, 0, 80, 0)

    def lambda_8EF7():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8EF7)
    WaitChrThread(0x10, 1)
    Sound(809, 0, 80, 0)

    def lambda_8F1E():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8F1E)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 80, 0)

    def lambda_8F45():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8F45)
    WaitChrThread(0x10, 1)
    SetChrFlags(0x10, 0x1)
    OP_93(0x10, 0x10E, 0x1F4)
    ClearChrFlags(0x10, 0x8000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    ChrTalk(
        0xFE,
        "Funyaawn......\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_9017")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_900D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15E, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x68, 1)

    label("loc_900D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9017")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_9061")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9057")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15F, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x74),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x74, 1)

    label("loc_9057")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9061")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_90AB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90A1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x160, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x79),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x79, 1)

    label("loc_90A1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_90F5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90EB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x161, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x92),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x92, 1)

    label("loc_90EB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_913F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9135")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x162, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x84),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x84, 1)

    label("loc_9135")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_913F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_9189")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_917F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x163, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x7C, 1)

    label("loc_917F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9189")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_91D3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91C9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x164, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB2, 1)

    label("loc_91C9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_921D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9213")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x165, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x71),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x71, 1)

    label("loc_9213")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_921D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_9267")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x166, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xBA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xBA, 1)

    label("loc_925D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9267")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_92B1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92A7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x167, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x9C, 1)

    label("loc_92A7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_92FB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x168, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x64, 1)

    label("loc_92F1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_9345")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_933B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x169, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x6C, 1)

    label("loc_933B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9345")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_938F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9385")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16A, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x9E, 1)

    label("loc_9385")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_938F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_93D9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93CF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16B, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x8C, 1)

    label("loc_93CF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_9423")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9419")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16C, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xAF, 1)

    label("loc_9419")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9423")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_946D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9463")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16D, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x80),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x80, 1)

    label("loc_9463")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_946D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_94B7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94AD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16E, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x8F, 1)

    label("loc_94AD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_94B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_9501")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94F7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16F, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x9B, 1)

    label("loc_94F7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9501")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_954B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9541")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x170, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x88),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x88, 1)

    label("loc_9541")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_954B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_9595")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_958B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x171, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x97),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x97, 1)

    label("loc_958B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9595")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_95DF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95D5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x172, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x6E, 1)

    label("loc_95D5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_9629")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_961F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x173, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x7E, 1)

    label("loc_961F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9629")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_9673")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9669")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x174, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x72, 1)

    label("loc_9669")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9673")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_96BD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96B3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x175, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB8, 1)

    label("loc_96B3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_96BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_END)), "loc_9707")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96FD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x176, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x66),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x66, 1)

    label("loc_96FD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9707")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_END)), "loc_9751")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9747")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x177, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB6, 1)

    label("loc_9747")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9751")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_END)), "loc_979B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9791")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x178, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB5, 1)

    label("loc_9791")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_979B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_END)), "loc_97E5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97DB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x179, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB4, 1)

    label("loc_97DB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_END)), "loc_982F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9825")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x17A, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB1, 1)

    label("loc_9825")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_982F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_END)), "loc_9879")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_986F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x17B, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xAE, 1)

    label("loc_986F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9879")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_END)), "loc_98C3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98B9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x17C, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xC6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xC6, 1)

    label("loc_98B9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_98C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_9910")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9906")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D9, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3 received.\x02",
        )
    )

    AddItemNumber(0x12D, 3)

    label("loc_9906")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9910")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9937")
    SetScenarioFlags(0x13B, 1)
    Jump("loc_99BA")

    label("loc_9937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9948")
    SetScenarioFlags(0x13B, 0)
    Jump("loc_99BA")

    label("loc_9948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9959")
    SetScenarioFlags(0x13A, 7)
    Jump("loc_99BA")

    label("loc_9959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_996A")
    SetScenarioFlags(0x13A, 6)
    Jump("loc_99BA")

    label("loc_996A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_997B")
    SetScenarioFlags(0x13A, 5)
    Jump("loc_99BA")

    label("loc_997B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_998C")
    SetScenarioFlags(0x13A, 4)
    Jump("loc_99BA")

    label("loc_998C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_999D")
    SetScenarioFlags(0x13A, 3)
    Jump("loc_99BA")

    label("loc_999D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_99AE")
    SetScenarioFlags(0x13A, 2)
    Jump("loc_99BA")

    label("loc_99AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_99BA")
    SetScenarioFlags(0x13A, 1)

    label("loc_99BA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 1)), scpexpr(EXPR_END)), "loc_99D7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 2)), scpexpr(EXPR_END)), "loc_99EA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 3)), scpexpr(EXPR_END)), "loc_99FD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 4)), scpexpr(EXPR_END)), "loc_9A10")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 5)), scpexpr(EXPR_END)), "loc_9A23")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 6)), scpexpr(EXPR_END)), "loc_9A36")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 7)), scpexpr(EXPR_END)), "loc_9A49")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 0)), scpexpr(EXPR_END)), "loc_9A5C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 1)), scpexpr(EXPR_END)), "loc_9A6F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B3D")

    ChrTalk(
        0xFE,
        "Nyannyannya～n......♪\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEE, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AF4")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xEE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xEE, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_9B3D")

    label("loc_9AF4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_9B3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B86")

    ChrTalk(
        0x102,
        (
            "#00105FMy... are you giving\x01",
            "this to me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CDE")

    label("loc_9B86")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BBD")

    ChrTalk(
        0x103,
        "#00205FAre you giving me this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CDE")

    label("loc_9BBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BFF")

    ChrTalk(
        0x104,
        (
            "#00305FYou mean you're givin'\x01",
            "this to me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CDE")

    label("loc_9BFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C3E")

    ChrTalk(
        0x109,
        (
            "#10105FHuh, are you giving this\x01",
            "to me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CDE")

    label("loc_9C3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C78")

    ChrTalk(
        0x105,
        (
            "#10305FOh my, are giving me\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CDE")

    label("loc_9C78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CAD")

    ChrTalk(
        0x106,
        "#10705FUmm... I can have it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CDE")

    label("loc_9CAD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CDE")

    ChrTalk(
        0x10A,
        "#00605FYou're giving me this?\x02",
    )

    CloseMessageWindow()

    label("loc_9CDE")


    ChrTalk(
        0x101,
        (
            "#0000FHaha, thanks. We'll use\x01",
            "it with gratitude.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    EventEnd(0x4)
    Return()

    label("loc_9D1B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D5A")

    label("loc_9D2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D3E")
    Jump("loc_9D5A")

    label("loc_9D3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 21)

    label("loc_9D5A")

    Jump("loc_8800")

    label("loc_9D5F")

    Jump("loc_9D67")

    label("loc_9D64")

    Call(1, 21)

    label("loc_9D67")

    TalkEnd(0xFE)
    Return()

    # Function_20_8497 end

    def Function_21_9D6B(): pass

    label("Function_21_9D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9E66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E35")

    ChrTalk(
        0x10,
        "Nyao...? [What's wrong?]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FKoppe, please watch the\x01",
            "house for a while\x01",
            "longer.\x02\x03",
            "#00200FWe'll bring back KeA for\x01",
            "sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...Nyaaoo~n. [You're\x01",
            "absolutely right]\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9E61")

    label("loc_9E35")


    ChrTalk(
        0x10,
        (
            "...Nyaaoo~n. [You're\x01",
            "absolutely right]\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E61")

    Jump("loc_A378")

    label("loc_9E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_9E74")
    Jump("loc_A378")

    label("loc_9E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9E94")

    ChrTalk(
        0x10,
        "Fumyaaawn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A378")

    label("loc_9E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9EB3")

    ChrTalk(
        0x10,
        "Fumyaawn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A378")

    label("loc_9EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9EDF")

    ChrTalk(
        0x10,
        "Nyaon...? [Who are you?]\x02",
    )

    CloseMessageWindow()
    Jump("loc_A378")

    label("loc_9EDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9EED")
    Jump("loc_A378")

    label("loc_9EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9F18")

    ChrTalk(
        0x10,
        "Nyaya~~go... [Hold up.]\x02",
    )

    CloseMessageWindow()
    Jump("loc_A378")

    label("loc_9F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9F37")

    ChrTalk(
        0x10,
        "Fumyaawn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A378")

    label("loc_9F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9F55")

    ChrTalk(
        0x10,
        "Fumyaaawn.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A378")

    label("loc_9F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A018")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A002")

    ChrTalk(
        0x10,
        (
            "Nyaao. [So, we meet\x01",
            "again, fleshy thing.]\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHaha... Long time no\x01",
            "see, Koppe.\x02\x03",
            "I'll give you food from\x01",
            "now on too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Nyayayaa~㈱\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A013")

    label("loc_A002")


    ChrTalk(
        0x10,
        "Nyayayaa~㈱\x02",
    )

    CloseMessageWindow()

    label("loc_A013")

    Jump("loc_A378")

    label("loc_A018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_A16F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A150")

    ChrTalk(
        0x10,
        (
            "Nyaago. [It's been a\x01",
            "while. How have you\x01",
            "been?]\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600FThe Support Section pet\x01",
            "cat, huh.\x02\x03",
            "#00603F(*pet, pet*...) ...You've\x01",
            "picked a tough place to\x01",
            "be too, haven't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Nyaa~~o......㈱ [That's\x01",
            "right]\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Dudley... He's\x01",
            "unexpectedly good at\x01",
            "dealing with cats...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A16A")

    label("loc_A150")


    ChrTalk(
        0x10,
        "Nyaon... [I'm tired]\x02",
    )

    CloseMessageWindow()

    label("loc_A16A")

    Jump("loc_A378")

    label("loc_A16F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_A198")

    ChrTalk(
        0x10,
        "Nyao? [What's wrong?]\x02",
    )

    CloseMessageWindow()
    Jump("loc_A378")

    label("loc_A198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A1B7")

    ChrTalk(
        0x10,
        "Fumyaawn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A378")

    label("loc_A1B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A1DE")

    ChrTalk(
        0x10,
        "Nyaa~~ [I'm hungry]\x02",
    )

    CloseMessageWindow()
    Jump("loc_A378")

    label("loc_A1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A1EC")
    Jump("loc_A378")

    label("loc_A1EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A378")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A364")

    ChrTalk(
        0x101,
        (
            "#00005FOh, right, we have to\x01",
            "feed Koppe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Nyao? [What's wrong?]\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A27C")

    ChrTalk(
        0x1A5,
        "#01100FHe says he's full.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2AC")

    label("loc_A27C")


    ChrTalk(
        0x105,
        (
            "#10300FStill, it looks like\x01",
            "he's full now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2AC")


    ChrTalk(
        0x102,
        (
            "#00100FLooks like Chief gave\x01",
            "him food before going\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FOoh, it's a bit of a\x01",
            "pity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well, shall we\x01",
            "bring him a fish the\x01",
            "next time we get one?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13B, 2)
    Jump("loc_A378")

    label("loc_A364")


    ChrTalk(
        0x10,
        "Nyanyayayaa~㈱\x02",
    )

    CloseMessageWindow()

    label("loc_A378")

    Return()

    # Function_21_9D6B end

    def Function_22_A379(): pass

    label("Function_22_A379")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_A387")
    SetScenarioFlags(0x1, 3)

    label("loc_A387")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_A395")
    SetScenarioFlags(0x1, 3)

    label("loc_A395")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_A3A3")
    SetScenarioFlags(0x1, 3)

    label("loc_A3A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_A3B1")
    SetScenarioFlags(0x1, 3)

    label("loc_A3B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_A3BF")
    SetScenarioFlags(0x1, 3)

    label("loc_A3BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_A3CD")
    SetScenarioFlags(0x1, 3)

    label("loc_A3CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_A3DB")
    SetScenarioFlags(0x1, 3)

    label("loc_A3DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_A3E9")
    SetScenarioFlags(0x1, 3)

    label("loc_A3E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_A3F7")
    SetScenarioFlags(0x1, 3)

    label("loc_A3F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_A405")
    SetScenarioFlags(0x1, 3)

    label("loc_A405")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_A413")
    SetScenarioFlags(0x1, 3)

    label("loc_A413")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_A421")
    SetScenarioFlags(0x1, 3)

    label("loc_A421")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_A42F")
    SetScenarioFlags(0x1, 3)

    label("loc_A42F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_A43D")
    SetScenarioFlags(0x1, 3)

    label("loc_A43D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_A44B")
    SetScenarioFlags(0x1, 3)

    label("loc_A44B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_A459")
    SetScenarioFlags(0x1, 3)

    label("loc_A459")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_A467")
    SetScenarioFlags(0x1, 3)

    label("loc_A467")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_A475")
    SetScenarioFlags(0x1, 3)

    label("loc_A475")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_A483")
    SetScenarioFlags(0x1, 3)

    label("loc_A483")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_A491")
    SetScenarioFlags(0x1, 3)

    label("loc_A491")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_A49F")
    SetScenarioFlags(0x1, 3)

    label("loc_A49F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_A4AD")
    SetScenarioFlags(0x1, 3)

    label("loc_A4AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_A4BB")
    SetScenarioFlags(0x1, 3)

    label("loc_A4BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_A4C9")
    SetScenarioFlags(0x1, 3)

    label("loc_A4C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_END)), "loc_A4D7")
    SetScenarioFlags(0x1, 3)

    label("loc_A4D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_END)), "loc_A4E5")
    SetScenarioFlags(0x1, 3)

    label("loc_A4E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_END)), "loc_A4F3")
    SetScenarioFlags(0x1, 3)

    label("loc_A4F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_END)), "loc_A501")
    SetScenarioFlags(0x1, 3)

    label("loc_A501")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_END)), "loc_A50F")
    SetScenarioFlags(0x1, 3)

    label("loc_A50F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_END)), "loc_A51D")
    SetScenarioFlags(0x1, 3)

    label("loc_A51D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_END)), "loc_A52B")
    SetScenarioFlags(0x1, 3)

    label("loc_A52B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_A539")
    SetScenarioFlags(0x1, 3)

    label("loc_A539")

    Return()

    # Function_22_A379 end

    def Function_23_A53A(): pass

    label("Function_23_A53A")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    SetChrPos(0x101, -25020, 1300, -19860, 90)
    SetChrPos(0x102, -25130, 1300, -18930, 90)
    SetChrPos(0x109, -26200, 1300, -19870, 90)
    SetChrPos(0x105, -26790, 1300, -19180, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A5B5")
    SetChrPos(0x1A5, -24820, 1300, -16830, 133)

    label("loc_A5B5")

    OP_68(-24880, 3000, -20830, 0)
    MoveCamera(43, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10510, 0)
    OP_0D()

    ChrTalk(
        0x11,
        "#01200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FZeit and Koppe. So\x01",
            "you're together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, they always\x01",
            "get along so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHe's the police dog you're\x01",
            "looking after at the Special\x01",
            "Support Section, right?\x02\x03",
            "#10300FNice to meet you again,\x01",
            "Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01203FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A84C")

    ChrTalk(
        0x1A5,
        (
            "#01104FLooking after is not the\x01",
            "right word. It is I who's\x01",
            "looking after them", he says.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#6P#10309FAhaha. A slip of the\x01",
            "tongue, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FW-Well... He is always\x01",
            "helping us, though. He's\x01",
            "always so proud...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8CF")

    label("loc_A84C")


    ChrTalk(
        0x101,
        (
            "#00005FIt looks like he wants\x01",
            "to say something else,\x01",
            "though...\x02\x03",
            "#00003FHmm, if Tio or KeA were\x01",
            "here, we could\x01",
            "understand him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8CF")

    TurnDirection(0x109, 0x10, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10102FI'm not good with dogs,\x01",
            "but I got used to Zeit.\x02\x03",
            "#10105FAnd this black cat is?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, he's Koppe.\x02\x03",
            "He's been living here ever\x01",
            "since Crossbell News Service\x01",
            "was in this building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11PNyaago. [It's been a\x01",
            "while. How have you\x01",
            "been?]\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FHaha, how cute.\x02\x03",
            "#10109FAah, does this mean I\x01",
            "get to pet him from now\x01",
            "on!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FDo you like cats, Noｱl?\x01",
            "Haha, please feel free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PFumyaawn...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24690, 1300, -19050, 90)
    SetScenarioFlags(0x139, 7)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0xB4, 0x0)
    OP_4C(0x11, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_23_A53A end

    def Function_24_AAB4(): pass

    label("Function_24_AAB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AAEB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AAEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAEB")
    Call(1, 26)
    Return()

    label("loc_AAEB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "       The Crossbell Bell\x01",
            "A giant bell excavated in Crossbell State in S1185. From\x01",
            "the condition of the unearthed remains, it is thought to\x01",
            "date back to the middle ages. Made of multiple metals,\x01",
            "when hit, it rings in a pleasant low tone.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thought to have been built by\x01",
            "influential person of those times, for\x01",
            "what it was used is still debated.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_AAB4 end

    def Function_25_AC80(): pass

    label("Function_25_AC80")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1A5")

    ChrTalk(
        0x1A2,
        (
            "Gironde Weapons... I\x01",
            "see, it's a lawful\x01",
            "weapons store, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Alright, let's drop in\x01",
            "for a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_AD53")

    def lambda_AD23():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD23)
    Sleep(50)

    def lambda_AD33():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD33)
    Sleep(50)

    def lambda_AD43():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AD43)
    Sleep(300)
    Jump("loc_ADCA")

    label("loc_AD53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_AD91")

    def lambda_AD61():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD61)
    Sleep(50)

    def lambda_AD71():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD71)
    Sleep(50)

    def lambda_AD81():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AD81)
    Sleep(300)
    Jump("loc_ADCA")

    label("loc_AD91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_ADCA")

    def lambda_AD9F():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD9F)
    Sleep(50)

    def lambda_ADAF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADAF)
    Sleep(50)

    def lambda_ADBF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ADBF)
    Sleep(300)

    label("loc_ADCA")


    ChrTalk(
        0x101,
        (
            "#00003FSorry, Shing. Like you\x01",
            "said, this is a weapons\x01",
            "store.\x02\x03",
            "#00001FDangerous goods are\x01",
            "inside, so we can't take\x01",
            "you in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmph. It'll be fine as\x01",
            "long as I keep my hands\x01",
            "off them, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I'm interested into this\x01",
            "place. If I say we're\x01",
            "going in, then we are.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F(*sigh*... Elie, if you\x01",
            "please.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00100F(Haha, got it.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00103FListen, Shing, you're\x01",
            "someone very, very precious\x01",
            "who was left in our care.\x02\x03",
            "That's why we must\x01",
            "eliminate even the most\x01",
            "remote possible dangers.\x02\x03",
            "#00100FYou're a smart boy, Shing.\x01",
            "You understand the\x01",
            "situation, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Ugh... That does make\x01",
            "sense, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*. I knew you'd\x01",
            "understand. You're such\x01",
            "a clever boy, Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Y-Yes... I am!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_B0FF")

    ChrTalk(
        0x104,
        (
            "#00309F(Haha. Milady made quite\x01",
            "an impact on him.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B19D")

    label("loc_B0FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B152")

    ChrTalk(
        0x109,
        (
            "#10109F(Ahaha. Milady made\x01",
            "quite an impact on him,\x01",
            "didn't she.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B19D")

    label("loc_B152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B19D")

    ChrTalk(
        0x105,
        (
            "#10302F(Haha. Elie made quite\x01",
            "an impact on him, didn't\x01",
            "she.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B19D")

    SetScenarioFlags(0x1DC, 7)
    Jump("loc_B1F1")

    label("loc_B1A5")


    ChrTalk(
        0x101,
        (
            "#00000FShing is with us. Let's\x01",
            "refrain from entering\x01",
            "the weapons shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1F1")

    TalkEnd(0xFF)
    Return()

    # Function_25_AC80 end

    def Function_26_B1F5(): pass

    label("Function_26_B1F5")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x14, 0x0)
    OP_4B(0x15, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 150, 0, -3900, 0)
    SetChrPos(0x109, 1330, 0, -4640, 0)
    SetChrPos(0x102, 2590, 0, -3300, 315)
    SetChrPos(0x103, -1610, 0, -4590, 0)
    SetChrPos(0x105, -900, 0, -5970, 0)
    SetChrPos(0x104, 740, 0, -6130, 0)
    OP_68(-1190, 1900, -5280, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(11710, 0)
    SetChrFlags(0xF, 0x8)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_B544")

    ChrTalk(
        0x14,
        "Hi, Lloyd and friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Everyone from the Special\x01",
            "Support Section, Sergeant\x01",
            "Major Noｱl, good morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FGood morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "By the way, did you\x01",
            "settle that job?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B40A")

    ChrTalk(
        0x101,
        (
            "#00002F#2PYeah, we just finished.\x01",
            "Thanks to you, Frantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Haha. I don't really get\x01",
            "it, but it's an honor to\x01",
            "have been of help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4D5")

    label("loc_B40A")


    ChrTalk(
        0x101,
        (
            "#00003F#2PY-Yeah... We just\x01",
            "finished.\x02\x03",
            "#00006F(Because we ignored what\x01",
            "he told us, the swindler\x01",
            "ended up slipping away...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Haha, I don't really get\x01",
            "it, but I'm glad things\x01",
            "are settled for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4D5")


    ChrTalk(
        0x101,
        (
            "#00005F#2PBy the way, Frantz, are\x01",
            "you stationed here\x01",
            "today?\x02\x03",
            "Officer Kate usually\x01",
            "patrols this area.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B638")

    label("loc_B544")


    ChrTalk(
        0x14,
        (
            "Hey, if it isn't Lloyd\x01",
            "and friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Everyone from the Special\x01",
            "Support Section, Sergeant\x01",
            "Major Noｱl, good morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FGood morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#2PFrantz, are you\x01",
            "stationed here today?\x02\x03",
            "Officer Kate usually\x01",
            "patrols this area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B638")


    ChrTalk(
        0x14,
        (
            "Yes, Officer Kate went\x01",
            "somewhere else for a\x01",
            "different case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It was decided that I'll\x01",
            "patrol this area\x01",
            "temporarily.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-2320, 2800, -900, 2000)
    MoveCamera(45, 8, 0, 2000)
    OP_6E(660, 2000)
    SetCameraDistance(15930, 2000)
    Sleep(2500)

    ChrTalk(
        0x102,
        (
            "#12P#00108FThe Crossbell Bell...\x01",
            "It's been stolen by Red\x01",
            "Constellation...\x02\x03",
            "#00101FIncreasing security here\x01",
            "is related to that,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "A major cultural asset\x01",
            "of Crossbell was stolen,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We CGF have come for\x01",
            "support, just in case.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1190, 1900, -5280, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(660, 2000)
    SetCameraDistance(11710, 2000)
    Sleep(2500)

    ChrTalk(
        0x103,
        (
            "#00206F#3PYou know neither why it\x01",
            "was stolen nor where it\x01",
            "was taken, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Yeah. The police and CGF\x01",
            "are looking for it, but\x01",
            "it hasn't been found yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#4PUncle and the others...\x01",
            "Why on earth did they do\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#4PHehe. It's a bit of an\x01",
            "unwieldy thing to be\x01",
            "carrying around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#2P...Anyway, we leave the\x01",
            "bell to you. We'll focus\x01",
            "on our own work.\x02\x03",
            "#00000FLater then, Frantz. Do\x01",
            "your best with guarding\x01",
            "the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Yeah, see you later.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x14, 0x0)
    OP_4C(0x15, 0x0)
    ClearChrFlags(0xF, 0x8)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 150, 0, -3900, 0)
    SetScenarioFlags(0x190, 4)
    EventEnd(0x5)
    Return()

    # Function_26_B1F5 end

    SaveToFile()

Try(main)
