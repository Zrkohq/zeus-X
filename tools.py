import os
import sys
import time
import math
import shutil
import threading
import webbrowser
import urllib.request
import re

try:
    from pystyle import Colors, Colorate
except ImportError:
    print("Erreur: pystyle n'est pas installé.")
    print("Installe-le avec: pip install pystyle")
    sys.exit(1)


# ============================================================
# CONFIGURATION
# ============================================================

CURRENT_VERSION = "1.0.0"

GITHUB_OWNER = "Zrkohq"
GITHUB_REPO = "zeus-X"
GITHUB_BRANCH = "main"

GITHUB_REPO_URL = "https://github.com/Zrkohq/zeus-X"


VERSION_CHECK_URL = (
    "https://raw.githubusercontent.com/"
    f"{GITHUB_OWNER}/{GITHUB_REPO}/"
    f"refs/heads/{GITHUB_BRANCH}/version.txt"
)

VERSION_CHECK_URL_FALLBACK = (
    "https://cdn.jsdelivr.net/gh/"
    f"{GITHUB_OWNER}/{GITHUB_REPO}@{GITHUB_BRANCH}/version.txt"
)

VERSION_CHECK_API_URL = (
    "https://api.github.com/repos/"
    f"{GITHUB_OWNER}/{GITHUB_REPO}/contents/version.txt"
    f"?ref={GITHUB_BRANCH}"
)

UPDATE_AVAILABLE = None
UPDATE_DECLINED = False



# ============================================================
# ASCII
# ============================================================

INTRO_ASCII = [
    " ███████████                    █████              ",
    "▒█▒▒▒▒▒▒███                    ▒▒███               ",
    "▒     ███▒    ██████  ████████  ▒███ █████  ██████ ",
    "     ███     ███▒▒███▒▒███▒▒███ ▒███▒▒███  ███▒▒███",
    "    ███     ▒███████  ▒███ ▒▒▒  ▒██████▒  ▒███ ▒███",
    "  ████     █▒███▒▒▒   ▒███      ▒███▒▒███ ▒███ ▒███",
    " ███████████▒▒██████  █████     ████ █████▒▒██████ ",
    "▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒     ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒  et bobby",
]

INTERFACE_ASCII = [
    "███████╗███████╗██╗   ██╗███████╗     ██╗  ██╗",
    "╚══███╔╝██╔════╝██║   ██║██╔════╝     ╚██╗██╔╝",
    "  ██╔╝ █████╗  ██║   ██║███████╗█████╗╚███╔╝ ",
    " ███╔╝  ██╔══╝  ██║   ██║╚════██║╚════╝██╔██╗ ",
    "███████╗███████╗╚██████╔╝███████║     ██╔╝ ██╗",
    "╚══════╝╚══════╝ ╚═════╝ ╚══════╝     ╚═╝  ╚═╝",
]


# ============================================================
# PAGES
# ============================================================

