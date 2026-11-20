# Mező Clicker v1.2

A standalone desktop clicker game built with **Python** and **Pygame**, featuring local account authentication with PBKDF2 password hashing, multi-category upgrades with shared category scaling, rebirth prestige multipliers, a skin locker with rarity tiers and a gamble spinner, daily login streak rewards, and persistent per-user save files.

---

## Features

* **Core Clicking & Automation:** Click the target or press `Space` to earn points, trigger critical hits (`crit_chance` and `crit_multiplier`), spawn floating combat/score text, and scale passive income and auto-clickers per second.


* **Four Upgrade Categories with Shared Scaling:**
* **Click Power:** Flat click power increases (`+1` up to `+50M` per level).


* **Auto-Income:** Passive points per second (`+1/s` up to `+7.5B/s`).


* **Multipliers:** Percentage boosts to all income (`+10%` up to `+1200%`).


* **Critical Chance:** Crit chance (capped at `75%`), crit multiplier bonuses, and auto-clicker turrets.


* Buying any upgrade increases a shared price multiplier across that category (`shared_scale`) in addition to individual upgrade growth.




* **Rebirth System:** Reset current score, clicks, upgrades, and category scaling once you reach `rebirth_cost` (starting at `1,000` and multiplying by `10x` per rebirth) to permanently double (`2.0x`) your rebirth multiplier.


* **Skins, Rarity Tiers & Gamble Wheel:**
* 13 selectable skins (`Szomszéd` through `ShyMezo`) with individual income multipliers (`1.00x` up to `2.80x`) and rarity tiers (`Common`, `Rare`, `Epic`, `Mythic`, `Legendary`, with `Secret` tier support).


* Optional integration with an external `rarity_system` module (`RaritySystem`, `RarityTier`) if present in the parent directory, with a built-in fallback rarity system.


* Unlock skins through rebirth milestones or spend `100,000` points on the **Gamble** spinner (duplicates refund `25,000` points).




* **Daily Rewards:** Claim daily rewards every 24 hours; claiming within a 48-hour window builds your login streak and increases the payout.


* **Local Accounts & Sessions:** Sign up or log in with username (`3–20` alphanumeric/underscore characters) and password (`4+` characters), hashed with `PBKDF2-HMAC-SHA256` (`200,000` iterations) and random salts, with persistent session tokens and autosaving every 15 seconds.


* **Configurable Display, Audio & Stats:** Adjust master volume, resolution (`1280x720`, `1600x900`, `1920x1080`), fullscreen toggle, and FPS cap (`30`, `60`, `120`, `144`, `Unlimited`), inspect lifetime player stats, and adapt layout for desktop or compact/mobile-like window dimensions.



---

## Project Structure

```text
.
├── clicker_windows_4.py     # Main Pygame client and game logic
├── rarity_system.py         # Optional external rarity module (looked up in ../)
├── bgp.webp                 # Optional background image
├── clickPIC.jpg             # Optional fallback clicker image
├── mezoegypedo.wav          # Optional looping background music
├── click_sound.wav          # Optional click sound effect
└── <skin image files>       # Optional skin assets (e.g., mezodeafult.jpg, mezo2.jpg, ...)

```

If optional image or audio files are missing, the game falls back cleanly to generated surfaces or silent audio and logs errors to `crash.log`.

---

## Requirements & Installation

1. **Python 3.10+** (standard library modules used: `hashlib`, `hmac`, `json`, `os`, `random`, `re`, `secrets`, `sys`, `traceback`, `datetime`, `pathlib`).


2. **Pygame:**

```bash
pip install pygame

```

---

## Running the Game

```bash
python clicker_windows_4.py

```

### Controls

* **Mouse Click / `Space`:** Earn points (and trigger crits).


* **Mouse Wheel / Scrollbar / Drag:** Scroll through Upgrades, Skins, Rebirth details, Stats, Daily Rewards, and Settings.


* **`Esc`:** Close open popups or panels.


* **Login / Sign Up Screen:** Click a field or press `Tab` to switch between Username and Password, type to enter text, and press `Enter` or click the submit button.



---

## Save Data & Logs

User data, settings, sessions, and crash logs are stored under:

```text
%USERPROFILE%\AppData\Local\MezoClicker\

```

* `settings.json` — Display and audio preferences


* `users.json` — User accounts, PBKDF2 password hashes/salts, and daily reward streak state


* `client_session.json` — Active login session token


* `save_<username>.json` — Per-user game state save file (written atomically via a `.tmp` file)


* `crash.log` — Timestamped unhandled exceptions and initialization/audio errors



---

## Packaging for Windows (PyInstaller)

The script checks `sys._MEIPASS` via `_bundle_dir()`, making it compatible with bundled single-file or folder builds:

```bash
pyinstaller --onefile --windowed clicker_windows_4.py

```

If bundling image or `.wav` assets alongside the executable, include them with PyInstaller's `--add-data` option so they resolve under `_MEIPASS`.
