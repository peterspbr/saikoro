#!/usr/bin/env python

import random, time, os, sys

def show_banner():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠚⠉⢉⣩⠽⠟⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠀⢀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠤⠄⢤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⠋⠉⠀⠀⠀⣀⣤⠴⠒⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢳⡄⢀⡴⠚⠉⠀⠀⠀⠀⠀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠹⡏⠀⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢬⣳⣄⣠⠤⠤⠶⠶⠒⠋⠀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠈⠉⠛⠲⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢳⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⢃⠈⠙⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⢀⢾⠃⠀⠀⠀⠀⠀⠀⠀⠀⢢⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠮⣄⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⠋⠀⠀⢀⡤⡴⠃⠈⠦⣀⠀⠀⠀⠀⠀⠀⢀⣷⢸⠀⠀⠀⠀⢀⣀⠘⡄⠤⠤⢤⠔⠒⠂⠉⠁⠀⠀⠀⠑⢄⡀⠀⠀⠙⢦⡀⠀⠀⠀
⠀⠀⠀⠀⣼⠃⠀⠀⢠⣞⠟⠀⠀⠀⡄⠀⠉⠒⠢⣤⣤⠄⣼⢻⠸⠀⠀⠀⠀⠉⢤⠀⢿⡖⠒⠊⢦⠤⠤⣀⣀⡀⠀⠀⠀⠈⠻⡝⠲⢤⣀⠙⢦⠀⠀
⠀⠀⠀⢰⠃⠀⠀⣴⣿⠎⠀⠀⢀⣜⠤⠄⢲⠎⠉⠀⠀⡼⠸⠘⡄⡇⠀⠀⠀⠀⢸⠀⢸⠘⢆⠀⠘⡄⠀⠀⠀⢢⠉⠉⠀⠒⠒⠽⡄⠀⠈⠙⠮⣷⡀
⠀⠀⠀⡟⠀⠀⣼⢻⠧⠐⠂⠉⡜⠀⠀⡰⡟⠀⠀⠀⡰⠁⡇⠀⡇⡇⠀⠀⠀⠀⢺⠇⠀⣆⡨⢆⠀⢽⠀⠀⠀⠈⡷⡄⠀⠀⠀⠀⠹⡄⠀⠀⠀⠈⠁
⠀⠀⢸⠃⠀⠀⢃⠎⠀⠀⠀⣴⠃⠀⡜⠹⠁⠀⠀⡰⠁⢠⠁⠀⢸⢸⠀⠀⠀⢠⡸⢣⠔⡏⠀⠈⢆⠀⣇⠀⠀⠀⢸⠘⢆⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀
⠀⠀⢸⠀⠀⠀⡜⠀⠀⢀⡜⡞⠀⡜⠈⠏⠀⠈⡹⠑⠒⠼⡀⠀⠀⢿⠀⠀⠀⢀⡇⠀⢇⢁⠀⠀⠈⢆⢰⠀⠀⠀⠈⡄⠈⢢⠀⠀⠀⠈⣇⠀⠀⠀⠀
⠀⠀⢸⡀⠀⢰⠁⠀⢀⢮⠀⠇⡜⠀⠘⠀⠀⢰⠃⠀⠀⡇⠈⠁⠀⢘⡄⠀⠀⢸⠀⠀⣘⣼⠤⠤⠤⣈⡞⡀⠀⠀⠀⡇⠰⡄⢣⡀⠀⠀⢻⠀⠀⠀⠀
⠀⠀⠈⡇⠀⡜⠀⢀⠎⢸⢸⢰⠁⠀⠄⠀⢠⠃⠀⠀⢸⠀⠀⠀⠀⠀⡇⠀⠀⡆⠀⠀⣶⣿⡿⠿⡛⢻⡟⡇⠀⠀⠀⡇⠀⣿⣆⢡⠀⠀⢸⡇⠀⠀⠀
⠀⠀⢠⡏⠀⠉⢢⡎⠀⡇⣿⠊⠀⠀⠀⢠⡏⠀⠀⠀⠎⠀⠀⠀⠀⠀⡇⠀⡸⠀⠀⠀⡇⠀⢰⡆⡇⢸⢠⢹⠀⠀⠀⡇⠀⢹⠈⢧⣣⠀⠘⡇⠀⠀⠀
⠀⠀⢸⡇⠀⠀⠀⡇⠀⡇⢹⠀⠀⠀⢀⡾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢠⠃⠀⠀⠠⠟⡯⣻⣇⢃⠇⢠⠏⡇⠀⢸⡆⠀⢸⠀⠈⢳⡀⠀⡇⠀⠀⠀
⠀⠀⠀⣇⠀⡔⠋⡇⠀⢱⢼⠀⠀⡂⣼⡇⢹⣶⣶⣶⣤⣤⣀⠀⠀⠀⣇⠇⠀⠀⠀⠀⣶⡭⢃⣏⡘⠀⡎⠀⠇⠀⡾⣷⠀⣼⠀⠀⠀⢻⡄⡇⠀⠀⠀
⠀⠀⠀⣹⠜⠋⠉⠓⢄⡏⢸⠀⠀⢳⡏⢸⠹⢀⣉⢭⣻⡽⠿⠛⠓⠀⠋⠀⠀⠀⠀⠀⠘⠛⠛⠓⠀⡄⡇⠀⢸⢰⡇⢸⡄⡟⠀⠀⠀⠀⢳⡇⠀⠀⠀
⠀⣠⠞⠁⠀⠀⠀⠀⠀⢙⠌⡇⠀⣿⠁⠀⡇⡗⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠁⠁⠀⢸⣼⠀⠈⣇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠁⠀⠀⢀⡠⠔⠚⠉⠉⢱⣇⢸⢧⠀⠀⠸⣱⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠦⡔⠀⠀⠀⠀⠀⢀⡼⠀⠀⣼⡏⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⠀⠀⠋⠀⠀⠀⢀⡠⠤⣿⣾⣇⣧⠀⠀⢫⡆⠀⠀⠀⠀⠀⠀⠀⢨⠀⠀⣠⠇⠀⠀⢀⡠⣶⠋⠀⠀⡸⣾⠁⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡄⠀⠀⠀⠀⠠⠊⠁⠀⠀⢸⢃⠘⡜⡵⡀⠈⢿⡱⢲⡤⠤⢀⣀⣀⡀⠉⠉⣀⡠⡴⠚⠉⣸⢸⠀⠀⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢧⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠚⣤⣵⡰⡑⡄⠀⢣⡈⠳⡀⠀⠀⠀⢨⡋⠙⣆⢸⠀⠀⣰⢻⡎⠀⠀⡎⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢷⡀⠀⠀⠀⠀⠀⠁⠀⠀⠀⡸⢌⣳⣵⡈⢦⡀⠳⡀⠈⢦⡀⠀⠘⠏⠲⣌⠙⢒⠴⡧⣸⡇⠀⡸⢸⠇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⠢⡀⠀⠀⠀⠠⠄⡖⠋⠀⠀⠙⢿⣳⡀⠑⢄⠹⣄⡀⠙⢄⡠⠤⠒⠚⡖⡇⠀⠘⣽⡇⢠⠃⢸⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⠃⠀⠀⠀⠀⠀⢀⡼⣄⠀⠀⠀⠀⠀⠑⣽⣆⠀⠑⢝⡍⠒⠬⢧⣀⡠⠊⠀⠸⡀⠀⢹⡇⡎⠀⡿⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡼⠁⠀⠀⠀⠀⠀⠀⢀⠻⣺⣧⠀⠀⠀⠰⢢⠈⢪⡷⡀⠀⠙⡄⠀⠀⠱⡄⠀⠀⠀⢧⠀⢸⡻⠀⢠⡇⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⠇⠀⠀⠀⠀⠀⠀⠀⢸⠀⡏⣿⠀⠀⠀⠀⢣⢇⠀⠑⣄⠀⠀⠸⡄⠀⠀⠘⡄⠀⠀⠸⡀⢸⠁⠀⡾⢰⡏⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
+====================================================+
| Japanese prefectures Saikoro V2.0                  |
| Written by Peter (https://github.com/peterspbr)    |
+====================================================+
""")

def hide_cursor():
    """Hides the terminal cursor."""
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    """Shows the terminal cursor."""
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def animated_selection(items, label, start_speed=0.005, end_speed=0.5, steps=32):
    current_speed = start_speed
    slowdown_factor = (end_speed - start_speed) / steps

    for _ in range(steps):
        selected = random.choice(items)
        sys.stdout.write(f"\r{label}: {selected.ljust(20)}")  # Pad to avoid residual characters
        sys.stdout.flush()
        time.sleep(current_speed)
        current_speed += slowdown_factor

    sys.stdout.write(f"\r{label}: {selected.ljust(20)}\n")
    sys.stdout.flush()
    return selected

def random_location_picker(locations):
    hide_cursor()
    try:
        prefectures = list(locations.keys())
        chosen_prefecture = animated_selection(prefectures, "Selecting Prefecture")

        cities = locations[chosen_prefecture]
        chosen_city = animated_selection(cities, "Selecting City")
    finally:
        show_cursor()

if __name__ == "__main__":
    japanese_locations = {
    "Hokkaido": ["Sapporo", "Hakodate", "Asahikawa", "Otaru", "Tomakomai", "Obihiro", "Muroran"],
    "Aomori": ["Aomori", "Hirosaki", "Hachinohe", "Kamaishi", "Towada", "Mutsu", "Goshogawara"],
    "Iwate": ["Morioka", "Hanamaki", "Kamaishi", "Ichinoseki", "Oshu", "Rikuzentakata", "Tono"],
    "Miyagi": ["Sendai", "Ishinomaki", "Shiogama", "Kurihara", "Natori", "Kesennuma", "Zao"],
    "Akita": ["Akita", "Oga", "Yokote", "Noshiro", "Daisen", "Kakita", "Kazuno"],
    "Yamagata": ["Yamagata", "Tsuruoka", "Sakata", "Shinjo", "Tendo", "Nishikawa", "Kaminoyama"],
    "Fukushima": ["Fukushima", "Koriyama", "Iwaki", "Aizu-Wakamatsu", "Soma", "Kitakata", "Shirakawa"],
    "Ibaraki": ["Mito", "Tsukuba", "Hitachi", "Tsuchiura", "Tama", "Kashima", "Takahagi"],
    "Tochigi": ["Utsunomiya", "Ashikaga", "Kanuma", "Sano", "Nikko", "Shimoza", "Tama"],
    "Gunma": ["Maebashi", "Takasaki", "Isesaki", "Ota", "Kiryu", "Tsumari", "Shibukawa"],
    "Saitama": ["Saitama", "Kawaguchi", "Koshigaya", "Urawa", "Kawagoe", "Sayama", "Kuki"],
    "Chiba": ["Chiba", "Narita", "Funabashi", "Kashiwa", "Matsudo", "Sakura", "Ichikawa"],
    "Tokyo": ["Shinjuku", "Shibuya", "Chiyoda", "Setagaya", "Toshima", "Bunkyo", "Meguro"],
    "Kanagawa": ["Yokohama", "Kawasaki", "Sagamihara", "Yokosuka", "Fujisawa", "Kamakura", "Odawara"],
    "Niigata": ["Niigata", "Nagaoka", "Sanjo", "Sado", "Jyoetsu", "Tsubame", "Kamo"],
    "Toyama": ["Toyama", "Takaoka", "Unazuki", "Himi", "Imizu", "Nanto", "Kamiichi"],
    "Ishikawa": ["Kanazawa", "Komatsu", "Suematsu", "Wajima", "Nomi", "Shika", "Kaga"],
    "Fukui": ["Fukui", "Sakai", "Echizen", "Tsuruga", "Awano", "Ono", "Yokokawa"],
    "Yamanashi": ["Kofu", "Fujiyoshida", "Furuta", "Tama", "Minami-Alps", "Nirasaki", "Kiyosato"],
    "Nagano": ["Nagano", "Matsumoto", "Suwa", "Ueda", "Saku", "Komoro", "Chino"],
    "Gifu": ["Gifu", "Ogaki", "Seki", "Tajimi", "Inazawa", "Kakamigahara", "Ichinomiya"],
    "Shizuoka": ["Shizuoka", "Hamamatsu", "Numazu", "Fujieda", "Kakegawa", "Shimizu", "Yaizu"],
    "Aichi": ["Nagoya", "Toyota", "Ichinomiya", "Kasugai", "Aichi", "Seto", "Kariya"],
    "Mie": ["Tsu", "Yokkaichi", "Ise", "Shima", "Suzuka", "Kuwana", "Kameyama"],
    "Shiga": ["Otsu", "Kusatsu", "Koka", "Hikone", "Nagahama", "Omihachiman", "Takashima"],
    "Kyoto": ["Kyoto", "Uji", "Kameoka", "Maizuru", "Fukuchiyama", "Joyo", "Kyotanabe"],
    "Osaka": ["Osaka", "Sakai", "Higashiosaka", "Takatsuki", "Yao", "Minoh", "Ibaraki"],
    "Hyogo": ["Kobe", "Himeji", "Amagasaki", "Akashi", "Takarazuka", "Sanda", "Nishinomiya"],
    "Nara": ["Nara", "Yamatokoriyama", "Tenri", "Saho", "Kashihara", "Gose", "Uda"],
    "Wakayama": ["Wakayama", "Shingū", "Kainan", "Kumano", "Gobo", "Arida", "Hashimoto"],
    "Tottori": ["Tottori", "Yonago", "Kurayoshi", "Sakaiminato", "Chizu", "Kozaki", "Hokuei"],
    "Shimane": ["Matsue", "Izumo", "Hamada", "Oda", "Masuda", "Unnan", "Nima"],
    "Okayama": ["Okayama", "Kurashiki", "Bizen", "Sanyo-Onoda", "Saijo", "Tamano", "Setouchi"],
    "Hiroshima": ["Hiroshima", "Kure", "Fukuyama", "Miyoshi", "Onomichi", "Takehara", "Aki"],
    "Yamaguchi": ["Yamaguchi", "Ube", "Shimonoseki", "Hofu", "Iwakuni", "Suo-Oshima", "Mine"],
    "Tokushima": ["Tokushima", "Awa", "Komatsushima", "Mima", "Naruto", "Kochi", "Iyo"],
    "Kagawa": ["Takamatsu", "Marugame", "Sakaide", "Zentsuji", "Kanonji", "Shodoshima", "Tama"],
    "Ehime": ["Matsuyama", "Imabari", "Niihama", "Uwajima", "Saijo", "Yawatahama", "Takamatsu"],
    "Kochi": ["Kochi", "Nankoku", "Okinawa", "Niyodogawa", "Susaki", "Konan", "Ino"],
    "Fukuoka": ["Fukuoka", "Kitakyushu", "Kurume", "Omuta", "Iizuka", "Futsukaichi", "Dazaifu"],
    "Saga": ["Saga", "Karatsu", "Takeo", "Imari", "Kashima", "Tosu", "Fukutsu"],
    "Nagasaki": ["Nagasaki", "Sasebo", "Isahaya", "Omura", "Huis Ten Bosch", "Goto", "Shimabara"],
    "Kumamoto": ["Kumamoto", "Yatsushiro", "Amakusa", "Hitoyoshi", "Tamana", "Higo", "Mifune"],
    "Oita": ["Oita", "Beppu", "Nakatsu", "Usa", "Hiji", "Saiki", "Yufu"],
    "Miyazaki": ["Miyazaki", "Nobeoka", "Kunitomi", "Hyuga", "Kobayashi", "Saito", "Takanabe"],
    "Kagoshima": ["Kagoshima", "Kirishima", "Amami", "Ibusuki", "Kanoya", "Makurazaki", "Izumi"],
    "Okinawa": ["Naha", "Okinawa City", "Urasoe", "Ishigaki", "Nago", "Uruma", "Ginowan"]
}
    show_banner()
    random_location_picker(japanese_locations)