PAGES = [
    {
        "label": "SEARCHERS",
        "hint": "Recherche de personnes",
        "tools": [
            ("1", "BrixHub", "https://brixhub.to"),
            ("2", "MultiSearch", "https://multisearch.li"),
            ("3", "SeekNow", "https://see-know.ru/"),
            ("4", "OSINT Industries", "https://osint.industries"),
            ("5", "Epieos", "https://epieos.com/"),
            ("6", "Fingerprint", "https://fingerprint.to"),
            ("7", "IntelX", "https://intelx.io/"),
            ("8", "Snusbase", "https://snusbase.com/"),
            ("9", "LeakCheck", "https://leakcheck.io/"),
            ("10", "DeHashed", "https://dehashed.com/"),
        ],
    },
    {
        "label": "SEARCHERS II",
        "hint": "Autres searchers",
        "tools": [
            ("1", "Revealer", "https://revealer.us/"),
            ("2", "OSINTsearch", "https://osintsearch.org/"),
            ("3", "Leak-Lookup", "https://leak-lookup.com/"),
            ("4", "IntelX Tools", "https://intelx.io/tools"),
            ("5", "Phonebook.cz", "https://phonebook.cz/"),
            ("6", "Hunter.io", "https://hunter.io/"),
            ("7", "EmailRep", "https://emailrep.io/"),
            ("8", "VoilaNorbert", "https://www.voilanorbert.com/"),
            ("9", "Clearbit", "https://www.clearbit.com/"),
            ("10", "FullContact", "https://www.fullcontact.com/"),
        ],
    },
    {
        "label": "OSINT",
        "hint": "Outils d'enquête",
        "tools": [
            ("1", "OSINT Framework", "https://osintframework.com/"),
            ("2", "Bellingcat Toolkit", "https://bellingcat.gitbook.io/toolkit"),
            ("3", "IntelTechniques", "https://inteltechniques.com/tools/"),
            ("4", "WhatsMyName", "https://whatsmyname.app/"),
            ("5", "Sherlock", "https://github.com/sherlock-project/sherlock"),
            ("6", "Maigret", "https://github.com/soxoj/maigret"),
            ("7", "Blackbird", "https://github.com/p1ngul1n0/blackbird"),
            ("8", "PhoneInfoga", "https://github.com/sundowndev/phoneinfoga"),
            ("9", "theHarvester", "https://github.com/laramies/theHarvester"),
            ("10", "SpiderFoot", "https://github.com/smicallef/spiderfoot"),
        ],
    },
    {
        "label": "SOCIAL",
        "hint": "Réseaux & usernames",
        "tools": [
            ("1", "Namechk", "https://namechk.com/"),
            ("2", "Instant Username", "https://instantusername.com/"),
            ("3", "UserSearch", "https://usersearch.org/"),
            ("4", "KnowEm", "https://knowem.com/"),
            ("5", "Social Searcher", "https://www.social-searcher.com/"),
            ("6", "IDCrawl", "https://www.idcrawl.com/"),
            ("7", "Picuki", "https://www.picuki.com/"),
            ("8", "Dumpor", "https://dumpor.io/"),
            ("9", "Nitter", "https://nitter.net/"),
            ("10", "Wayback Machine", "https://web.archive.org/"),
        ],
    },
    {
        "label": "RECON",
        "hint": "Domaines & sites",
        "tools": [
            ("1", "SecurityTrails", "https://securitytrails.com/"),
            ("2", "crt.sh", "https://crt.sh/"),
            ("3", "DNSdumpster", "https://dnsdumpster.com/"),
            ("4", "ViewDNS", "https://viewdns.info/"),
            ("5", "Whois.com", "https://www.whois.com/whois/"),
            ("6", "DomainTools", "https://whois.domaintools.com/"),
            ("7", "BuiltWith", "https://builtwith.com/"),
            ("8", "Wappalyzer", "https://www.wappalyzer.com/"),
            ("9", "Netcraft", "https://www.netcraft.com/"),
            ("10", "urlscan", "https://urlscan.io/"),
        ],
    },
    {
        "label": "RÉSEAU",
        "hint": "IP & scanners",
        "tools": [
            ("1", "Shodan", "https://www.shodan.io/"),
            ("2", "Censys", "https://search.censys.io/"),
            ("3", "FOFA", "https://en.fofa.info/"),
            ("4", "ZoomEye", "https://www.zoomeye.org/"),
            ("5", "LeakIX", "https://leakix.net/"),
            ("6", "IPinfo", "https://ipinfo.io/"),
            ("7", "AbuseIPDB", "https://www.abuseipdb.com/"),
            ("8", "VirusTotal", "https://www.virustotal.com/"),
            ("9", "GreyNoise", "https://viz.greynoise.io/"),
            ("10", "BGPView", "https://bgpview.io/"),
        ],
    },
    {
        "label": "PERSONNES",
        "hint": "Annuaires publics",
        "tools": [
            ("1", "TruePeopleSearch", "https://www.truepeoplesearch.com/"),
            ("2", "FastPeopleSearch", "https://www.fastpeoplesearch.com/"),
            ("3", "Spokeo", "https://www.spokeo.com/"),
            ("4", "Whitepages", "https://www.whitepages.com/"),
            ("5", "BeenVerified", "https://www.beenverified.com/"),
            ("6", "ThatsThem", "https://thatsthem.com/"),
            ("7", "FamilySearch", "https://www.familysearch.org/"),
            ("8", "OpenStreetMap", "https://www.openstreetmap.org/"),
            ("9", "Google Maps", "https://www.google.com/maps"),
            ("10", "Wikimapia", "https://wikimapia.org/"),
        ],
    },
    {
        "label": "IMAGES",
        "hint": "Photo & reverse image",
        "tools": [
            ("1", "Google Images", "https://images.google.com/"),
            ("2", "Yandex Images", "https://yandex.com/images/"),
            ("3", "TinEye", "https://tineye.com/"),
            ("4", "Bing Visual Search", "https://www.bing.com/visualsearch"),
            ("5", "PimEyes", "https://pimeyes.com/"),
            ("6", "FaceCheck ID", "https://facecheck.id/"),
            ("7", "ExifTool Online", "https://exiftool.org/"),
            ("8", "FotoForensics", "https://fotoforensics.com/"),
            ("9", "ImgOps", "https://imgops.com/"),
            (
                "10",
                "InVID Verification",
                "https://www.invid-project.eu/tools-and-services/invid-verification-plugin/",
            ),
        ],
    },
    {
        "label": "OUTILS",
        "hint": "Utilitaires",
        "tools": [
            ("1", "CyberChef", "https://gchq.github.io/CyberChef/"),
            ("2", "Regex101", "https://regex101.com/"),
            ("3", "Base64 Decode", "https://www.base64decode.org/"),
            ("4", "JWT.io", "https://jwt.io/"),
            ("5", "Hash Identifier", "https://hashes.com/en/tools/hash_identifier"),
            ("6", "MXToolbox", "https://mxtoolbox.com/"),
            ("7", "DNSChecker", "https://dnschecker.org/"),
            ("8", "SimilarWeb", "https://www.similarweb.com/"),
            ("9", "Archive.today", "https://archive.ph/"),
            ("10", "Pastebin", "https://pastebin.com/"),
        ],
    },
]


