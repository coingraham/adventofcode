

def get_repeating_letters(id):
    has_two = False
    has_three = False

    letter_list = list(id)
    seen_letters = []

    for letter in letter_list:
        if letter in seen_letters:
            continue
        if letter_list.count(letter) == 2:
            has_two = True
        elif letter_list.count(letter) == 3:
            has_three = True
        seen_letters.append(letter)

    return [has_two, has_three]


def part_one(string_list):
    two_letter_total = 0
    three_letter_total = 0

    for my_id in string_list:
        has_two, has_three = get_repeating_letters(my_id)
        two_letter_total += has_two
        three_letter_total += has_three

    return "Checksum: {}".format(two_letter_total * three_letter_total)


def part_two(first_string_list, second_string_list):

    for first_item in first_string_list:
        for second_item in second_string_list:
            if first_item == second_item:
                continue

            count = 0

            for x, y in zip(first_item, second_item):
                if x != y:
                    count += 1

            if count == 1:
                for i, letter in enumerate(first_item):
                    if second_item[i] != letter:
                        print(second_item[:i] + second_item[i+1:])

                # print("One off: {} {}".format(first_item, second_item))


if __name__ == '__main__':
    test_string_list = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

    actual_string_list = ["tjxmoewpqkyaiqvmndgflunszc", "tjxmobwpqkyaihvrndgfjubszm", "tjxmzewpqkyaihvrydgflrbszc", "tjxmoeypqkyvihvrndgflubsza", "tjcmoewpqkytihvrndgflgbszc", "tjvmoewpqkyanevrndgflubszc", "tjxmoewpqkdiihirndgflubszc", "tjxboewpqkyaihbrnogflubszc", "ojpmoewpqkyaihvjndgflubszc", "tjxyoewpqkyaiuvrndgflutszc", "tjxmoewpqkyalhvrndmflebszc", "tjxmoewpqzyaihhrndgflubszf", "tjxmrewpqkyaihirndgfjubszc", "pjxmoewpqkyaihvendgfbubszc", "txxmkewpqkyjihvrndgflubszc", "tjxmoewcqkyaihvrnmgflubczc", "tjxmoewkqkyaghvrndgfluvszc", "tjxmoewfqkhaihvrndgflubhzc", "jjqmoewpqkyaihvrndzflubszc", "tjxmoewmqksaihvcndgflubszc", "tjrmoewpqkyaihvrvdgflubzzc", "tjxxoewpqkyaiiwrndgflubszc", "cjxmoawxqkyaihvrndgflubszc", "tjxdoewpvkyaihvrndgflubsoc", "tjxmsewpqkyaihvrndgfluzozc", "tjxmoewpqkyafhvrnyeflubszc", "tjxmlewpqkyawhvondgflubszc", "tjxmonwpqkyaiqvrnxgflubszc", "tjxmoewcqkyaihvrnjgflumszc", "tjvmoewpqkyaihveadgflubszc", "tjxmogfpqkyaigvrndgflubszc", "tybmoewpqkyaihvrndgllubszc", "tjxmoewpdkyaihvrndgfluwbzc", "etxmbewpqkyaihvrndgflubszc", "tjxmoeapqcynihvrndgflubszc", "tbxmoewpqkyaihvrndgfdebszc", "haxmoewpqyyaihvrndgflubszc", "ojxmoewpqkyaihvrnegflubszr", "tjxmoewpqkyaihvrndoflubarc", "ljxmoewpqkykihvrndgflvbszc", "tjxmovwpqkyaihvrndgfluzsyc", "tvxmoewpqkyanhvrkdgflubszc", "tjxmoewpqkyaihkrndgfluwwzc", "zjxmoewpfkyaihvrndgfrubszc", "tjxyoegpqkyaihvrndlflubszc", "tjxmoewpqkyamhvrnsgflubmzc", "tjmmoewpqkyaihvrndgftuwszc", "tjxmoewpqbraihvrncgflubszc", "tjxmeeepqkyainvrndgflubszc", "tjemoegpqkyaihvredgflubszc", "tjxmoewpqkyaihvdndgfzubqzc", "tjxmoegrqkyaihfrndgflubszc", "tjxmoewpqxyaihvrndgfluyvzc", "qjxmoewpqkyaiwvrnfgflubszc", "tjxwoewpqkyashkrndgflubszc", "tjzmoewiqkyaihurndgflubszc", "tjumuewpqkyaihvrndgflubssc", "tyxooewpukyaihvrndgflubszc", "tjxvoewpqkyaiivindgflubszc", "ijxmoqwpqkyaihvradgflubszc", "tjxmlewpqkyaihvrhdgflubwzc", "tjxmkewpqkyajhqrndgflubszc", "tjxmoewpqkqaiherndgflurszc", "tjamoewpqkyaizvondgflubszc", "tjxgogwpqkyalhvrndgflubszc", "tjxmoewpqkyachvrndgflubuzq", "tjxmowqpqkyaihvrnegflubszc", "mjxmoewpwkyaihvrndgfkubszc", "tpbmoewpqkyaihvrzdgflubszc", "tjbmoewpqkyaiuvrndgflsbszc", "tjxmoewpqklaghvrndgflubazc", "tjxmoewpqkyrihvrndgwlpbszc", "tjcmoewpqksaiyvrndgflubszc", "tjxmoeapqkymihvindgflubszc", "tjxmdewpqkyafhvrndgflqbszc", "tjxmoewpqxyaihvrndsflubszi", "tjxmoeppqkyaihvrcdgflubszd", "tjxmomwpqkyainvrmdgflubszc", "tjxmovwpqkyaihvrndgfdubdzc", "tjxmoewwqkiaihvrjdgflubszc", "tmxmoewpqkyaifvrndgflubszs", "tbxmoewpqkyaihvrbdgflunszc", "tjxmoewrqkyaihvxndgflubszp", "ujxmoewpqkyaihvxndgflubpzc", "tdxmotwpqkyaihvdndgflubszc", "tjxmvewpqkyaihfrndgtlubszc", "tjfmoewpqkyaihvrnyqflubszc", "tjxfolwzqkyaihvrndgflubszc", "ojrmoiwpqkyaihvrndgflubszc", "tjsmoqwpqkyqihvrndgflubszc", "tjxmohwpqkyaihvrudgflubslc", "tjxtoiwpqkyaihvrnogflubszc", "taxmoewpqkyaiyvrndgfwubszc", "tjxwnezpqkyaihvrndgflubszc", "tjxmyevpqkyaivvrndgflubszc", "tjxdoeopqkyaihvgndgflubszc", "tjxaoewpqkmaihvrndgflufszc", "tjxmoewpqkyaxhvrndgflubncc", "tjxmoewpqkyaihurndgflubbjc", "tjxmjewpqgyaihvrnngflubszc", "tjxmogwpqkyaihvrndgflubbcc", "tjxmoewplkyaihvrnpgflibszc", "tjwmoewpqkyaohvrndgfbubszc", "tjwmoewpqkyaihvrndgfsubszm", "tjxmogwpqkyaihvrndiflubqzc", "tjxmoewpqkyaihvrndgflopshc", "rjxmlewpvkyaihvrndgflubszc", "tjxmogwpakyaihvrndgflzbszc", "tjxmoeppqkyaihvrndgflmxszc", "tjxmoewpqkyhihgrndgfzubszc", "tjxqoewpqkyaihtrndgwlubszc", "tjxnoespqkyaihvrndgflubsuc", "tjmmoewpqkraihvrndgflfbszc", "tjxmoewnqkwaihvrndgflubstc", "tjxmoewpqqyaihvrndgfljbszi", "tjxmoewpqkyaihkrkdgalubszc", "tjxmoewpqkyaihvradgjlurszc", "tvxmoewpqkybihvrndbflubszc", "tjxvoewpqkyaihvradgfoubszc", "tjxmoewpqfyaihvlodgflubszc", "tjxmoewmnkyaiivrndgflubszc", "kjxmoewpqkyaihprndgflcbszc", "hjxmoewpqkcaihvrndgvlubszc", "tjxmoewcqkyaihvrncgfllbszc", "tuxmoewpckyaihvrndoflubszc", "tjxmdewpokyaihvrndgflubszn", "mjxmaewpqkyaqhvrndgflubszc", "tjxmoewpmzyaihvrndgfiubszc", "tjxmoewnqkyvihvrndgflubszk", "tjxmoewpmnyaihvrndgftubszc", "zjxmoewpqkysihvrndgfmubszc", "tjxmoewpqkyaihzrntgflubbzc", "tjxmoewpqkgaihwrndsflubszc", "tjxjoewpqkyaihvrndgflgbizc", "oqxmoewpqkyaihvrndgfldbszc", "wjamoewpqkyaihvfndgflubszc", "tjxmoewtmkyvihvrndgflubszc", "tjlmojwpqkyaihvrndgfludszc", "tjxmowwpqkyaihvrndefludszc", "tjxmoewpqkbaihvrndgfluaszt", "tjxmoewpqkzaahvrodgflubszc", "tjxmoewpqkgaihvrndgflubtpc", "tjxmoenpqkyaihcrndgfqubszc", "tbxmoewpqbyaihvrndgalubszc", "tjvmoewqqkyaihvrndvflubszc", "tjxmoewpqkeaihvundgfaubszc", "txxmoewpqkyaihvrwdgflpbszc", "tzxmoewpqkijihvrndgflubszc", "tjxmoewoqkytiuvrndgflubszc", "tjxmrejplkyaihvrndgflubszc", "tjxmoewpqkynihvrpxgflubszc", "tjxmoewpqkvanhvrndgvlubszc", "tjxmoewpdkyiihvrndgflubszs", "tpxmyewpqkyaihvrndgfeubszc", "tpxmoewpqyyaihvrndhflubszc", "tjsmoewpqkyaihvrndhflubnzc", "tjxmoewpukyaihvrnmgflubwzc", "txxmoewpqlyaihwrndgflubszc", "tjxmoewprkyaiovrndgflubxzc", "tjxmouwpqkyaihzrodgflubszc", "tjxmojwpqkywimvrndgflubszc", "tjxsoewpqkyaihvrzdgqlubszc", "tfxmoewpakyaihvrndgllubszc", "tjhmoewpqiyaihvrndgflubsac", "tjxmoewpqkoaihvrndoflubsxc", "tjxmoewpqkyzpjvrndgflubszc", "tjxmoewpqkyaiharndgzlnbszc", "tjimoevpqkyaihvrndgflubbzc", "tjxsoewpqkyahhvrndgfzubszc", "txxmoewpqkyaimvrrdgflubszc", "tjxmoewpwkyaihvrndpylubszc", "tjxmoewpskyaghvrndgfbubszc", "tjxmuewpqmyaihvrndgfyubszc", "tjxmoewpqkyaihvdndgglubsxc", "xjxmoewpqkyjiovrndgflubszc", "gjxmoewpqkyaihvrndodlubszc", "tjbmoewpqkyaihvridgflvbszc", "tjxmozwpqkyapbvrndgflubszc", "tjxeoewpqkyqihvrndgflubhzc", "tjxdoewpqzyaihvrndgflubsmc", "tjxmwewpqkyathvcndgflubszc", "tjxmoewpszyaihvrndgflusszc", "tuxmoewpqkyaihvrndgfluasxc", "tjemoewpnvyaihvrndgflubszc", "tjxmoewpjkyaihvrndgjlufszc", "tjomoewppkyaihvzndgflubszc", "tjxmvewpqkyaimvrntgflubszc", "rjxmoewpqkyaihvpndgflubszq", "hjxzoewpqkyaihvridgflubszc", "texmoejpqkyaihvrndgflubszx", "tjxcoewpqkyaihbrxdgflubszc", "tjxmoewpnkyaihvrndgfltbsze", "tjxmoewpdkyaihvrndwfluwbzc", "tjxmoewpqryjihkrndgflubszc", "tjlmoewpqkhaihvrndgflubsnc", "tjxmovapqkjaihvrndgflubszc", "tjxvoewpqkyaihqrndgfluyszc", "tjxwoewnqkyaihvrndgfgubszc", "tjdmoewpqklaihvcndgflubszc", "tjxmoewpvkynihvrndgflubskc", "tjxmtewpqkyaihvhndgfluaszc", "tjxmoewpqkyanhvrnpgfluvszc", "tjxmoewpqkyaifvbndgflubspc", "tjxmoexpqknaihvrndgxlubszc", "qjxmoewqqkyaihvrndgflubpzc", "tjxmoewppkyaihvaxdgflubszc", "myxmoewpqkyaihvrudgflubszc", "tjxmwewpmkyaihvrndgflubssc", "tjxmoewpqkyaihvrndgfxqbszq", "tjxmoewhqkyaahvrndgflubbzc", "tbxmoewmqkyaihvrndgflubszu", "toxmolwpqkyaihvrndnflubszc", "tjxmoewhqkyaihvrnrgflubvzc", "yjxmoewcqkyaihvrndgflubfzc", "tjxmoewpqkyamhvrgdgflmbszc", "tjxmtewpqkyaizvrndgfluoszc", "tjxmoewpqzyaihvrntsflubszc", "fjxmoewpqkyaihyrmdgflubszc", "tjxwoewpqcyaihbrndgflubszc", "tjxmoebpqkzaihvrndcflubszc", "tjxmoewpqkyaihvrndnlmubszc", "tjxmoewpqkyaihvrndgeyubskc", "tfxmoewpqryaihvrndgfluiszc", "tjxmoewpqkjaihvynngflubszc", "tjxmoewpqkqaihvonjgflubszc", "tjfmokwpqkyeihvrndgflubszc", "djxmoewpkkyaihvrnmgflubszc", "tjxmiewpqkyaihvrndgflubhlc", "tjxmmejpqkyaihvrnhgflubszc", "djxmoewmqkyaihvrnggflubszc", "tjxmoewpqkyaihvrkggflubsze", "gjxmoewpqkyaihjrndgflvbszc", "tjxmoewpqkyaidvrndgkzubszc", "tjxmoewpqkyaedvrnpgflubszc", "sjxmoewpqkyaihvrnngfluhszc", "tjxmoewpqkuaihvrndghlubxzc", "tjxmoewgqkyuihvrndgftubszc", "tjxmoewpqsyaifvrkdgflubszc", "tjxrrewpqkyaihvrnpgflubszc", "tjxmoezpqkyaihvrwdgflabszc", "tjfmoewpqknaihvrndgflubkzc", "tjxmoewnqkxaihvrndgflubtzc", "tjxmoewpkkyaihvrndgfrnbszc", "tjxmorwpnkqaihvrndgflubszc", "tsxmoewwqkyathvrndgflubszc", "tjxmoeupqkyaihvrndyflubszp", "bjxmoewdqkyaihvrndgflurszc", "tjxmoewpvkyaihvrndoflubszq", "sjxmoewpqkyaihvrndgflubyec", "tjxmoewpqkyaizcrndgfnubszc"]

    troubleshoot_list = ["aabbccdddeeefffgghhii", "bbccddeeggghh", "aabbcc"]
    # print(part_one(actual_string_list))
    print(part_two(actual_string_list, actual_string_list))

    # print(online(actual_string_list))