# ============================================================
# COULEURS
# ============================================================

PURPLE = "\033[38;2;130;60;210m"
SOFT_PURPLE = "\033[38;2;110;80;180m"
WHITE = "\033[38;2;248;248;248m"
MUTED = "\033[38;2;168;168;175m"
GRAY = "\033[38;2;120;120;130m"
DARK = "\033[38;2;72;72;82m"
DIM = "\033[38;2;46;46;56m"
LINE = "\033[38;2;40;40;52m"
RED = "\033[38;2;255;55;55m"
RESET = "\033[0m"
OPT = "\033[38;2;0;0;237m"
OPT_SOFT = "\033[38;2;40;40;245m"

IS_WINDOWS = os.name == "nt"


# ============================================================
# WINDOWS
# ============================================================

if IS_WINDOWS:
    import ctypes

    STD_INPUT_HANDLE = -10
    ENABLE_MOUSE_INPUT = 0x0010
    ENABLE_EXTENDED_FLAGS = 0x0080
    ENABLE_QUICK_EDIT_MODE = 0x0040
    MOUSE_EVENT = 0x0002
    KEY_EVENT = 0x0001
    FROM_LEFT_1ST_BUTTON_PRESSED = 0x0001
    VK_ESCAPE = 0x1B

    class COORD(ctypes.Structure):
        _fields_ = [
            ("X", ctypes.c_short),
            ("Y", ctypes.c_short),
        ]

    class MOUSE_EVENT_RECORD(ctypes.Structure):
        _fields_ = [
            ("dwMousePosition", COORD),
            ("dwButtonState", ctypes.c_ulong),
            ("dwControlKeyState", ctypes.c_ulong),
            ("dwEventFlags", ctypes.c_ulong),
        ]

    class KEY_EVENT_RECORD(ctypes.Structure):
        _fields_ = [
            ("bKeyDown", ctypes.c_int),
            ("wRepeatCount", ctypes.c_ushort),
            ("wVirtualKeyCode", ctypes.c_ushort),
            ("wVirtualScanCode", ctypes.c_ushort),
            ("uChar", ctypes.c_wchar),
            ("dwControlKeyState", ctypes.c_ulong),
        ]

    class INPUT_RECORD_UNION(ctypes.Union):
        _fields_ = [
            ("KeyEvent", KEY_EVENT_RECORD),
            ("MouseEvent", MOUSE_EVENT_RECORD),
        ]

    class INPUT_RECORD(ctypes.Structure):
        _anonymous_ = ("Event",)
        _fields_ = [
            ("EventType", ctypes.c_ushort),
            ("Event", INPUT_RECORD_UNION),
        ]

    kernel32 = ctypes.windll.kernel32

    console_handle = kernel32.GetStdHandle(
        STD_INPUT_HANDLE
    )

    original_console_mode = ctypes.c_ulong()


_CTRL_HANDLER_REF = None
_thanks_lock = threading.Lock()
_thanks_shown = False


# ============================================================
# SORTIE
# ============================================================

def show_thanks():
    global _thanks_shown

    with _thanks_lock:
        if _thanks_shown:
            return

        _thanks_shown = True

    if not IS_WINDOWS:
        return

    try:
        ps = (
            "Add-Type -AssemblyName System.Windows.Forms; "
            "Add-Type -AssemblyName System.Drawing; "
            "$n = New-Object System.Windows.Forms.NotifyIcon; "
            "$n.Icon = [System.Drawing.SystemIcons]::Information; "
            "$n.BalloonTipTitle = 'ZEUS-X'; "
            "$n.BalloonTipText = 'Merci d''avoir utilisé ZEUS-X !'; "
            "$n.Visible = $true; "
            "$n.ShowBalloonTip(4000); "
            "Start-Sleep -Milliseconds 4200; "
            "$n.Dispose()"
        )

        import subprocess

        subprocess.Popen(
            [
                "powershell",
                "-NoProfile",
                "-WindowStyle",
                "Hidden",
                "-Command",
                ps,
            ],
            creationflags=0x08000000,
        )

        return

    except Exception:
        pass

    try:
        ctypes.windll.user32.MessageBoxW(
            0,
            "Merci d'avoir utilisé ZEUS-X !",
            "ZEUS-X",
            0x40,
        )
    except Exception:
        pass


def register_close_handler():
    global _CTRL_HANDLER_REF

    if not IS_WINDOWS:
        return

    @ctypes.WINFUNCTYPE(
        ctypes.c_int,
        ctypes.c_uint,
    )
    def _handler(ctrl_type):
        if ctrl_type in (0, 1, 2, 5, 6):
            show_thanks()

            try:
                time.sleep(1.2)
            except Exception:
                pass

        return 0

    _CTRL_HANDLER_REF = _handler

    try:
        ctypes.windll.kernel32.SetConsoleCtrlHandler(
            _CTRL_HANDLER_REF,
            True,
        )
    except Exception:
        pass


# ============================================================
# CONSOLE
# ============================================================

def set_console_title(title="ZEUS-X"):
    if not IS_WINDOWS:
        return

    try:
        ctypes.windll.kernel32.SetConsoleTitleW(
            str(title)
        )
    except Exception:
        try:
            os.system(f"title {title}")
        except Exception:
            pass


def enable_ansi():
    if IS_WINDOWS:
        os.system("")


def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


def move_cursor(row, col):
    sys.stdout.write(
        f"\033[{int(row)};{int(col)}H"
    )


def write_at(row, col, text):
    move_cursor(row, col)
    sys.stdout.write(text)


def setup_console():
    if not IS_WINDOWS:
        return

    if not kernel32.GetConsoleMode(
        console_handle,
        ctypes.byref(original_console_mode),
    ):
        return

    mode = (
        original_console_mode.value
        | ENABLE_MOUSE_INPUT
        | ENABLE_EXTENDED_FLAGS
    ) & ~ENABLE_QUICK_EDIT_MODE

    kernel32.SetConsoleMode(
        console_handle,
        mode,
    )


def restore_console():
    if not IS_WINDOWS:
        return

    try:
        kernel32.SetConsoleMode(
            console_handle,
            original_console_mode.value,
        )
    except Exception:
        pass


def flush_console_input():
    if not IS_WINDOWS:
        return

    try:
        kernel32.FlushConsoleInputBuffer(
            console_handle
        )
    except Exception:
        pass


def read_console_event():
    if not IS_WINDOWS:
        return None

    events = ctypes.c_ulong()

    if not kernel32.GetNumberOfConsoleInputEvents(
        console_handle,
        ctypes.byref(events),
    ):
        return None

    if events.value == 0:
        return None

    record = INPUT_RECORD()
    read = ctypes.c_ulong()

    success = kernel32.ReadConsoleInputW(
        console_handle,
        ctypes.byref(record),
        1,
        ctypes.byref(read),
    )

    if not success:
        return None

    if record.EventType == MOUSE_EVENT:
        if (
            record.MouseEvent.dwButtonState
            & FROM_LEFT_1ST_BUTTON_PRESSED
        ):
            x = (
                record.MouseEvent.dwMousePosition.X
                + 1
            )

            y = (
                record.MouseEvent.dwMousePosition.Y
                + 1
            )

            return (
                "mouse",
                x,
                y,
            )

        return None

    if record.EventType == KEY_EVENT:
        if not record.KeyEvent.bKeyDown:
            return None

        return (
            "key",
            record.KeyEvent.uChar,
            record.KeyEvent.wVirtualKeyCode,
        )

    return None


# ============================================================
# UPDATE SYSTEM
# ============================================================

def parse_version(version):
    if not isinstance(version, str):
        return None

    version = version.strip()

    if version.lower().startswith("v"):
        version = version[1:].strip()

    match = re.fullmatch(
        r"(\d+)\.(\d+)(?:\.(\d+))?",
        version,
    )

    if not match:
        return None

    return (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3) or 0),
    )


def get_latest_version():
    """
    Récupère la version sur github
    """

    try:
        cache_buster = time.time_ns()

        url = (
            f"{VERSION_CHECK_URL}"
            f"?_={cache_buster}"
        )

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "ZEUS-X-Version-Checker/1.0",
                "Accept": "text/plain, */*",
                "Cache-Control": "no-cache, no-store, max-age=0",
                "Pragma": "no-cache",
                "Connection": "close",
            },
            method="GET",
        )

        with urllib.request.urlopen(
            request,
            timeout=10,
        ) as response:

            raw_data = response.read()

        content = raw_data.decode(
            "utf-8-sig"
        )

        for line in content.splitlines():
            line = line.strip()

            if not line:
                continue

            parsed = parse_version(line)

            if parsed is None:
                return None

            return (
                f"{parsed[0]}."
                f"{parsed[1]}."
                f"{parsed[2]}"
            )

    except Exception:
        return None

    return None


def center_position(text, width):
    return max(
        1,
        (width - len(text)) // 2 + 1,
    )


def show_update_prompt(latest):
    clear()
    hide_cursor()

    width, height = (
        shutil.get_terminal_size()
    )

    title = (
        "VOUS UTILISEZ UNE ANCIENNE VERSION"
    )

    current_line = (
        f"Version actuelle : "
        f"{CURRENT_VERSION}"
    )

    latest_line = (
        f"Nouvelle version : "
        f"{latest}"
    )

    question = (
        "Voulez-vous la nouvelle version ?"
    )

    choices = (
        "[Y] Oui        [N] Non"
    )

    lines = [
        "",
        "",
        title,
        "",
        current_line,
        latest_line,
        "",
        question,
        "",
        choices,
    ]

    start_y = max(
        1,
        (height - len(lines)) // 2,
    )

    for index, line in enumerate(lines):
        if line == title:
            color = RED
        elif "[Y]" in line:
            color = WHITE
        else:
            color = GRAY

        x = center_position(
            line,
            width,
        )

        write_at(
            start_y + index,
            x,
            color
            + line
            + RESET,
        )

    sys.stdout.flush()

    if not IS_WINDOWS:
        try:
            choice = input(
                "\nChoix : "
            ).strip().lower()

            return choice in (
                "y",
                "yes",
                "o",
                "oui",
            )

        except (
            EOFError,
            KeyboardInterrupt,
        ):
            return False

    flush_console_input()

    while True:
        event = read_console_event()

        if event is None:
            time.sleep(0.02)
            continue

        if event[0] != "key":
            continue

        key = event[1]

        if not key:
            continue

        key = key.upper()

        if key == "Y":
            return True

        if key == "N":
            return False


def show_redirect_and_wait():
    clear()
    hide_cursor()

    width, height = (
        shutil.get_terminal_size()
    )

    main_text = (
        "Redirection vers le GitHub..."
    )

    sub_text = (
        "Cliquez dans le CMD pour fermer..."
    )

    version_text = (
        f"{CURRENT_VERSION} → "
        f"{UPDATE_AVAILABLE}"
    )

    y = max(
        1,
        height // 2 - 2,
    )

    write_at(
        y,
        center_position(
            main_text,
            width,
        ),
        RED
        + main_text
        + RESET,
    )

    write_at(
        y + 2,
        center_position(
            sub_text,
            width,
        ),
        GRAY
        + sub_text
        + RESET,
    )

    write_at(
        y + 4,
        center_position(
            version_text,
            width,
        ),
        DARK
        + version_text
        + RESET,
    )

    sys.stdout.flush()

    flush_console_input()

    try:
        webbrowser.open_new_tab(
            GITHUB_REPO_URL
        )
    except Exception:
        try:
            webbrowser.open(
                GITHUB_REPO_URL
            )
        except Exception:
            pass

    if not IS_WINDOWS:
        try:
            input(
                "\nAppuie sur Entrée pour fermer..."
            )
        except (
            EOFError,
            KeyboardInterrupt,
        ):
            pass

        return

    while True:
        event = read_console_event()

        if event is None:
            time.sleep(0.02)
            continue

        if event[0] == "mouse":
            return

        if (
            event[0] == "key"
            and event[2] == VK_ESCAPE
        ):
            return


def check_for_update():
    """
    vérifie la version directement dans le RAW GitHub.

    Si version.txt contient une version supérieure à
    CURRENT_VERSION, l'écran d'update apparaît.

    si les versions sont identiques ou si la version locale
    est plus récente, rien ne s'affiche.
    """

    global UPDATE_AVAILABLE
    global UPDATE_DECLINED

    UPDATE_AVAILABLE = None
    UPDATE_DECLINED = False

    # Récupération réelle depuis GitHub
    latest = get_latest_version()

    if latest is None:
        return False

    current_parsed = parse_version(
        CURRENT_VERSION
    )

    latest_parsed = parse_version(
        latest
    )

    if (
        current_parsed is None
        or latest_parsed is None
    ):
        return False

    if latest_parsed == current_parsed:
        return False

    if latest_parsed < current_parsed:
        return False

    UPDATE_AVAILABLE = latest

    wants_update = show_update_prompt(
        latest
    )

    if wants_update:
        show_redirect_and_wait()
        return True

    UPDATE_DECLINED = True

    clear()

    return False


# ============================================================
# INTRO
# ============================================================

def interpolate(c1, c2, amount):
    return tuple(
        int(
            c1[i]
            + (
                c2[i] - c1[i]
            ) * amount
        )
        for i in range(3)
    )


def intro_wave_color(
    x,
    y,
    frame,
    palette,
):
    position = (
        math.sin(
            x * 0.28
            - frame * 0.13
        )
        + 1
    ) / 2

    position += (
        math.sin(
            y * 0.8
            - frame * 0.08
        )
        * 0.08
    )

    position = max(
        0.0,
        min(1.0, position),
    )

    scaled = (
        position
        * (len(palette) - 1)
    )

    index = int(scaled)

    amount = (
        scaled - index
    )

    if index >= len(palette) - 1:
        return palette[-1]

    return interpolate(
        palette[index],
        palette[index + 1],
        amount,
    )


def zerko_color(
    x,
    y,
    frame,
):
    return intro_wave_color(
        x,
        y,
        frame,
        [
            (25, 0, 55),
            (65, 5, 100),
            (105, 15, 155),
            (145, 35, 205),
            (175, 55, 230),
            (110, 35, 200),
            (35, 20, 185),
            (0, 18, 184),
        ],
    )


def get_intro_character_color(
    x,
    y,
    frame,
):
    return zerko_color(
        x,
        y,
        frame,
    )


def get_intro_position():
    terminal_width, terminal_height = (
        shutil.get_terminal_size()
    )

    width = max(
        len(line)
        for line in INTRO_ASCII
    )

    height = len(
        INTRO_ASCII
    )

    x = max(
        1,
        (
            terminal_width
            - width
        ) // 2
        + 1,
    )

    y = max(
        1,
        (
            terminal_height
            - height
        ) // 2
        + 1,
    )

    return x, y


def draw_intro(frame):
    start_x, start_y = (
        get_intro_position()
    )

    for y, line in enumerate(
        INTRO_ASCII
    ):
        move_cursor(
            start_y + y,
            start_x,
        )

        parts = []

        for x, char in enumerate(line):
            if char == " ":
                parts.append(" ")
                continue

            r, g, b = (
                get_intro_character_color(
                    x,
                    y,
                    frame,
                )
            )

            parts.append(
                f"\033[38;2;"
                f"{r};{g};{b}m"
                f"{char}"
            )

        parts.append(RESET)

        sys.stdout.write(
            "".join(parts)
        )

    sys.stdout.flush()


def intro_animation():
    clear()
    hide_cursor()

    frame = 0

    try:
        while True:
            event = (
                read_console_event()
            )

            if event is not None:
                flush_console_input()
                break

            draw_intro(frame)

            frame += 1

            time.sleep(
                0.028
            )

    finally:
        clear()

        sys.stdout.write(
            RESET
        )

        sys.stdout.flush()


# ============================================================
# INTERFACE
# ============================================================

PANEL_W = 94
PANEL_H = 34


def get_interface_layout():
    terminal_width, terminal_height = (
        shutil.get_terminal_size()
    )

    start_x = max(
        1,
        (
            terminal_width
            - PANEL_W
        ) // 2
        + 1,
    )

    start_y = max(
        1,
        (
            terminal_height
            - PANEL_H
        ) // 2,
    )

    return (
        start_x,
        start_y,
        PANEL_W,
    )


def pad_name(
    name,
    width=22,
):
    if len(name) > width:
        return (
            name[: width - 1]
            + "…"
        )

    return (
        name
        + " "
        * (
            width
            - len(name)
        )
    )


def get_tool_positions(page):
    start_x, start_y, _ = (
        get_interface_layout()
    )

    tools = PAGES[page][
        "tools"
    ]

    left_x = start_x + 5
    right_x = start_x + 50
    grid_y = start_y + 14
    cell_w = 38

    positions = []

    for index in range(
        len(tools)
    ):
        if index < 5:
            x = left_x
            y = (
                grid_y
                + index * 2
            )
        else:
            x = right_x
            y = (
                grid_y
                + (
                    index - 5
                ) * 2
            )

        positions.append(
            (
                x,
                y,
                x + cell_w,
                y,
            )
        )

    return positions


def draw_hbar(
    y,
    start_x,
    w,
    left="├",
    right="┤",
):
    write_at(
        y,
        start_x,
        LINE
        + left
        + "─"
        * (
            w - 2
        )
        + right
        + RESET,
    )


def draw_interface(page):
    clear()

    start_x, start_y, w = (
        get_interface_layout()
    )

    data = PAGES[page]
    tools = data["tools"]

    write_at(
        start_y,
        start_x,
        LINE
        + "╭"
        + "─"
        * (
            w - 2
        )
        + "╮"
        + RESET,
    )

    for r in range(
        1,
        PANEL_H - 1,
    ):
        write_at(
            start_y + r,
            start_x,
            LINE
            + "│"
            + RESET,
        )

        write_at(
            start_y + r,
            start_x + w - 1,
            LINE
            + "│"
            + RESET,
        )

    write_at(
        start_y
        + PANEL_H
        - 1,
        start_x,
        LINE
        + "╰"
        + "─"
        * (
            w - 2
        )
        + "╯"
        + RESET,
    )

    brand = " ZEUS-X "

    write_at(
        start_y,
        start_x + 3,
        LINE
        + "┬"
        + RESET,
    )

    write_at(
        start_y,
        start_x + 4,
        OPT
        + brand
        + RESET,
    )

    write_at(
        start_y,
        start_x + 4
        + len(brand),
        LINE
        + "┬"
        + RESET,
    )

    tag = (
        f" {page + 1:02d}"
        f"/{len(PAGES):02d} "
    )

    write_at(
        start_y,
        start_x
        + w
        - 3
        - len(tag),
        LINE
        + "┬"
        + RESET,
    )

    write_at(
        start_y,
        start_x
        + w
        - 2
        - len(tag),
        SOFT_PURPLE
        + tag
        + RESET,
    )

    write_at(
        start_y,
        start_x + w - 2,
        LINE
        + "┬"
        + RESET,
    )

    logo_w = max(
        len(line)
        for line in INTERFACE_ASCII
    )

    logo_x = (
        start_x
        + (
            w
            - logo_w
        ) // 2
    )

    colored = Colorate.Horizontal(
        Colors.blue_to_purple,
        "\n".join(
            INTERFACE_ASCII
        ),
    )

    for i, line in enumerate(
        colored.splitlines()
    ):
        write_at(
            start_y + 2 + i,
            logo_x,
            line,
        )

    link = (
        "https://guns.lol/zerko.pro / "
        "https://guns.lol/zerko.off / "
        "https://guns.lol/zxk.off"
    )

    write_at(
        start_y + 8,
        start_x
        + (
            w
            - len(link)
        ) // 2,
        GRAY
        + link
        + RESET,
    )

    # ========================================================
    # VERSION
    # ========================================================

    version_offset = 0

    if (
        UPDATE_DECLINED
        and UPDATE_AVAILABLE
    ):
        version_text = (
            "ancienne version → "
            f"{UPDATE_AVAILABLE}"
        )

        write_at(
            start_y + 9,
            start_x
            + (
                w
                - len(version_text)
            ) // 2,
            RED
            + version_text
            + RESET,
        )

        draw_hbar(
            start_y + 10,
            start_x,
            w,
        )

        tab_y = (
            start_y + 11
        )

        version_offset = 1

    else:
        draw_hbar(
            start_y + 9,
            start_x,
            w,
        )

        tab_y = (
            start_y + 10
        )

    tab_x = start_x + 3
    max_x = start_x + w - 3

    for i, p in enumerate(
        PAGES
    ):
        name = p["label"]

        step = (
            len(name)
            + 2
        )

        if (
            tab_x + step
            > max_x
        ):
            break

        if i == page:
            chunk = (
                OPT
                + "█"
                + WHITE
                + name
                + RESET
                + " "
            )
        else:
            chunk = (
                DIM
                + " "
                + DARK
                + name
                + RESET
                + " "
            )

        write_at(
            tab_y,
            tab_x,
            chunk,
        )

        tab_x += step

    # séparation
    title_bar_y = (
        tab_y + 1
    )

    draw_hbar(
        title_bar_y,
        start_x,
        w,
    )

    # titre
    write_at(
        title_bar_y + 1,
        start_x + 4,
        OPT
        + "◆"
        + RESET
        + " "
        + WHITE
        + data["label"]
        + RESET
        + DIM
        + "  —  "
        + RESET
        + GRAY
        + data["hint"]
        + RESET,
    )

    positions = (
        get_tool_positions(page)
    )

    for index, (
        key,
        name,
        _,
    ) in enumerate(tools):
        x, y, _, _ = (
            positions[index]
        )

        if version_offset:
            y += version_offset

        num = key.rjust(2)

        row = (
            OPT
            + "▌"
            + RESET
            + " "
            + OPT
            + "["
            + num
            + "]"
            + RESET
            + DIM
            + " │ "
            + RESET
            + WHITE
            + pad_name(
                name,
                22,
            )
            + RESET
        )

        write_at(
            y,
            x,
            row,
        )

    bottom_bar = (
        start_y
        + PANEL_H
        - 6
    )

    draw_hbar(
        bottom_bar,
        start_x,
        w,
    )

    dots = []

    for i in range(
        len(PAGES)
    ):
        if i == page:
            dots.append(
                OPT
                + "●"
                + RESET
            )
        else:
            dots.append(
                DIM
                + "○"
                + RESET
            )

    dots_str = " ".join(
        dots
    )

    dots_len = (
        len(PAGES) * 2
        - 1
    )

    write_at(
        bottom_bar + 1,
        start_x
        + (
            w
            - dots_len
        ) // 2,
        dots_str,
    )

    draw_hbar(
        bottom_bar + 2,
        start_x,
        w,
    )

    parts = [
        OPT
        + "[1-0]"
        + RESET
        + WHITE
        + " ouvrir"
        + RESET,

        OPT
        + "[Clic]"
        + RESET
        + WHITE
        + " ouvrir"
        + RESET,
    ]

    if page > 0:
        parts.append(
            OPT
            + "[A]"
            + RESET
            + WHITE
            + " précédent"
            + RESET
        )

    if page < len(PAGES) - 1:
        parts.append(
            OPT
            + "[E]"
            + RESET
            + WHITE
            + " suivant"
            + RESET
        )

    parts.append(
        OPT
        + "[ESC]"
        + RESET
        + WHITE
        + " quitter"
        + RESET
    )

    controls = (
        f"  {DIM}·{RESET}  "
        .join(parts)
    )

    plain = [
        "[1-0] ouvrir",
        "[Clic] ouvrir",
    ]

    if page > 0:
        plain.append(
            "[A] précédent"
        )

    if page < len(PAGES) - 1:
        plain.append(
            "[E] suivant"
        )

    plain.append(
        "[ESC] quitter"
    )

    plain_len = len(
        "  ·  ".join(plain)
    )

    write_at(
        bottom_bar + 3,
        start_x
        + max(
            3,
            (
                w
                - plain_len
            ) // 2,
        ),
        controls,
    )

    sys.stdout.flush()


# ============================================================
# OUTILS
# ============================================================

def get_clicked_tool(
    mouse_x,
    mouse_y,
    page,
):
    positions = (
        get_tool_positions(page)
    )

    for index, (
        x1,
        y,
        x2,
        _,
    ) in enumerate(
        positions
    ):
        if (
            UPDATE_DECLINED
            and UPDATE_AVAILABLE
        ):
            y += 1

        if (
            x1 <= mouse_x <= x2
            and mouse_y == y
        ):
            return index

    return None


def open_tool(
    page,
    index,
):
    tools = PAGES[page][
        "tools"
    ]

    if (
        index < 0
        or index >= len(tools)
    ):
        return

    _, _, url = tools[
        index
    ]

    if not url:
        return

    try:
        webbrowser.open_new_tab(
            url
        )
    except Exception:
        try:
            webbrowser.open(
                url
            )
        except Exception:
            pass


# ============================================================
# MENU
# ============================================================

def menu():
    page = 0

    draw_interface(
        page
    )

    try:
        while True:
            event = (
                read_console_event()
            )

            if event is None:
                time.sleep(
                    0.018
                )
                continue

            if event[0] == "mouse":
                selected = (
                    get_clicked_tool(
                        event[1],
                        event[2],
                        page,
                    )
                )

                if selected is not None:
                    open_tool(
                        page,
                        selected,
                    )

                continue

            if event[0] != "key":
                continue

            key, vk = (
                event[1],
                event[2],
            )

            if (
                IS_WINDOWS
                and vk == VK_ESCAPE
            ):
                break

            if key == "\x1b":
                break

            if not key:
                continue

            normalized = (
                key.upper()
            )

            if (
                normalized == "E"
                and page
                < len(PAGES) - 1
            ):
                page += 1

                draw_interface(
                    page
                )

                continue

            if (
                normalized == "A"
                and page > 0
            ):
                page -= 1

                draw_interface(
                    page
                )

                continue

            if normalized == "0":
                open_tool(
                    page,
                    9,
                )

                continue

            for index, tool in enumerate(
                PAGES[page]["tools"]
            ):
                if (
                    normalized
                    == tool[0].upper()
                ):
                    open_tool(
                        page,
                        index,
                    )

                    break

    finally:
        sys.stdout.write(
            RESET
        )

        show_cursor()

        sys.stdout.flush()


# ============================================================
# MAIN
# ============================================================

def main():
    set_console_title(
        "ZEUS-X"
    )

    enable_ansi()
    setup_console()

    try:
        if check_for_update():
            return

        if not IS_WINDOWS:
            print(
                f"{PURPLE}"
                "⚠ Optimisé pour Windows "
                "(souris + console)."
                f"{RESET}"
            )

            print(
                f"{GRAY}"
                "  Sur Linux/Mac la souris "
                "ne fonctionnera pas."
                f"{RESET}"
            )

            print(
                f"{DARK}"
                "  Appuie sur Entrée "
                "pour continuer..."
                f"{RESET}"
            )

            input()

        set_console_title(
            "ZEUS-X"
        )

        register_close_handler()

        hide_cursor()

        intro_animation()

        menu()

    finally:
        show_cursor()

        restore_console()

        sys.stdout.write(
            RESET
        )

        sys.stdout.flush()

        clear()

        show_thanks()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        show_cursor()
        restore_console()

        sys.stdout.write(
            RESET
        )

        sys.stdout.flush()

        clear()

        show_thanks()

        sys.exit(0)

    except Exception as error:
        show_cursor()
        restore_console()

        sys.stdout.write(
            RESET
        )

        sys.stdout.flush()

        clear()

        print()

        print(
            f"{OPT}Erreur :{RESET} "
            f"{error}"
        )

        input(
            f"\n{GRAY}"
            "Appuie sur Entrée "
            "pour quitter..."
            f"{RESET}"
        )

        show_thanks()
